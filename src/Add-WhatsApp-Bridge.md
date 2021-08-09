# Add a WhatsApp Bridge

This article is licensed under the standard MIT license. See [Home](index.md) for a full copy.

This guide explains how to use the `WhatsApp` bridge from the EMS Integration Manager to integrate your `WhatsApp` chats with your EMS server.

It requires your EMS server to have federation on.

The following instructions are done with the  Element Desktop on the Element side and on Element iOS for the `WhatsApp` side. Element Android should be almost identical to Element Web.

## Purchase  the WhatsApp integration
1. Open the EMS control panel at: [https://ems.element.io/user/hosting](https://ems.element.io/user/hosting)  
Click the `Integrations` tab  and if you have more than one server, select the server you wish to add the `WhatsApp` integration to
![](images/click-integration-tab-ems-user-hosting.png)  

1. Choose `WhatsApp` from the list of available Bridges
![](images/wa-matrix-choose-bridge.png)  

1. Enter the maximum number of users in `Maximum WhatsApp users`  
Please note:  **this is the maximum number of WhatsApp users who actually send messages over the bridge each month. You are only billed for the number of WhatsApp users who are active. Once you exceed the maximum, then the bridge will be disabled until you increase the maximum.**  
If you enter less than `5`, you will get a warning  
![](images/wa-low-rmau-warning.png)  
If you enter a number `5` or greater in `Maximum WhatsApp users` e.g. `20`, you will not see a warning  
![](images/wa-enter-number-users-click-purchase.png)  
Once you have entered `Maximum WhatsApp users`, click `Purchase` (remember you can always go back to this step and increase the maximum number of `WhatsApp` users if you need more in the future).

1. A dialogue will remind you of the price per user and ask if you wish to proceed. Click `Purchase` if you wish to proceed with the `WhatsApp` Integration  
![](images/wa-confirm-subscription-click-purchase.png)  

1. You will have to wait a few minutes while your host is reprovisioned with the `WhatsApp` bridge. 
Once reprovisioning is finished, you be able to bridge `WhatsApp` to your EMS server using your Element client.

## Bridge WhatsApp to your EMS server

1. Once the bridge is running, open your Element app. Click on the `+` next to `People`   
![](images/start-chat.png)  
1.  Create a Direct Message conversation by typing `@whatsappbot:example.ems.host` (replace the domain with the one of your homeserver). Then click`Go` 
![](images/dm-wa-bot.png)  
1. The bridge account will join your room and tell you how to use it
![](images/wabridge-bot-joins-room.png)  
1. Open `WhatsApp` on your mobile device (iOS or Android) and go to `Settings` and then `Linked Devices` and then `Link a Device` and tap `OK` to start the `WhatsApp` QR code scanner. You will use this QR code scanner to scan a QR code displayed by your Element client in the next step  
![](images/wabridge-whatsapp-ios-qrcode.png)
1. From your Element client, send a `login` message to the bot to connect to your `WhatsApp` account  
![](images/wabridge-send-login-message.png)
1. A QR code will be displayed. Quickly scan the QR code with `WhatsApp` on your mobile device. You have about a minute before it times out. If it times out, just send the login message again to generate another QR code  
![](images/wabridge-qr-code-from-login-command.png)  
1. On your Element client, you will see `Successfully logged in, synchronizing chats...` and you will see invitations for each of your `WhatsApp` chats in your Element client. Each `WhatsApp` chat is a separate Matrix room. Join one or more chats and start chatting from either your Element app on desktop, iOS or Android or your `WhatsApp` on mobile.
