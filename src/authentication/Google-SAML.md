# Authentication via Google SAML

Note, other SAML providers may also work with EMS. Contact [EMS support](https://ems.element.io/support) to discuss your options.

## Setup

To enable authentication with Google SAML, the following needs to be done:

- Go to your Google apps admin panel: <https://admin.google.com/ac/apps/unified>
- Add a new application by clicking `Add app` and choosing `Add custom SAML app`.
- Choose a name for the application (can be anything). Click next.
- Choose option 1 and download the metadata XML. Click next.
- Add some values, replacing the `homeserver` in `https://homeserver.ems.host` with whatever the hostname will be chosen in EMS. Note, this is the EMS hostname, not the custom server domain name.
  - ACS URL: `https://homeserver.ems.host/_synapse/client/saml2/authn_response`
  - Entity ID: `https://homeserver.ems.host/_synapse/client/saml2/metadata.xml`
  - Signed response: yes
  - Click next
- Click add new mapping 3 times, adding the following:
  1. Application attribute: `email`
     - Category: Basic Information
     - Field: Primary Email
  1. Application attribute: `firstName`
     - Category: Basic Information
     - Field: First Name
  1. Application attribute: `lastName`
     - Category: Basic Information
     - Field: Last Name
- Click `Finish` and then `OK`.
- In the settings for the app, turn on for everyone.

## Update metadata

When the certificate expires (by default after 5 years) a new metadata file is required. The file can be downloaded from Google:

- Go to your Google apps admin panel: <https://admin.google.com/ac/apps/unified>
- Click on your app for Element.
- Click `Download metadata` in the sidebar.
- Click `Download metadata` in the modal.
- Store the metadata XML on your computer to upload it to EMS.

## Upload metadata to EMS

The previously downloaded metadata XML is required by EMS to establish a secure connection to your GSuite environment.

- Go to your EMS hosts: <https://ems.element.io/user/hosting>
- Click on the tab `Integrations`.
- Select the host you wish to update.
- Under `Advanced Authentication` click on the `Google SAML` integration.
- Copy paste the contents of your downloaded metadata XML into the text field.
- Click `Purchase` or `Update` and wait for your host to apply the change.
- **Test your changes by logging into the EMS host.**
