# Admin Bot

Matrix brings lots of possibilities for collaboration through federation of different homeservers.
This calls for moderation tools which consider the decentral power levels of Matrix rooms.

**Admin Bot is only available on homeservers with the Element Enterprise Cloud plan.**

Admin Bot is an administration tool which works in addition to the EMS Server Admin UI and [Synapse Admin API](https://matrix-org.github.io/synapse/latest/usage/administration/admin_api/).
For most administrative tasks in a Matrix room you're required to have local account in the room with the power level "Administrator" (100).

The Admin Bot extension ensures this by inviting and promoting the account `adminbot` in every Matrix room which is created on your server.
This ensures that you can moderate content in these rooms, invite and promote room members and kick or ban unwanted members.

## Use case examples
* All active administrators in a room depromoted themselves. Use Admin Bot to regain control of this room.
* Someone reported a Code of Conduct violation in a room without active moderators. Use Admin Bot to kick or ban the offender.

## Good to know
* Admin Bot joins all rooms and spaces created by your users.
* Admin Bot also joins Direct Message rooms created by your users.
* The use of Admin Bot is visible to your users. The account cannot be hidden. In Direct Message rooms it will not appear in the room title but is visible in the room member list.
* Admin Bot does not join rooms created by users on others servers. You can still manually invite Admin Bot and promote them to be a room admin.
* The user account `adminbot` will be used. The full Matrix ID will be something like `@adminbot:element.io`.
* Admin Bot is able to read encrypted messages to allow you to moderate message content.

## Setup

1. Go to the [Integrations tab on the EMS homeserver page](https://ems.element.io/user/hosting#/integrations).
2. Select the homeserver to add Admin Bot to.
3. In the section Extensions, click on `Admin Bot`. If this is not visible, check that the homeserver is using the Element Enterprise Cloud plan.
4. Click on `Set Up Integration` and confirm the pricing in a modal.

## Usage

Admin Bot improves your ability to use the `Server Admin` tab on the EMS homeserver page and Synapse Admin API by having a local admin in every room.

Furthermore, you can use Element Web to log into the `adminbot` account:

1. Go to the [Integrations tab on the EMS homeserver page](https://ems.element.io/user/hosting#/integrations).
2. Select the homeserver to add Admin Bot to.
3. In the section Extensions, click on `Admin Bot`. If this is not visible, check that the homeserver is using the Element Enterprise Cloud plan.
4. Click on `Log in as Admin bot`.
