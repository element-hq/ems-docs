# Element Enterprise Installer: How to Install a Production Environment

Our Element Enterprise Production Installer can handle the installation of
Element Enterprise into your production k8s environment.

To get started with a production installation, there are several things that
need to be considered and this guide will work through them:

- [Hostnames/DNS](install-prod.md#hostnamesdns)
- [Resource Requirements](install-prod.md#resource-requirements)
- [k8s Environments](install-prod.md#k8s-environments)
- [Postgresql Database](install-prod.md#postgresql-database)
- [TURN Server](install-prod.md#turn-server)
- [SSL Certificates](install-prod.md#ssl-certificates)
- [Extra configuation items](install-prod.md#extra-configuration-items)

Once these areas have been covered, you'll be able to install a production
environment!

## Hostnames/DNS

You will need hostnames for the following pieces of infrastructure:

- Element Server
- Synapse Server
- Dimension Server
- Hookshot Server

These hostnames must resolve to the appropriate IP addresses. You must have
a proper DNS server to serve these records in a production environment.

## Resource Requirements

For running running in production, we support only the x86_64
architecture and recommend the following minimums:

- No federation: 4 vCPUs/CPUS and 16GB RAM
- Federation: 8 vCPUs/CPUS and 32GB RAM

### Unpacking the Installer

Please make sure that you unpack `element-enterprise-installer` onto a system
that has access to your k8s environment. The directory that it unpacks into
will be referenced in this document as the installer directory.

## k8s Environments

To configure your k8s environment, you need to :

- Configure a kubectl context able to connect to your kubernetes instance
- Copy `k8s.yml.sample` to `k8s.yml`. Edit `k8s.yml` with the following
 values :
- `provider_storage_class_name`: The [storage
  class](https://kubernetes.io/docs/concepts/storage/storage-classes/)
  to use when creating PVCs.
- `ingress_annotations`: The annotations to add to the ingresses created
  by the operator.
- `tls_managed_externally`: Should be true if you don't expect the operator
  to manage the certificates of your kubernetes deployment. In this case, you
  will be able to skip the **Certificates*- chapter of the `CONFIGURE.md` file.
- `operator_namespace`: The namespace to create to deploy the operator.
- `element_namespace`: The namespace to create to deploy the element
  resources.
- `k8s_auth_context`: The value of the context used in kubectl.
If you want to use
[cert-manager](https://cert-manager.io/docs/configuration/acme/) for your
tls certificates, it needs to be already installed in the targeted k8s cluster.

## Postgresql Database

The installation requires that you have a postgresql
database with a locale of C and UTF8 encoding set up. See
<https://github.com/matrix-org/synapse/blob/develop/docs/postgres.md#set-up-database>
for further details.

Please make note of the database hostname, database name, user,
and password as you will need these to begin the installation.

## TURN Server

For installations in which you desire to use video conferencing functionality,
you will need to have a TURN server installed and available for Element to use.

If you do not have an existing TURN server, we recommend installing
`coturn` outside of your k8s environment. `coturn` must open a lot of ports
to work and this can be problematic for k8s environments. Instructions on
how to do that are available here:
<https://github.com/matrix-org/synapse/blob/master/docs/turn-howto.md>

## SSL Certificates

For SSL Certificates, you have three options:

- Signed certificates from an internet recognized authority.
- LetsEncrypt
- Signed certificates from an internal to your company authority.

In the case of Internet Recognized Signed certificates or LetsEncrypt,
your hostnames must be
accessible on the internet.

### Certificates without LetsEncrypt

If you have certificates for all of the aforementioned host names,
then you can simply place the `.crt` and `.key` files in the certs directory
under the installer directory. Certificates in the certs directory must take
the form of `fqdn.cert` and `fqdn.key`.

### Certificates with LetsEncrypt

Our installer also supports using LetsEncrypt to build certificates for your
host names and automatically install them into your environment. If your
hosts are internet accessible, this is the easiest method and only requires
an admin email address to provide to LetsEncrypt.

## parameters.yml

Now it is time to set `parameters.yml`. A sample has been provided and to
get started, it is easiest to do:

```bash
cp parameters.yml.sample parameters.yml
```

Using the example hostnames of
`element.local` and `synapse.local` (not resolvable on the internet), we
would set the following parameters first in `parameters.yml`:

```bash
domain_name: local
element_fqdn: element.local
synapse_fqdn: synapse.local
```

Next, we need to set the variables related to Postgres. For your Postgres
server, please set the following:

```bash
postgres_fqdn: `Postgres Server`
postgres_user: `Postgres User`
postgres_db: `Postgres Database for Element`
```

The next item in the configuration is the microk8s DNS resolvers. By default,
the installer will use Google's publicly available DNS servers. If you have
defined your hosts on a
non-publicly available DNS server, then you should use your DNS servers
instead of the publicly available Google DNS servers. Let's assume that
your local dns servers are 192.168.122.253 and 192.168.122.252. To use those
servers, you would need to add this line:

```bash
microk8s_dns_resolvers: "192.168.122.253,192.168.122.252"
```

The next section pertains to certmanager. If you are not using LetsEncrypt,
please leave these items both blank, as such:

```bash
certmanager_issuer:
certmanager_admin_email:
```

If you have chosen to use LetsEncrypt, please specify “letsencrypt” for
the certmanager_issue and an actual email address for who should manage the
certificates for certmanager_admin_email:

```bash
certmanager_issuer: 'letsencrypt'
certmanager_admin_email: 'admin@mydomain.com'
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

To build a `secrets.yml` with the macaroon key, the registration shared secret,
the generic shared secret, and the signing key already filled in, please run:

```bash
sh build_secrets.sh
```

You will need to uncomment and set your `postgres_password` field to the
proper password for your database.

Do not forget to also set the values for `registry_username` and
`registry_token`, which will both be provided by Element.

If you have a paid docker hub account, you can specify your username
and password to avoid being throttled in the `dockerhub_username` and
`dockerhub_token` fields. This is optional.

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
- [k8s Environments](install-prod.md#k8s-environments)
- [Postgresql Database](install-poc.md#postgresql-database)
- [TURN Server](install-poc.md#turn-server)
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
