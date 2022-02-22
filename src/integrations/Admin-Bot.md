# Admin Bot

Matrix brings lots of possibilities for collaboration through federation of different homeservers.
This calls for moderation tools which consider the decentral power levels of Matrix rooms.

**Admin Bot is only available on homeservers with the Element Enterprise Cloud plan.**

Admin Bot is a service account which works in addition to the EMS Server Admin UI and [Synapse Admin API](https://matrix-org.github.io/synapse/latest/usage/administration/admin_api/).
Most administrative tasks in a Matrix room require a local account with the power level "Administrator" (100) to be a room member.

The Admin Bot extension ensures this by inviting and promoting the account `adminbot` in every Matrix room created on your server.
This way you can moderate content in these rooms, invite and promote room members and kick or ban unwanted members.

## Use case examples

- All active administrators in a room depromoted themselves. Use Admin Bot to regain control of this room.
- Someone reported a Code of Conduct violation in a room without active moderators. Use Admin Bot to redact the messages and kick or ban the offender.

## Good to know

- Admin Bot joins all rooms and spaces created by your users.
- Admin Bot also joins Direct Message rooms created by your users.
- The use of Admin Bot is visible to your users. The service account cannot be hidden. In Direct Message rooms it will not appear in the room title but is visible in the room member list.
- Admin Bot does not join rooms created by users on others servers. You can still manually invite Admin Bot and promote them to be a room admin.
- The user account `adminbot` will be used. The full Matrix ID will be something like `@adminbot:element.io`.
- Admin Bot is able to read encrypted messages to allow you to moderate messages.

## Setup

1. Go to the [Integrations tab on the EMS homeserver page](https://ems.element.io/user/hosting#/integrations).
1. If you have more than one homesever, select the homeserver to add Admin Bot to.
1. In the section Extensions, click on `Admin Bot`. If this is not visible, check that the homeserver is using the Element Enterprise Cloud plan.
1. Click on `Set Up Integration` and confirm the pricing in a modal.

![](/images/integrations/Admin-Bot/setup-button.png)

## Usage

Admin Bot improves your ability to use the `Server Admin` tab on the EMS homeserver page and Synapse Admin API by having a local admin in every room.

![](/images/integrations/Admin-Bot/logged-into-element.png)

Furthermore, you can use Element Web to log into the `adminbot` account:

1. Go to the [Integrations tab on the EMS homeserver page](https://ems.element.io/user/hosting#/integrations).
1. If you have more than one homeserver, select the one you want to administrate.
1. In the section Extensions, click on `Admin Bot`. If this is not visible, check that the homeserver is using the Element Enterprise Cloud plan.
1. If this is the first time you log in using this browser, click `Secure Backup Phrase (click to view)` and copy the phrase to your clipboard.  
![](/images/integrations/Admin-Bot/secure-backup-phrase.png)
1. Click on `Log in as Admin bot`. You will need to enter the Secure Backup Phrase on first login with a new browser in order to access Secure Storage and encrypted messages.

## Removal

Removing the integration will not cause the user `adminbot` to leave rooms.
This is a separate step to make mistakes easier to recover from.
If the integration was accidentally deactivated and Admin Bot left rooms as the last local Administrator in that room, such rooms can no longer be moderated by anyone and need to be abandoned. Those room also couldn't be rejoined by Admin Bot.

You can deactivate the `adminbot` account using the EMS Admin GUI or Synapse Admin API, if you want it to leave all rooms.
