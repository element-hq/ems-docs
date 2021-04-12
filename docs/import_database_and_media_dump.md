# Import Database and Media Dump <!-- omit in toc -->

This article is licensed under the standard MIT license. See [[Home]] for a full copy.

This article is structured for an export from EMS, but may also be applicable in other circumstances.

For support on Synapse or matrix-media-repo, ask in the Matrix rooms [#synapse:matrix.org](https://matrix.to/#/#synapse:matrix.org) and [#mediarepo:t2bot.io](https://matrix.to/#/#mediarepo:t2bot.io)

## Prerequisites
You need these items to complete the import. If you are migrating from EMS, EMS support will provide all five to you

- Database dump
- Media export
- GPG decryption password
- Pepper
- Synapse signing key

## Import process

1. Following official documentation, install and configure
   1. [PostgreSQL](https://www.postgresql.org/)
   2. [Synapse](https://github.com/matrix-org/synapse/)
   3. [matrix-media-repo](https://github.com/turt2live/matrix-media-repo)
2. When generating your Synapse configuration file, you MUST use the same domain as your EMS server.
3. Do not start Synapse yet.
4. In the Synapse config file (usually `homeserver.yaml`), set:
   1. [pepper](https://github.com/matrix-org/synapse/blob/develop/docs/sample_config.yaml#L2020-L2034) to the value received. If you do not to this you have to reset all passwords.
   2. Signing key. This is stored in a file. See [this](https://github.com/matrix-org/synapse/blob/develop/docs/sample_config.yaml#L1452-L1454) config file option for path. Alternatively, add the old key to [old_signing_keys](https://github.com/matrix-org/synapse/blob/develop/docs/sample_config.yaml#L1459-L1469).
5. Download the database and media exports provided.
6. Decrypt and extract the exports
    ```bash
    gpg --no-symkey-cache --output postgres-export.sql.gz --decrypt postgres-export.sql.gz.gpg
    gpg --no-symkey-cache --output export-part-1.tgz --decrypt export-part-1.tgz.gpg
    gzip --decompress postgres-export.sql.gz
    tar zxvf export-part-1.tgz
    ```
7. Import the database dump
   1. If your Synapse database is not empty, empty it  
        **WARNING - THIS WILL IMMEDIATELY AND IRRECOVERABLY DELETE DATA. I TAKE NO RESPONSIBILITY IF YOU DELETE THE WRONG DATABASE OR THE WRONG DATA**

        Connect to the database with `psql`, then run the following queries:
        ```sql
        DO $$ DECLARE
        r RECORD;
        BEGIN
            FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = current_schema()) LOOP
                EXECUTE 'DROP TABLE ' || quote_ident(r.tablename) || ' CASCADE';
            END LOOP;
        END $$;

        DROP sequence cache_invalidation_stream_seq;
        DROP sequence state_group_id_seq;
        DROP sequence user_id_seq;
        ```
   2. Disconnect from the database, then import the database dump
        ```bash
        psql --username=USERNAME --host=HOSTNAME DATABASE_NAME < postgres-export.sql
        ```
   3. Verify that sequence was set correctly. Connect to the database and run the query
        ```sql
        SELECT * FROM state_group_id_seq;
        ```
        `last_value` should be greater than 1
8. Import media according to documentation [here](https://github.com/turt2live/matrix-media-repo/blob/master/docs/admin.md#exportingimporting-data).
9. Start Synapse.
10. Optionally, install [Element Web](https://github.com/vector-im/element-web) or use another [Matrix client](https://matrix.org/clients/).