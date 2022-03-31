# Introduction

Welcome to the Element Enterprise Installer Documentation! Element Enterprise
Installer enables you to install Element Enterprise for two purposes:

- Proof of concept on a single node. For this, we use microk8s on Ubuntu or Eneterprise Linux.
- Production on multiple nodes. For this, we will install into an existing
kubernetes environment.

The Element Enterprise Installer supports the following features:

- Synapse Homeserver - A synapse homeserver configured to Element's best
practices will be installed.
- Element Web - An instance of Element Web will be configured to Element's
best practices and immediately available post installation.
- SSO / SAML - The installer is able to configure using your LDAP/AD based
infrastructure over SSO/SAML technologies for login.
- Group Sync - The installer is able to configure group sync v1, which enables
the application of ACLs from your LDAP/AD architecture to Spaces and Rooms in
the Element ecosystem. Please note that the initial version we are providing
only supports a single node, non-federated configuration.
- Dimension Integration Manager - The installer is able to configure the
dimension integration manager, which allows you to serve integrations
on-premise.
- Gitlab, Github, and Jira Integrations - The installer is able to configure
hookshot, which provides integrations with Gitlab, Github, and Jira.
