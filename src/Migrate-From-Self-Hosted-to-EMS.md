# Migrate From Self Hosted to EMS

This article is licensed under the standard MIT license. See [Home](index.md) for a full copy.


## Notes

* Except where specified, you should be able to just copy-paste each command in succession.
* Please do not change any file names anywhere.

## SSH to your matrix server

You might want to run everything in a `tmux` or a `screen` session to avoid disruption in case of a lost SSH connection.

## Generate password for gpg encryption
```bash
pwgen -s 64 1
```

Alternately, you can use our GPG key. Note, this expires on 2022-04-22, if this is soon, please talk to your EMS contact.    
[ems-support-public.pgp](ems-support-public.pgp)

## GPG

If `gpg` is being uncooperative, use the command `gpgconf --kill gpg-agent`.

## Create a folder to store everything

```bash
mkdir -p /tmp/synapse_export
cd /tmp/synapse_export
```

The guide from here on assumes your current working directory is `/tmp/synapse_export`.

### Set restrictive permissions on the folder

If you are working as root: (otherwise set restrictive permissions as needed):

```bash
chmod 000 /tmp/synapse_export
```

## Copy Synapse config

Copy the following files and send to EMS Support:
* Your Synapse configuration file (usually `homeserver.yaml`)
* Your message signing key.
    * This is stored in a separate file. See the Synapse config file for the path. The variable is `signing_key_path` [https://github.com/matrix-org/synapse/blob/v1.32.2/docs/sample_config.yaml#L1526-L1528](https://github.com/matrix-org/synapse/blob/v1.32.2/docs/sample_config.yaml#L1526-L1528)


## Stop Synapse

**DO NOT START IT AGAIN AFTER THIS**

## Database export

### PostgreSQL

#### Dump, compress and encrypt

Replace:
* `<dbhost>` (ip or fqdn for your database server)
* `<dbusername>` (username for your synapse database)
* `<dbname>` (the name of the database for synapse)

```bash
pg_dump -O -h <dbhost> -U <dbusername> -d <dbname> | gzip > customer_db_export.sql.gz
gpg --symmetric --no-symkey-cache customer_db_export.sql.gz
rm customer_db_export.sql.gz
```

#### If required, split into smaller files

Please only do this if you have a slow connection and are worried about transferring a single large file.

```bash
split -b 100m customer_db_export.sql.gz.gpg customer_db_export.sql.gz.gpg.part-
rm customer_db_export.sql.gz.gpg
```

### SQLIte

#### Compress and encrypt

```bash
tar -zcvf homeserver.db.tar.gz /path/to/homeserver.db
gpg --symmetric --no-symkey-cache homeserver.db.tar.gz
rm homeserver.db.tar.gz
```

#### If required, split into smaller files

Please only do this if you have a slow connection and are worried about transferring a single large file.

```bash
split -b 100m homeserver.db.tar.gz homeserver.db.tar.gz.part-
rm homeserver.db.tar.gz
```

## Media export

### If you are using SQLIte as database

Skip ahead to and follow [Backup media export](#backup-media-export).

### Download the export tool

Download the latest version of `export_synapse_for_import-linux-x64` (or ` export_synapse_for_import-win-x64.exe`) from [https://github.com/turt2live/matrix-media-repo/releases](https://github.com/turt2live/matrix-media-repo/releases)

```bash
wget https://github.com/turt2live/matrix-media-repo/releases/download/vx.x.x/export_synapse_for_import-linux-x64
chmod +x export_synapse_for_import-linux-x64
```

### Run the export

Replace:
* `<dbhost>` (ip or fqdn for your database server)
* `<dbname>` (the name of the database for synapse)
* `<dbusername>` (username for your synapse database)
* `/path/to/synapse/media_store` (the path to where synapse stores your media)
* `<yourdomain.tld>` (the domain for your server. this is the part that is in your usernames)

```bash
./export_synapse_for_import-linux-x64 -h
./export_synapse_for_import-linux-x64 -dbHost <dbhost> -dbPort 5432 -dbName <dbname> -dbUsername <dbusername> -mediaDirectory /path/to/synapse/media_store -serverName <yourdomain.tld> -destination ./customer_media_export
mv logs customer_media_export
mv media-repo.yaml customer_media_export
rm export_synapse_for_import-linux-x64
```

### Compress and encrypt
```bash
tar -zcvf customer_media_export.tar.gz customer_media_export
gpg --symmetric --no-symkey-cache customer_media_export.tar.gz
rm customer_media_export.tar.gz
rm -r customer_media_export
```

### If required, split into smaller files

Please only do this if you have a slow connection and are worried about transferring a single large file.

```bash
split -b 100m customer_media_export.tar.gz.gpg customer_media_export.tar.gz.gpg.part-
rm customer_media_export.tar.gz.gpg
```

## Backup media export

### Compress and encrypt

Replace * `/path/to/synapse/media_store` (the path to where synapse stores your media)

```bash
tar -zcvf customer_backup_media_export.tar.gz /path/to/synapse/media_store
gpg --symmetric --no-symkey-cache customer_backup_media_export.tar.gz
rm customer_backup_media_export.tar.gz
```

### If required, split into smaller files

Please only do this if you have a slow connection and are worried about transferring a single large file.

```bash
split -b 100m customer_backup_media_export.tar.gz.gpg customer_backup_media_export.tar.gz.gpg.part-
rm customer_backup_media_export.tar.gz.gpg
```

## Transfer
Download the files, then upload to the Google Drive folder shared by EMS or a location as agreed with your EMS contact.

While transfer is running, you should edit or create the well-known files and CNAME DNS records to point to your EMS host.

On your local computer:

```bash
scp -r -P 1234 -i ~/.ssh/matrix-server youruser@1.2.3.4:/tmp/synapse_export /some/local/folder
```

## Cleanup

We strongly recommend that you leave the export and Synapse untouched until the import is finished and everything is verified working.

## Note on users and Element

Element does have support for changing the delegated homeserver URL. All your users will have to sign out and sign in again to Element. You should ensure everyone have Key Backup set configured and working.
