# Frequently Asked Questions

## Element General

### Can spaces be deleted?

Spaces are rooms and can be deleted in the same way using the [delete room](https://matrix-org.github.io/synapse/latest/admin_api/rooms.html#delete-room-api) Synapse Admin API.

### How do I link to my space outside of my Element Web?

Spaces are just rooms, so you can link to a space the same way you would a room. For example <https://matrix.to/#/#community:matrix.org>.

### What is the permissions required to start a video call?

In a room with more than two members, voice and video calls are done using the Jitsi integration. Users need "Modify widgets" permissions to add the Jitsi widget to the room and initiate a call.

Once the call is initiated, anyone in the room can join.

### What is the preferred resolution for room and space icons?

Room and space icons can be shown in a full screen lightbox, so the resolution should be high. The homeserver will create a smaller thumbnail that is displayed when viewing rooms and spaces normally.

## Matrix General

### What is an Identity Server and how does it work?

The best response to 'What is an Identity Server' is detailed in section 2. of the vector.im Identity Server privacy policy, available here: [https://element.io/is-privacy-notice](https://element.io/is-privacy-notice)

New Vector runs two identity servers, one at matrix.org, and another at vector.im. These servers run in a closed federation - this means that if you add (or remove) your data from one, it is added to (or removed from) the other automatically, too.

The behavior and role of Identity Servers is changing. Historically, Identity Servers provided three sets of functionality:

1. Letting users publish their third party identifiers (email/telephone number) to a directory to allow other Matrix users to discover them.
1. Letting users send invites to a Matrix chat room to an email address instead of a Matrix ID.
1. Letting homeservers send emails/SMS text messages to verify that they belong to a given Matrix user so that user can log in to the homeserver using a third-party identifier instead of a Matrix ID.

Identity Servers continue to provide the functionality described in 1. The features described in 2. and 3. are now provided by the homeserver instead, and will be deprecated and phased out of the Identity Server in the future.

For a period in 2019, while privacy functionality was being enhanced on vector.im and matrix.org, these Identity Servers were restricted to only provide services for users on New Vector homeservers. Once privacy improvements landed, this restriction was lifted.

## Element Matrix Services

### Account Management

#### Please discontinue my account

It is best if EMS customers delete their host or account themselves. Here's how:

Delete the host from the  host management page at [https://ems.element.io/user/hosting](https://ems.element.io/user/hosting) by clicking on the `Delete host` button (and confirming deletion in the resultant dialog). This will delete the host and cancel all associated subscriptions.

Or delete the EMS account entirely.  This is done from the  user account page [https://ems.element.io/user/account](https://ems.element.io/user/account), by clicking on the `Delete account` button and confirming. This will delete all hosts and subscriptions before removing the user's account.

### Integrations

#### Bots? What's the reason for using them?

Bots allow you to get information and perform actions inline with your chat, there are a bunch that can be found in [https://matrix.org/docs/projects/bots/](https://matrix.org/docs/projects/bots/).

#### Can I host my own Telegram bridge?

Unfortunately you are not currently able to host your own bridges to work with your EMS hosted homeserver. As of December 2020, we have added a Telegram bridge to EMS. See our blog post:  [EMS brings more interoperability to messaging](https://element.io/blog/telegram-bridging/)

If you have federation enabled for your homeserver, you are also able to bridge into publicly accessible rooms, for example using [https://t2bot.io/](https://t2bot.io/) or integrations available on public homeservers such as matrix.org.

#### Does DMs count towards the 20 channel limit for the paid Slack bridge?

Yes, but we're currently in the process of reviewing the bridging pricing models and soon we'll likely be offering Slack (as well as all of our other bridges) on a usage basis, rather than on a room / workspace capped basis.

When this launches, existing customers will be able to stay on their existing plan, or choose to move to the new model.

#### How do I add a GitHub integration?

To create a GitHub integration in a room, click on the `i` icon at the top right, accept the privacy policy, click `Add widgets, bridges & bots`, click `Add integrations` and select GitHub from the Bots list. Log in to GitHub when prompted and select the repositories and functions you want.

Note that your server needs to have federation enabled for integrations to work.

#### How do I add RSS integration to my Matrix server?

To create RSS integration in a room,  click on the `i` icon at the top right, accept the privacy policy, click `Add widgets, bridges & bots`, click `Add integrations`and select RSS Bot from the Bots list. Enter the RSS URL and click `Subscribe`.

Note that your server needs to have federation enabled for integrations to work.

#### How do I bridge to Libera Chat IRC rooms with more than 100 users?

Please talk to your account manager, or open a support ticket by emailing [support@matrix.org](mailto:support@matrix.org). Requests will be considered by the bridge team on a case-by-case basis.

#### What is the difference between the free and paid Slack bridge?

They're mostly the same. The big difference is that the free one doesn't bridge DMs / puppet your account. See also [Does DMs count towards the 20 channel limit for the paid Slack bridge?](#does-dms-count-towards-the-20-channel-limit-for-the-paid-slack-bridge)

#### With Jitsi video conferencing, how is the data being transferred?

Jitsi conferencing data goes directly from the browser to the Jitsi server, it does not use the Matrix protocol. If you add a Jitsi widget to a room, that widget will be stored in the room state as Matrix events, but the Jitsi communication itself is from the client to the Jitsi server used.

### Miscellaneous

#### Are all my messages stored on my homeserver?

Messages are stored on your server. However, if you are communicating with users registered on other servers, then relevant messages / events will also exist on their server.

#### Is there a maximum file size per upload?

The file upload limit for EMS hosts is currently set at 100MB.

#### How do I send "System Alerts" or post from the @server user?

The web console has a form to do this. "System status messages" - You can use this form to send messages to all users of your server. For example, this could be used to send "messages of the day", or important policy updates etc.

#### What are exactly the benefits of paying for an EMS homeserver?

EMS aims to take the hassle out of having to host and manage your own Matrix stack. There is a significant technical overhead (in terms of technical knowledge required) as well as ongoing time and resources to ensure that your server continues running and is kept up to date with all of the latest security updates etc. With EMS you don't have to worry about that as it is all taken care of for you, at the touch of a button.

We also provide a (growing) suite of proprietary host administration tools in the form of the EMS Synapse admin dashboard to help give you better insight and control of your server.

#### What are the limitations in terms of storage?

For storage, we’ve shied away from hard limits, and instead adopted a fair use policy. If you are using the server for business conversations and sharing a few images as part of your discussions you will never have problems, if you are sharing thousands of images daily per user then you will hit a limit.

### Pricing & Payments

#### Do you offer other payment options like IBAN/SEPA?

Currently, we only accept Credit or Debit / bank account cards as payment. "Debit cards" should work with any normal bank account.

#### How do I update my payment info?

To update your payment info, go to [https://ems.element.io/user/billing](https://ems.element.io/user/billing). From here you can update your payment details.

#### If I join a room with a lot of external users from my homeserver will I be charged for those?

No, you are only ever charged for users that are registered on your server, who have been active for more than two days in a month. These users make up your Monthly Active User (MAU) total. Users that are registered on other servers (that you communicate with over federation), guest users and users who are only briefly active on your server are not counted.

### Server Configuration & Management

#### Are custom appservices supported?

Upload of custom (yaml) registration files for appservices is not currently supported for EMS hosts.

We are actively working on improving bridging support for EMS hosts and hope that this will be something that you see substantial improvement in over the coming months.

#### Are you able to use a custom domain like: "matrix.example.com"?

Yes, absolutely! However you need to set this at host creation time as the homeserver name is "baked in" to all of the events that the homeserver creates.

You can set both the homeserver name, e.g. `example.com` (so your Matrix user IDs would be of the form `@foo:example.com`) and your (Element) client address, which might be something like `webchat.example.com`. However, in order to prove that you own the domain in question you will need to place some JSON / text into two `well-known` files on the web server for your domain. You will be guided through this process when setting up the custom domain for your server in the setup wizard.

#### Can I add all my users to a Space by default?

Yes, this is available for Gold and Enterprise customers. Please talk to your Account Manager or open a support ticket.

#### Can I change the default room notification level for my users?

This is currently not possible unfortunately.

#### Can I customize the Element web login page?

Yes, you can modify the look and feel of your client to suit you.

Please see our blog article on custom branding for your Element instance, here [https://element.io/blog/custom-branding/](https://element.io/blog/custom-branding/) and [Client Look and Feel](Client-Look-and-Feel.md), for more details.

You will be able to enter the customization preferences from the managed host page of your EMS account - [https://ems.element.io/user/hosting](https://ems.element.io/user/hosting).

#### Can I use a subdomain instead of the root domain with my EMS server?

Yes. However this is not recommended. For the same reason your email address probably is not `someone@email.example.com`, you probably don't want your Matrix IDs to be `@someone:matrix.example.com`.

Please see <https://matrix-org.github.io/synapse/latest/setup/installation.html#choosing-your-server-name> for additional details on your server name.

#### Can I use EMS hosted well-knowns with the root of my domain?

Yes you can, however there are some limitations:

- You will not be able to serve a website on the domain.
- Using a CNAME DNS record on the root of a domain is not compliant with the DNS Specification (per [Domain Name System RFC 1034, paragraph 3.6.2](https://joinup.ec.europa.eu/collection/ict-standards-procurement/solution/dns-rfc-1034-rfc-1035-domain-name-system/about) specifically). But you may still be able to do this successfully if:
  - Your DNS provider allows setting a CNAME record on the root of your domain. Be aware that certain other DNS records for your domain will not be returned properly, including SOA, NS, and TXT records. (Such as SPF, DMARC, and DKIM which is used for securing email)
  - Your DNS provider offers a DNS Spec compliant workaround for using CNAME on root, this include ALIAS records and CloudFlare CNAME Flattening (note that proxy must be turned off).
    - When using this, please note that the EMS Control Panel will not recognize your DNS record as correct, but your EMS server will function properly and without limitations (beyond the yellow warning in the EMS Control Panel)
- You can use an A record instead of a CNAME record. To do this, finish setting up your EMS server without adding the DNS record when asked. After setup is complete, check the IP address of your EMS server, for example with `$ dig example.ems.host` in the Mac/Linux terminal or `Resolve-DnsName -Name example.ems.host` in Windows PowerShell, then add an A record on the root of your domain pointing to this IP address.
  - **Please note that this is not officially supported from EMS and we reserve the rights to change the IP address of your EMS server without notice.**
  - You will see the same error in the EMS Control Panel as above, but your EMS server will work with this configuration.
- Using a subdomain for your EMS server. By doing this, you will not see any of the limitations and do not need any of the workarounds listed above. However please consider [Can I use a subdomain instead of the root domain with my EMS server?](#can-i-use-a-subdomain-instead-of-the-root-domain-with-my-ems-server)

#### CNAME and .well-known?

- You need to create a CNAME record with your DNS provider. This need to be:  
    **chat.example.com. CNAME yourEMShost.element.io.**  
(please note that proxy must be turned off if you are using CloudFlare)

- You need to set up a website on your domain e.g. `example.com`.
- This website needs HTTPS enabled.

- You need to create two files on the web server. These need to be located at exactly:  
  - <https://example.com/.well-known/matrix/client>  
  - <https://example.com/.well-known/matrix/server>  

- You need to enable the CORS header `Access-Control-Allow-Origin: *` on the web server for the client file. See [https://enable-cors.org/](https://enable-cors.org/) for instructions on how to do this.

The client file needs to contain:

```json
{
    "m.homeserver": {
        "base_url": "https://yourEMShost.ems.host"
    },
    "m.identity_server": {
        "base_url": "https://vector.im"
    }
}
```

The server file needs to contain:

```json
{
    "m.server": "yourEMShost.ems.host:443"
}
```

#### CNAME doesn't work with CloudFlare?

You can use the CNAME with CloudFlare, but you have to change Proxy status to DNS only.

#### Could you expand on "over federation"?

If you have federation turned on in your server configuration, you are able to communicate with users registered on other servers (e.g. matrix.org).

You are only ever charged for users that are registered on your server, who have been active for more than two days in a month. These users make up your Monthly Active User (MAU) total. Users that are registered on other servers (that you communicate with over federation), guest users and users who are only briefly active on your server are not counted.

#### DNS not resolving

This problem is most likely caused by a delay in DNS replication downstream of your DNS servers.

#### How can I manage my #general room?

You can gain admin permissions in this room by calling [this](https://matrix-org.github.io/synapse/latest/admin_api/rooms.html#make-room-admin-api) Synapse Admin API or by contacting EMS Support on <https://ems.element.io/support>.

Gold and Enterprise customers can also request changes the list of default rooms all their users are automatically added to.

#### How do I change the name/brand of the Element Web client?

You can rename the Element client from `Element` to for example `Company Chat` with the `Client name` field on <https://ems.element.io/user/hosting#/hosts>. See [Client Look and Feel](Client-Look-and-Feel.md) for additional details.

#### How do I change the server's custom domain?

You can only set a custom domain name for a server at setup time. This is because the domain name of the server is "baked-in" to all of the events that are generated by the server.

So, you would need to deprovision an existing server and create a new one, selecting your custom DNS preferences from the advanced settings section of host setup configuration if you wished to change existing host DNS.

#### How do I delete users when administering the server?

You can deactivate users from the admin dashboard for your host, at [https://ems.element.io/user/hosting](https://ems.element.io/user/hosting).

Select the `Server Admin` tab and then the `User Info` sub-tab. From here you can search for the relevant user and hit the `Deactivate account` button.

#### How do I enable the public room directory?

The public room directory is enabled on your EMS server if both `Federation` and `Guest users` is enabled.

#### How do I migrate from EMS to self-hosted if I choose to do so in the future?

Currently the process for migrating away is manual. However, we hope to have an automated, self-serve system in the not too distant future. For the time being, if you wish to migrate away, please simply email ems-support@element.io (while your EMS server is still up and running) and ask for a snapshot of your Synapse database. We will then generate a snapshot for you and generate a link for you to download the data. You can then use this to restore the database / Synapse instance on your own infrastructure.

#### I deleted my host, now my server name is taken and I cannot rebuild

This is actually part of a security measure - We generally prevent hosts from returning to the pool after they were initially claimed in order to prevent people from attempting to imitate old servers / users. Contact support from [https://ems.element.io/support](https://ems.element.io/support) while signed in to get the hostname released.

#### Online users are displayed as offline?

Unfortunately, we are not able to offer user presence as a feature at the moment. This is due to potential performance impact and excess resource usage on hosts when this feature is enabled. The Synapse team is aware of this and it is on their road map to address. However, we do not currently have a timeline for when it will be available again.

#### What does "Include bridged accounts" on the user management page mean?

When you bridge to external services, external users get an "appservice user" on your EMS server. If you have any bridges, and you check this checkbox, users from across your bridges will also be shown.
