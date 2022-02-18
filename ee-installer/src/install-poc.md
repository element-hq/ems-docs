# Element Enterprise Installer: How to Install a POC Environment

## Overview

Our Element Enterprise Installer can handle the installation of Element Proof
of Concept (POC) environments. Our standard POC environment is a single node
server with multik8s running that we deploy our Element Enterprise Operator
to, resulting in a fully functioning Synapse server with Element Web that
can be used to conduct a POC. On-premise production deployments use the
same installer and operator, but are intended to be deployed into a full
kubernetes environment.

To get started with a POC installation, there are several things that need
to be considered and this guide will work through them:

- [Hostnames/DNS](install-poc.md#hostnamesdns)
- [Machine Size](install-poc.md#machine-size)
- [Operating System](install-poc.md#operating-system) (We’ve tested on
Ubuntu Server 20.04)
- [Network Ports to Open](install-poc.md#network-ports-to-open)
- [Postgresql Database](install-poc.md#postgresql-database)
- [SSL Certificates](install-poc.md#ssl-certificates)
- [Extra configuration items](install-poc.md#extra-configuration-items)

Once these areas have been covered, you’ll be able to install a POC
environment!

## Hostnames/DNS

You will need hostnames for the following pieces of infrastructure:

- Postgresql Server
- Element Server
- Synapse Server

These hostnames must resolve to the appropriate IP addresses. If you have a
proper DNS server with records for these hostnames in place, then you will
be good to go.

`/etc/hosts` may be used as an alternative to proper DNS in a POC scenario
only. In this case, you will need entries similar to:

```plaintext
192.168.122.39 element.local element
192.168.122.39 synapse.local synapse
```

## Machine Size

For running a proof of concept with our installer, we support only the x86_64
architecture and recommend the following minimums:

- No federation: 4 vCPUs/CPUS and 16GB RAM
- Federation: 8 vCPUs/CPUS and 32GB RAM

## Operating System

To get started, we have tested on Ubuntu 20.04 and suggest that you start
there as well. For x86_64, you can grab the iso here:

<https://releases.ubuntu.com/20.04.3/ubuntu-20.04.3-live-server-amd64.iso>

Make sure to select docker as a package option. Do set up ssh.

Once you log in, please run:

```bash
sudo apt-get update
sudo apt-get upgrade
```

### Further Pre-requisites

You should have the installer unpacked in a directory on your server. We
will refer to this as the installer directory. Both the `parameters.yml`
and `secrets.yml` file live in this directory.

Please run the following commands to create the `/mnt/data` directory and
install the `python3-signedjson package` which will be used during the
configuration of the installer.

The `/mnt/data` directory should have at least 50 GB of space.

```bash
# mkdir /mnt/data

# apt-get install python3-signedjson -y
```

### Network Ports to Open

Element Enterprise On-Premise needs to bind and serve content over:

- Port 80 TCP
- Port 443 TCP

In a default Ubuntu installation, these ports are allowed through the
firewall. You will need to ensure that these ports are passed through your
firewall.

### Unpacking the Installer

Please make sure that you unpack `element-enterprise-installer` onto your
POC system. The directory that it unpacks into will be referenced in this
document as the installer directory.

## Postgresql Database

The installation requires that you have a postgresql
database with a locale of C and UTF8 encoding set up. See
<https://github.com/matrix-org/synapse/blob/develop/docs/postgres.md#set-up-database>
for further details.

If you have this already, please make note of the database name, user,
and password as you will need these to begin the installation.

If you do not have a database that you can already connect to and you are
doing this for a POC only and not in production, you can create a quick
Postgresql database on the machine you’ll be doing the POC on. Element
does not ship Postgresql and you'll see these instructions rely on the Docker
Hub image for Postgresql.

To do this you can run:

```bash
docker pull docker.io/postgres:latest
```

Install the `pwgen` utility:

```bash
apt-get install pwgen -y
```

Generate a password to replace `insert_random_password_here` in the script
by doing:

```bash
pwgen 32 1
```

Then create a script, `start_postgresql`:

```bash
#!/bin/bash

docker run -d -p 5432:5432 -v $(pwd)/data:/var/lib/postgresql/data -e
POSTGRES_PASSWORD="insert_random_password_here" -e POSTGRES_USER="element"
-e POSTGRES_DB="element" -e POSTGRES_INITDB_ARGS="--encoding UTF8 --locale C" d
ocker.io/postgres:latest
```

Now create a directory for the postgresql database:

```bash
mkdir data
```

Set the executable permission on `start_postgresql`:

```bash
chmod +x start_postgresql
```

and finally start postgresql:

```bash
./start_postgresql
```

## SSL Certificates

For SSL Certificates, you have three options:

- Signed certificates from an internet recognized authority.
- LetsEncrypt
- Self-signed certificates

In the case of Signed certificates or LetsEncrypt, your hostnames must be
accessible on the internet.

In the case of self-signed certificates, these are acceptable for a PoC
environment, but will not be supported in a production environment as the
security risk would be too high. Configuring mobile clients and federation
will not be possible with self-signed certificates.

### Certificates without letsencrypt

If you have certificates for your Element fqdn and Synapse fqdn already,
then you can simply place the `.crt` and `.key` files in the certs directory
under the installer directory. Certificates in the certs directory must take
the form of `fqdn.cert` and `fqdn.key`.

### Self-signed certificates with mkcert

The following instructions will enable you to use a tool called mkcert to
generate self-signed certificates. Element nor Canonical ship this tool and
so these directions are provided as one example of how to get self-signed
certificates.

```bash
apt-get install wget libnss3-tools
wget
https://github.com/FiloSottile/mkcert/releases/download/v1.4.3/mkcert-v1.4.3-linux-amd64
mv mkcert-v1.4.3-linux-amd64 /usr/bin/mkcert

chmod +x /usr/bin/mkcert
```

Once you have mkcert executable, you can run:

```bash
# mkcert -install
The local CA is now installed in the system trust store! ⚡️
```

Now, you can verify the CA Root by doing:

```bash
# mkcert -CAROOT
/root/.local/share/mkcert
```

Your output may not be exactly the same, but it should be similar. Once we’ve
done this, we need to generate self-signed certificates for our hostnames. In
our example, we’ll be using `element.local` and `synapse.local`, which
are both on the same host, `192.168.122.39`:

The run for the element fqdn looks like this:

```bash
# mkcert element.local element 192.168.122.39 127.0.0.1

Created a new certificate valid for the following names
- "element.local"
- "element"
- "192.168.122.39"
- "127.0.0.1"

The certificate is at "./element.local+3.pem" and the key at
"./element.local+3-key.pem" ✅

It will expire on 1 May 2024
```

The run for the synapse fqdn looks like this:

```bash
# mkcert synapse.local synapse 192.168.122.39 127.0.0.1

Created a new certificate valid for the following names
- "synapse.local"
- "synapse"
- "192.168.122.39"
- "127.0.0.1"

The certificate is at "./synapse.local+3.pem" and the key at
"./synapse.local+3-key.pem" ✅

It will expire on 1 May 2024
```

Once you have self-signed certificates, you need to copy them into the certs
directory under the installer directory. Certificates in the certs directory
must take the form of `fqdn.crt` and `fqdn.key`.

Using our above example, these are the commands we would need to run from
the installer directory: (We ran `mkcert` in that directory as well.)

```bash
cp element.local+3.pem certs/element.local.crt
cp element.local+3-key.pem certs/element.local.key
cp synapse.local+3.pem certs/synapse.local.crt
cp synapse.local+3-key.pem certs/synapse.local.key
```

### Certificates with LetsEncrypt

Our installer also supports using LetsEncrypt to build certificates for your
host names and automatically install them into your environment. If your
hosts are internet accessible, this is the easiest method and only requires
an admin email address to provide to LetsEncrypt.

## parameters.yml

Now it is time to set `parameters.yml`. Using the example hostnames of
`element.local` and `synapse.local` (not resolvable on the internet), we
would set the following parameters first in `parameters.yml`:

```bash
domain_name: local
element_fqdn: element.local
synapse_fqdn: synapse.local
```

Next, we need to set the variables related to Postgres:

```bash
postgres_fqdn: element.local
postgres_user: element
postgres_db: element
postgres_ssl_mode: "prefer"
postgres_port: 5432
```

Now, we need to set information about the media host. By default, these are
set to `/mnt/data` for the path and a media size of 50Gi. If you need to
make changes you can, but the defaults are safe to leave in place as long
as you can fit 50Gi on `/mnt/data`.

```bash
media_host_data_path: "/mnt/data"
media_size: "50Gi"
```

The next item in the configuration is the microk8s DNS resolvers. This
defaults to using Google’s DNS. You may change this if you need to use
your company’s DNS.

```bash
microk8s_dns_resolvers: "8.8.8.8,8.8.4.4"
```

The next section pertains to certmanager. If you are using your own
certificates, please leave these items both blank, as such:

```bash
certmanager_issuer:
certmanager_admin_email:
```

If you have chosen to use letsencrypt, please specify “letsencrypt” for
the certmanager_issue and an actual email address for who should manage the
certificates for certmanager_admin_email:

```bash
certmanager_issuer: 'letsencrypt'
certmanager_admin_email: admin@mydomain.com'
```

## secrets.yml

Now we move on to configuring `secrets.yml`. You will need the following
items here:

- A Macaroon key
- Your postgres password for the user specified in parameters.yml
- A Registration Shared Secret
- A signing Key
- A Registry username and token, which will have been provided to you
by Element.

For the `macaroon` key and the `registration_shared_secret`, you may
generate them with the `pwgen` utility. If you do not have this utility,
you may install it in Ubuntu with:

```bash
apt-get install pwgen -y
```

Once you have the 'pwgen' tool, you can use it as follows:

```bash
pwgen 32 1
```

At this point, you can set the following items in `secrets.yml`:

```bash
macaroon: "insert_pwgen_output_here"
postgres_passwd: "insert_random_password_here"
registration_shared_secret: "insert_different_pwgen_output_here"
```

In order to generate the signing key, we need to run:

```bash
python3 tools/create_keys.py
```

This will create output similar to:

```bash
Signing key: ed25519 0 8uCMyhmX5X3N78tkxGYzzjtZrKN0hGAw03ue4Pa/294
Verify key: ed25519 0 m9//8YDBgKCssHDp9AHpa5umUjn/B1HJXL0TngdUiFo
```

From this, we can specify in `secrets.yml`:

```bash
signing_key: “ed25519 0 8uCMyhmX5X3N78tkxGYzzjtZrKN0hGAw03ue4Pa/294”
```

Do not forget to also set the values for `registry_username` and
`registry_token`, which will both be provided by Element.

## Extra Configuration Items

It is possible to configure anything in Synapse's
[homeserver.yaml](https://github.com/matrix-org/synapse/blob/develop/docs/sample_config.yaml)
or Element’s
[config.json](https://github.com/vector-im/element-web/blob/develop/docs/config.md).

To do so, you need to create json or yaml files in an `extra-config`
directory under the installer directory. These files will be merged to the
target configuration file.

Samples are available in `config-sample` under the installer directory.

To configure synapse:

- Create a directory `extra-config/synapse` at the root of the installer
directory : `mkdir -p extra-config/synapse`
- Copy the configurations extensions you want to setup from
`config-sample/synapse` to `extra-config/synapse`.
- Edit the values in the file accordingly to your configuration

To configure element:

- Create a directory `extra-config/element` at the root of the installer
directory : `mkdir -p extra-config/element`
- Copy the configurations extensions you want to setup from
`config-sample/element` to `extra-config/element`.
- Edit the values in the file accordingly to your configuration

For specifics on configuring permalinks for Element, please see [Configuring
Permalinks](./permalinks.md).

For specifics on setting up SSO/SAML, please see [Setting up
SSO/SAML](./saml.md).

For specifics on setting up Group Sync, please see [Setting up Group
Sync](./groupsync.md).

## Installation

Let’s review! Have you considered:

- [Hostnames/DNS](install-poc.md#hostnamesdns)
- [Operating System](install-poc.md#operating-system) (We’ve tested on
Ubuntu Server 20.04)
- [Postgresql Database](install-poc.md#postgresql-database)
- [SSL Certificates](install-poc.md#ssl-certificates)
- [Extra configuration items](install-poc.md#extra-configuration-items)

Once you have the above sections taken care of and your `parameters.yml`
and `secrets.yml` files are in order, you are ready to begin the actual
installation.

From the installer directory, run:

```bash
bash install.sh
```

The first run should go for a little while and then exit, instructing you
to log out and back in.

Please log out and back in and re-run the installer from the installer
directory again:

```bash
bash install.sh
```

Once this has finished, you can run:

```bash
kubectl get pods -n element-onprem
```

And you should get similar output to:

```bash
NAME                                       READY   STATUS    RESTARTS   AGE
app-element-web-5c8c6d8765-2hwvm           1/1     Running   0          52m
server-well-known-59f87956d8-f5j2h         1/1     Running   0          52m
instance-synapse-haproxy-f7c597bdb-tz28h   1/1     Running   0          52m
instance-synapse-main-0                    1/1     Running   0          52m
```

At this time, you should also be able to browse to: `https://fqdn` and create
a test account with Element on your new homeserver. Using our example values,
I am able to go to `https://element.local/` and register an account, sign
in and begin testing the proof of concept!
