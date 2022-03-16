# Configuring Group Sync

## What is Group Sync?

Group Sync allows you to use the ACLs from your identity infrastructure
in order to set up permissions on Spaces and Rooms in the Element
Ecosystem. Please note that the initial version we are providing
only supports a single node, non-federated configuration.

## General settings

- Copy sample file from `config-sample/groupsync/gsync.yml` to
 `extra-config/groupsync`
- Edit the file with the following values :
  - `ems_bridges_registry_username`: `ems bridges registry token name`
  - `ems_bridges_registry_password`: `ems bridges registry token password`
  - `group_power_levels` : A list of groups that'll determine people's
    Matrix power levels. This affects only the space that the Group belongs
    to – doesn't leak up or down. For MSGraph source, groups should be
    identified by their ids. On LDAP, they should be identified by their names.
  - `provisioner.dn_default_prefix`: Display names starting with this
    prefix will get corrected according to the names we found for their
    users in LDAP. Optional. Useful if you're using an OIDC provider that
    doesn't give you users' display names.
  - `provisioner.default_rooms` : Optional. A list of rooms that'll get
    automatically created in in managed space. The ID is required to enable
    GPS to track whether they were already created or not. You can change it,
    but it'll cause new rooms to be generated.
  - `provisioner.whitelisted_users` : Optional. A list of userid patterns
    that will not get kicked from rooms even if they don't belong to them
    according to LDAP. This is useful for things like the auditbot. Patterns
    listed here will be wrapped in ^ and $ before matching.

## Configuring the source

### LDAP Servers

- You should create a ldap account with read access to the OUs containing
 the users
- This account should use password authentication
- To use LDAP source, copy the file  `config-sample/groupsync/ldap.yml` to
`extra-config/groupsync` the following variables :
  - `ldap_check_interval_seconds`: The interval check in seconds
  - `ldap_uri`: The LDAP Uri to connect to the ldap server
  - `ldap_base`: The LDAP base used to build the space hierarchy. This OU
    will become the root space. Every OU below this base will be a child-space.
  - `ldap_bind_dn`: The user bind dn to use to read the space hierarchy.
  - `ldap_bind_password`: The user password
  - `ldap_attrs_uid`: The attribute to use to map to users mxids
  - `ldap_attrs_name`: The attribute to use to map to spaces names
- Restart the install script

### MS Graph (Azure AD)

- You need to create an `App registration`. You'll need the `Tenant ID` of
 the organization, the `Application (client ID)` and a secret generated from
 `Certificates & secrets` on the app.
- For the bridge to be able to operate correctly, navigate to API permissions
 and ensure it has access to Group.Read.All, GroupMember.Read.All and
 User.Read.All
- Remember to grant the admin consent for those.

- To use MSGraph source, copy the file  `config-sample/groupsync/msgraph.yml`
to `extra-config/groupsync` the following variables :
  - `msgraph_tenant_id`: This is the "Tenant ID" from your Azure Active
   Directory Overview
  - `msgraph_client_id`: Register your app in "App registrations". This
   will be its "Application (client) ID"
  - `msgraph_client_secret` : Go to "Certificates & secrets", and click
   on "New client secret". This will be the "Value" of the created secret
   (not the "Secret ID").

- Restart the install script
