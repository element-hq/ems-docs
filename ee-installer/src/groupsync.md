# Configuring Groupsync

## On Element Enterprise

 - In the installer root directory, Copy the sample file from `config-sample/groupsync/gsync.yml` to `extra-config/groupsync`
 - Edit the file with the following values. Note that Element will provide you with the ems_bridges_registry_token_name and the ems_bridges_registry_token_password.
    - `ems_bridges_registry_username`: ems_bridges_registry_token_name
    - `ems_bridges_registry_password`: ems_bridges_registry_token_password
    - `ldap_check_interval_seconds`: The interval check in seconds
    - `ldap_uri`: The LDAP Uri to connect to the ldap server
    - `ldap_base`: The LDAP base used to build the space hierarchy. This OU will become the root space. Every OU below this base will be a child-space.
    - `ldap_bind_dn`: The user bind dn to use to read the space hierarchy.
    - `ldap_bind_password`: The user password
    - `ldap_attrs_uid`: The attribute to use to map to users mxids
    - `ldap_attrs_name`: The attribute to use to map to spaces names
    - `group_power_levels` : A list of LDAP security groups that'll determine people's Matrix power levels. This affects only the OU (Space) that the Group belongs to – doesn't leak up or down.
    - `provisioner.dn_default_prefix`: Display names starting with this prefix will get corrected according to the names we found for their users in LDAP. Optional. Useful if you're using an OIDC provider that doesn't give you users' display names.
    - `provisioner.default_rooms` : Optional. A list of rooms that'll get automatically created in in managed space. The ID is required to enable GPS to track whether they were already created or not. You can change it, but it'll cause new rooms to be generated.
    - `provisioner.whitelisted_users` : Optional. A list of userid patterns that will not get kicked from rooms even if they don't belong to them according to LDAP. This is useful for things like the auditbot. Patterns listed here will be wrapped in ^ and $ before matching.

 - Restart the install script


