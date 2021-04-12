# Leave Community On Dead Homeserver <!-- omit in toc -->

This article is licensed under the standard MIT license. See [[Home]] for a full copy.

This guide explains a working, but dirty solution to leave a community that used to live on a homeserver that now is dead.

[Element Web issue](https://github.com/vector-im/element-web/issues/10383)

[Synapse issue](https://github.com/matrix-org/synapse/issues/5254)

## Requirements

* Your account is on your own homeserver, or a homeserver you have access to change the configuration of
* You own any domain (in ths guide, this will be `yourDomain.com`)
* You have a web server to host a web site and a temporary Synapse on. This guide include examples for nginx

## Overview

This guide will explain how to leave the community `+deadCommunity:deadHsDomain.com` when the homeserver on the domain `deadHsDomain.com` is dead. You do not need to own or have access to this domain to continue.

<!-- TOC depthfrom:3 -->

- [Requirements](#requirements)
- [Overview](#overview)
- [Steps](#steps)
  - [Serve well-known files on deadHsDomain.com](#serve-well-known-files-on-deadhsdomaincom)
  - [Set up a Synapse server on deadHsDomain.com](#set-up-a-synapse-server-on-deadhsdomaincom)
  - [Log in to deadHsDomain.com and create the community](#log-in-to-deadhsdomaincom-and-create-the-community)
  - [Make your primary Synapse federate with deadHsDomain.com](#make-your-primary-synapse-federate-with-deadhsdomaincom)
  - [Leave the community](#leave-the-community)
  - [Clean up](#clean-up)

<!-- /TOC -->

## Steps

### Serve well-known files on deadHsDomain.com

On your web server, create `/etc/nginx/sites-available/deadHsDomain.com` with the following content:

```
server {
        listen 443;
        listen [::]:443;
        server_name deadHsDomain.com;
        location /.well-known/matrix/client {
                return 200 '{"m.homeserver": {"base_url": "https://temporarySubDomain.yourDomain.com"},"m.identity_server": {"base_url": "https://vector.im"}}';
                add_header Content-Type application/json;
                add_header "Access-Control-Allow-Origin" *;
         }
        location /.well-known/matrix/server {
                return 200 '{"m.server": "temporarySubDomain.yourDomain.com:443"}';
                add_header Content-Type application/json;
         }
}
```

Enable this site: `ln -s /etc/nginx/sites-available/deadHsDomain.com /etc/nginx/sites-enabled/deadHsDomain.com`

Validate nginx config: `nginx t`

Reload nginx: `systemctl reload nginx`

Add the following to the `hosts` file on your local computer, and to your primary Matrix server. Use the IP of your web server

```
1.2.3.4 deadHsDomain.com
```

You should now be able to talk to this domain from both your local computer and from your primary Matrix server.

```
$ curl --insecure "https://deadHsDomain.com/.well-known/matrix/client"
{"m.homeserver": {"base_url": "https://temporarySubDomain.yourDomain.com"},"m.identity_server": {"base_url": "https://vector.im"}}

curl --insecure "https://deadHsDomain.com/.well-known/matrix/server"
{"m.server": "temporarySubDomain.yourDomain.com:443"
```

### Set up a Synapse server on deadHsDomain.com

Create a DNS `A` record for the sub domain you added to the well-known files in last step, point this to the IP of your web server

On your web server, create `/etc/nginx/sites-available/temporarySubDomain.yourDomain.com` with the following content:

```
server {
    listen 80;
    listen [::]:80;
    server_name temporarySubDomain.yourDomain.com;
    location / {
            proxy_pass http://localhost:8008;
            proxy_set_header X-Forwarded-For ]$remote_addr;
    }
}
```

Enable this site

Enable SSL on this site with certbot, select redirect HTTP to HTTPS when asked

Install Synapse according to the [documentation](https://github.com/matrix-org/synapse/blob/develop/INSTALL.md) using `deadHsDomain.com` as the `--server-name`

Postgres not needed as this server is temporary

Add the following to the top of the Synapse config file:

```
federation_verify_certificates: false
use_insecure_ssl_client_just_for_testing_do_not_use: true
```

Then replace 
```
trusted_key_servers:
  - server_name: "matrix.org"
```
with
```
trusted_key_servers:
  - server_name: "matrix.org"
    accept_keys_insecurely: true
```

Start Synapse

You should now be able to load `https://temporarySubDomain.yourDomain.com/_matrix/static/` in your browser with no errors and valid certificate. It should show `It works! Synapse is running`

Create an account on the homeserver according to https://github.com/matrix-org/synapse/blob/develop/INSTALL.md#registering-a-user - Which username you choose does not matter



### Log in to deadHsDomain.com and create the community

Repeat this step multiple times if you want to leave multiple communities on this dead homeserver.

Go to [Element Web](https://app.element.io/) -- Sign in -- Change homeserver

Set Homeserver URL to `https://temporarySubDomain.yourDomain.com`

Click Next

Log in with the username and password you created earlier

Create the community you want to leave

Stop the `deadHsDomain.com` Synapse

Add the following to the Synapse DB on `deadHsDomain.com`. Replace
* `+deadCommunity:deadHsDomain.com` with the community you created earlier
* `@you:yourMatrixDomain.com` wth your primary Matrix ID, the user you want to leave the community
* `1601386190185` with a timestamp a couple of days into the future
* `yourMatrixDomain.com`  with the domain of your primary Matrix server

```sql
INSERT INTO group_attestations_renewals (group_id, user_id, valid_until_ms)
VALUES ('+deadCommunity:deadHsDomain.com', '@you:yourMatrixDomain.com', 1601386190185);

INSERT INTO group_users (group_id, user_id, is_admin, is_public)
VALUES ('+deadCommunity:deadHsDomain.com', '@you:yourMatrixDomain.com', 'f', 't');

INSERT INTO group_attestations_remote (group_id, user_id, valid_until_ms, attestation_json)
VALUES ('+deadCommunity:deadHsDomain.com', '@you:yourMatrixDomain.com', 1601402356216, '{"group_id":"+deadCommunity:deadHsDomain.com","signatures":{"yourMatrixDomain.com":{"ed25519:a_RXGa":"IDontThinkWhatYouPutHereMattersMuchItsGonnaBeInvalidNoMatterWhat"}},"user_id":"@you:yourMatrixDomain.com","valid_until_ms":1601402356216}');
```

Start the `deadHsDomain.com` Synapse


### Make your primary Synapse federate with deadHsDomain.com

**NOTE: this step makes your homeserver insecure. You want to have it running with these options as short as possible**


Add the following to the top of the Synapse config file:

```
federation_verify_certificates: false
use_insecure_ssl_client_just_for_testing_do_not_use: true
```

Replace 
```
trusted_key_servers:
  - server_name: "matrix.org"
```
With
```
trusted_key_servers:
  - server_name: "matrix.org"
    accept_keys_insecurely: true
```

Restart Synapse

### Leave the community

In Element, on your main account. Go to the community -- Community settings -- Leave community

### Clean up

Remove these three lines from the Synapse config file on your primary Synapse

```
federation_verify_certificates: false
use_insecure_ssl_client_just_for_testing_do_not_use: true
    accept_keys_insecurely: true
```

Restart synapse

Stop and delete the temporary Synapse installation on `deadHsDomain.com`

Remove the nginx config for `temporarySubDomain.yourDomain.com` and `deadHsDomain.com`. Also revoke the certificate with certbot

Remove the DNS A record for `temporarySubDomain.yourDomain.com`

Remove the `deadHsDomain.com` record in the `hosts` file on your computer and your primary Matrix server
