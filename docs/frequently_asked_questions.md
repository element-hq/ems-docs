# Frequently Asked Questions <!-- omit in toc -->

This article is licensed under the standard MIT license. See [[Home]] for a full copy.

<!-- TOC -->

- [Matrix General](#matrix-general)
  - [What is an Identity Server and how does it work?](#what-is-an-identity-server-and-how-does-it-work)
- [Element Matrix Services](#element-matrix-services)
  - [Account Management](#account-management)
    - [Please discontinue my account.](#please-discontinue-my-account)
  - [Integrations](#integrations)
    - [Bots? What's the reason for using them?](#bots-whats-the-reason-for-using-them)
    - [Can I host my own Telegram bridge?](#can-i-host-my-own-telegram-bridge)
    - [How do I add a GitHub integration?](#how-do-i-add-a-github-integration)
    - [How do I add RSS integration to my matrix server?](#how-do-i-add-rss-integration-to-my-matrix-server)
    - [With Jitsi video conferencing, how is the data being transferred?](#with-jitsi-video-conferencing-how-is-the-data-being-transferred)
  - [Miscellaneous](#miscellaneous)
    - [Are all my messages stored on my homeserver?](#are-all-my-messages-stored-on-my-homeserver)
    - [Is there a maximum file size per upload?](#is-there-a-maximum-file-size-per-upload)
    - [What are exactly the benefits of paying for a EMS homeserver?](#what-are-exactly-the-benefits-of-paying-for-a-ems-homeserver)
    - [What are the limitations in terms of storage?](#what-are-the-limitations-in-terms-of-storage)
  - [Pricing & Payments](#pricing--payments)
    - [Do you offer other payment options like IBAN/SEPA?](#do-you-offer-other-payment-options-like-ibansepa)
    - [How do I update my payment info?](#how-do-i-update-my-payment-info)
    - [If I join a room with a lot of external users from my homeserver will I be charged for those?](#if-i-join-a-room-with-a-lot-of-external-users-from-my-homeserver-will-i-be-charged-for-those)
  - [Server Configuration & Management](#server-configuration--management)
    - [Are you able to use a custom domain like: "matrix.example.com"?](#are-you-able-to-use-a-custom-domain-like-matrixexamplecom)
    - [Can I customize the Element web login page?](#can-i-customize-the-element-web-login-page)
    - [CNAME and .well-known?](#cname-and-well-known)
    - [CNAME doesn't work with CloudFlare?](#cname-doesnt-work-with-cloudflare)
    - [Could you expand on "over federation"?](#could-you-expand-on-over-federation)
    - [DNS not resolving](#dns-not-resolving)
    - [How do I change the servers custom domain?](#how-do-i-change-the-servers-custom-domain)
    - [How do I delete users when administering the server?](#how-do-i-delete-users-when-administering-the-server)
    - [I deleted my host, now my server name is taken and I cannot rebuild](#i-deleted-my-host-now-my-server-name-is-taken-and-i-cannot-rebuild)
    - [If I in the future want to migrate from EMS to self-hosted, how?](#if-i-in-the-future-want-to-migrate-from-ems-to-self-hosted-how)
    - [Is upload of custom yaml supported?](#is-upload-of-custom-yaml-supported)
    - [Online users are displayed as offline?](#online-users-are-displayed-as-offline)

<!-- /TOC -->

## Matrix General

### What is an Identity Server and how does it work?

The best response to 'What is an Identity Server' is detailed in section 2. of the vector.im Identity Server privacy policy, available here: [https://element.io/is-privacy-notice](https://element.io/is-privacy-notice)

New Vector runs two identity servers, one at matrix.org, and another at vector.im. These servers run in a closed federation - this means that if you add (or remove) your data from one, it is added to (or removed from) the other automatically, too.

The behavior and role of Identity Servers is changing. Historically, Identity Servers provided three sets of functionality:

1. Letting users publish their third party identifiers (email/telephone number) to a directory to allow other Matrix users to discover them
1. Letting users send invites to a Matrix chat room to an email address instead of a Matrix ID
1. Letting homeservers send emails/SMS text messages to verify that they belong to a given Matrix user so that user can log in to the homeserver using a third-party identifier instead of a Matrix ID

Identity Servers continue to provide the functionality described in 1. The features described in 2. and 3. are now provided by the homeserver instead, and will be deprecated and phased out of the Identity Server in the future.

For a period in 2019, whilst privacy functionality was being enhanced on vector.im and matrix.org, these Identity Servers were restricted to only provide services for users on New Vector homeservers. Once privacy improvements landed, this restriction was lifted.


## Element Matrix Services

### Account Management

#### Please discontinue my account.

You can request deletion of your host(s) from your host management page at [https://ems.element.io/user/hosting](https://ems.element.io/user/hosting) by clicking on the "Delete host" button (and confirming deletion in the resultant dialog). This will delete your host and cancel all associated subscriptions.

If you wish to delete your EMS account entirely, you can do so from your user account page [https://ems.element.io/user/account](https://ems.element.io/user/account), by clicking on the "delete account" button and confirming. This will delete all hosts and subscriptions before removing your user account.

### Integrations

#### Bots? What's the reason for using them?

Bots allow you to get information and perform actions inline with your chat, there are a bunch that can be found in https://matrix.org/docs/projects/bots/.

#### Can I host my own Telegram bridge?

Unfortunately you are not currently able to host your own bridges to work with your EMS hosted homeserver. However, we are actively working to add EMS bridges at the moment and hope that these will be available soon.

That said, if you have federation enabled for your homeserver you are able to bridge into publicly accessible rooms, for example using https://t2bot.io/ or integrations available on public homeservers such as matrix.org.

#### How do I add a GitHub integration?

To create a GitHub integration in a room, press the four squares in the top of a room labeled Manage Integrations, accept the privacy policy and select GitHub from the Bots list. Log in to GitHub when prompted and select the repositories and functions you want.

Note that your server needs to have federation enabled for integrations to work.

#### How do I add RSS integration to my matrix server?

To create RSS integration in a room, press the four squares in the top of a room labeled Manage Integrations, accept the privacy policy and select RSS Bot from the Bots list. Enter the RSS URL and click Subscribe.

Note that your server needs to have federation enabled for integrations to work.

#### With Jitsi video conferencing, how is the data being transferred?

Jitsi conferencing data goes directly from the browser to the Jitsi server, it does not use the Matrix protocol. If you add a Jitsi widget to a room, that widget will be stored in the room state as Matrix events, but the Jitsi communication itself is from the client to the Jitsi server used.

### Miscellaneous

#### Are all my messages stored on my homeserver?

Messages are stored on your server. However, if you are communicating with users registered on other servers, then relevant messages / events will also exist on their server.

#### Is there a maximum file size per upload?

The file upload limit for Small hosts is currently set at 100MB.

#### What are exactly the benefits of paying for a EMS homeserver?

EMS aims to take the hassle out of having to host and manage your own Matrix stack. There is a significant technical overhead (in terms of technical knowledge required) as well as ongoing time and resources to ensure that your server continues running and is kept up to date with all of the latest security updates etc. with EMS you don't have to worry about that as it is all taken care of for you, at the touch of a button.

We also provide a (growing) suite of proprietary host administration tools in the form of the EMS Synapse admin dashboard to help give you better insight and control of your server.

#### What are the limitations in terms of storage?

For storage, we’ve shied away from hard limits, and instead adopted a fair use policy. If you are using the server for business conversations and sharing a few images as part of your discussions you will never have problems, if you are sharing thousands of images daily per user then you will hit a limit. 

### Pricing & Payments

#### Do you offer other payment options like IBAN/SEPA?

At present we only accept Credit or Debit / bank account cards as payment. "Debit cards" should work with any normal bank account.

#### How do I update my payment info?

To update your payment info, go to [https://ems.element.io/user/billing](https://ems.element.io/user/billing). From here you can update your payment details.

#### If I join a room with a lot of external users from my homeserver will I be charged for those?

No, you are only ever charged for users that are registered on your server, who have been active for more than two days in a month. These users make up your Monthly Active User (MAU) total. Users that are registered on other servers (that you communicate with over federation), guest users and users who are only briefly active on your server are not counted.

### Server Configuration & Management

#### Are you able to use a custom domain like: "matrix.example.com"?

Yes, absolutely! However you need to set this at host creation time as the homeserver name is "baked in" to all of the events that the homeserver creates.

You can set both the homeserver name, e.g. "example.com" (so your Matrix user IDs would be of the form "@foo:example.com") and your (Element) client address, which might be something like "webchat.example.com". However, in order to prove that you own the domain in question you will need to place some JSON / text, .well-known files on the web server for your domain. You will be guided through this process when setting up the custom domain for your server in the setup wizard.

#### Can I customize the Element web login page?

Yes, you can modify the look and feel of your client to suit you.

Please see our blog article on custom branding for your riot instance, here [https://element.io/blog/custom-branding/](https://element.io/blog/custom-branding/), for more details.

You will be able to enter the customization preferences from the managed host page of your EMS account - [https://ems.element.io/user/hosting](https://ems.element.io/user/hosting).

#### CNAME and .well-known?

* You need to create a CNAME record with your DNS provider. This need to be:  
    **chat.example.com. CNAME yourEMShost.element.io.**  
(please note that proxy must be turned off if you are using CloudFlare)


* You need to set up a website on your domain example.com.
* This website needs HTTPS enabled.


* You need to create two files on the web server. These need to be located at exactly:  
  - https://example.com/.well-known/matrix/client  
  - https://example.com/.well-known/matrix/server  


* You need to enable the CORS header `Access-Control-Allow-Origin: *` on the web server for the client file. See [https://enable-cors.org/](https://enable-cors.org/) for instructions on how to do this.

The client file need to contain:
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

The server file need to contain:
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

This problem was most likely caused by a delay in DNS replication downstream of your DNS servers. Everything seems to be working from my end now. Is everything working as expected for you?

#### How do I change the servers custom domain?

You can only set a custom domain name for a server at setup time. This is because the domain name of the server is "baked-in" to all of the events that are generated by the server.

So, you would need to deprovision an existing server and create a new one, selecting your custom DNS preferences from the advanced settings section of host setup configuration if you wished to change existing host DNS.

#### How do I delete users when administering the server?

You can deactivate users from the admin dashboard for your host, at [https://ems.element.io/user/hosting](https://ems.element.io/user/hosting).

Select the "Server Admin" tab and then the "User Info." sub-tab. From here you can search for the relevant user and hit the "Deactivate account button".

#### I deleted my host, now my server name is taken and I cannot rebuild

This is actually part of a security measure - We generally prevent hosts from returning to the pool after they were initially claimed in order to prevent people from attempting to imitate old servers / users. Contact support from [https://ems.element.io/support](https://ems.element.io/support) while signed in to get the hostname released.

#### If I in the future want to migrate from EMS to self-hosted, how?

Currently the process for migrating away is manual. However, we hope to have an automated, self-serve system in the not too distant future. For the time being, if you wish to migrate away, please simply email ems-support@element.io (while your EMS server is still up and running) and ask for a snapshot of your Synapse database. We will then generate a snapshot for you and generate a link for you to download the data. You can then use this to restore the database / Synapse instance on your own infrastructure.

#### Is upload of custom yaml supported?

Upload of custom (yaml) config is not currently supported for EMS hosts.

We are actively working on improving bridging support for EMS hosts and hope that this will be something that you see substantial improvement in over the coming months.

#### Online users are displayed as offline?


This is actually intended. User presence can be quite complex and resource intensive to calculate (especially for larger rooms). For this reason, user presence is disabled by default for smaller instances.

You can re-enable it from your host management dashboard in EMS [https://ems.element.io/user/hosting](https://ems.element.io/user/hosting). However, please be aware that this may have a negative impact on your server performance, especially if you are joining larger rooms, so please try it and see how it works for you.

Note that you will not be able to see presence for users of other homeservers with presence disabled (matrix.org) for example.

