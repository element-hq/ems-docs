# EMS Slack Bridge

The EMS Slack bridge is a paid integration for EMS homeservers. In addition to the features provided by the matrix.org bridge, it:

- Allows you to bridge to private rooms and private channels.
- Allows you to puppet your Slack identity from Matrix, appearing to send messages as if you were using Slack.
- Direct Message other Slack users

## Purchase the Slack integration

1. Open the EMS control panel at: [https://ems.element.io/user/hosting](https://ems.element.io/user/hosting)  
Click the `Integrations` tab  and if you have more than one server, select the server you wish to add the Slack integration to  
![temp](/images/click-integration-tab-ems-user-hosting.png)  

1. Click on `Slack Bridge` in the list of available Bridges
![temp](/images/bridge-integration-list.png)  

1. Enter the maximum number of users in `Maximum Slack users`.  
Please note:  **this is the maximum number of Slack users who actually send messages over the bridge each month. You are only billed for the number of Slack users who are active. Once you exceed the maximum, then the bridge will be disabled until you increase the maximum.**

Once you have entered `Maximum Slack users`, click `Purchase` (remember you can always go back to this step and increase the maximum number of Slack users if you need more in the future).

1. A dialogue will remind you of the price per user and ask if you wish to proceed. Click `Purchase` if you wish to proceed with the Slack Integration  
![temp](/images/integrations/ems-Slack-Bridge/confirm-payment.png)  

1. You will have to wait a few minutes while your host is reprovisioned.
Once reprovisioning is finished, you are able to bridge Slack to your EMS server using your Element client.

## Setup

The setup process for the EMS Slack bridge is explained [here](./morg-Slack-Bridge.md)

## Initiate a DM with a Slack user from Matrix

- Message the Slack bot user on Matrix.
- Say `login`
- Follow the OAuth2 URL to get puppeted to the right Slack instance
- Click a Slack user in Matrix and DM as normal
