# Telegram Bridge

This guide explains how to use the Telegram bridge from the EMS Integration Manager to integrate your Telegram chats with your EMS server.

It requires your EMS server to have federation on.

The following instructions are done with the  Element Desktop on the Element side and on Element iOS for the Telegram side. Element Android should be almost identical to Element Web.

## Purchase the Telegram integration

1. Open the EMS control panel at: [https://ems.element.io/user/hosting](https://ems.element.io/user/hosting)  
Click the `Integrations` tab  and if you have more than one server, select the server you wish to add the Telegram integration to.  
![](/images/click-integration-tab-ems-user-hosting.png)  

1. Click on `Telegram Bridge` in the list of available Bridges. 
![](/images/bridge-integration-list.png)  

1. Enter the maximum number of users in `Maximum Telegram users`.  
Please note:  **this is the maximum number of Telegram users who actually send messages over the bridge each month. You are only billed for the number of Telegram users who are active. Once you exceed the maximum, then the bridge will be disabled until you increase the maximum.**

Once you have entered `Maximum Telegram users`, click `Purchase` (remember you can always go back to this step and increase the maximum number of Telegram users if you need more in the future).

1. A dialogue will remind you of the price per user and ask if you wish to proceed. Click `Purchase` if you wish to proceed with the Telegram Integration. 
![](/images/integrations/Telegram-Bridge/confirm-payment.png)  

1. You will have to wait a few minutes while your host is reprovisioned.
Once reprovisioning is finished, you are able to bridge Telegram to your EMS server using your Element client.

## Bridge Telegram to your Element account

1. Once the bridge is running, open your Element app. Click on the `+` next to `People`. 
![](/images/start-chat.png)

1. Create a Direct Message conversation by typing `@telegram:example.ems.host` (replace the domain with the one of your homeserver). Then click `Go`.

1. Wait for the bridge account to join your room.

1. Open Telegram on your mobile device (iOS or Android) and tap on ≡, go to `Settings`, and then `Devices`, and then `Scan QR Code` to start the Telegram QR code scanner. You will use this QR code scanner to scan a QR code displayed by your Element client in the next step.

1. From your Element client, send a `login-qr` message to the bot to connect to your Telegram account.

1. A QR code will be displayed. Quickly scan the QR code with Telegram on your mobile device.

1. On your Element client, you will see `Successfully logged in as <username>`.

## Sending a message to an Telegram User

To send a message to a Telegram user, you must first be connected to the bridge (see above).

1. On your Element client, open the "Telegram bridge bot" room.

1. Say `pm` followed by the phone number or username. The phone number must exist in your Telegram contacts.

1. You will be invited to a DM with that user, and can send messages to them.

## Bridging Matrix users without a Telegram acccount

By default, a Matrix user will have to connect their Telegram account for their messages to be bridged to Telegram. If you provide a bot token, we will use this bot to relay the messages of any Matrix users to Telegram.

Follow these steps to register a bot account with Telegram.

1. With your Telegram account, message [@BotFather](https://www.t.me/BotFather).

1. Create a new bot by sending the message `/newbot` to BotFather.

1. Wait for BotFather to provide you a bot token.
