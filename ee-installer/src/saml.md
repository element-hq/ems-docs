# Configuring SAML

## On Element Enterprise

- Depending on your provider, copy the sample file in the installer root
directory from `config-sample/synapse/` to `extra-config/synapse`
- Edit the file for the provider you are setting up. You have at least 3
parameters to edit :
  - The IdP metadata url
  - The name and description of your synapse server, which your provider
  would display to inform the users to which app they are logging in
- Run the installer to configure SAML provisioning

## On the provider

[Azure ADFS](./saml.html#azure-adfs)

[Keycloak](./saml.html#keycloak)

### Azure ADFS

- With an account with enough rights, go to : [Enterprise Applications
Portal](https://portal.azure.com/#blade/Microsoft_AAD_IAM/StartboardApplicationsMenuBlade/AllApps/menuId/)
- Click on  `New Application`
- Click on `Create your own application` on the top left corner
- Choose a name for it, and select `Integrate any other application you
don't find in the gallery`
- Click on "Create"
- Select `Set up single sign on`
- Select `SAML`
- `Edit` on `Basic SAML Configuration`
- In `Identifier`, add the following URL : `https://<synapse
fqdn>/_synapse/client/saml2/metadata.xml`
- Remove the default URL
- In `Reply URL`, add the following URL : `https://<synapse
fqdn>/_synapse/client/saml2/authn_response`
- Click on `Save`
- `Edit` on `Attributes & Claims`
- Remove all defaults additional claims
- Click on `Add new claim` to add the following claims. The UID will be used
as the MXID, the value here is mostly a suggestion :
  - Name: `uid`, Transformation : `ExtractMailPrefix`, Parameter 1 :
  `user.userprincipalname`
  - Name: `email`, Source attribute : `user.mail`
  - Name: `displayName`, Source attribute : `user.displayname`
- Click on `Save`
- In `Users and Groups`, add groups and users which may have access to element

### Keycloak

- In `Configure` > `Clients`, add a new client. Enter `https://<synapse
fqdn>/_synapse/client/saml2/metadata.xml` as its Client ID
- In `Mappers`, add the 3 following mappers :
  - Name: `uid` : User attribute : `username`
  - Name: `email`, User attribute : `email`
  - Name: `displayName`, Javascript mapper : `user.FirstName + " " +
  user.lastName`
