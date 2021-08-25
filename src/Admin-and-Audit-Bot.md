# Admin and Audit Bot

# Overview

The Admin Bot adds an account with administrator privileges to every room on your server. You can log into this account, post messages and modify the state of any local room.

The Audit Bot is for compliance with the law or your organization's guidelines, this service account allows you to read every conversation on your server, including encrypted conversations.

Both bots are aimed primarily at enterprise customers and available as addons to Gold and Platinum EMS servers.

This guide assumes you already have a Gold or Platinum server configured and running. See [Get Your Own EMS Server](Get-Your-Own-EMS-Server.md) for instructions on how to set up an EMS server.

The Setup and Usage sections covers both bots as the process is the same. See the sections per bot below.

# Setup

1. Go to the Integrations tab on https://ems.element.io/user/hosting#/integrations and click `Admin Bot` or `Audit Bot` from the list of Extensions. Click `Setup Integration`, then `Purchase` on the following modal  
![](images/Screen%20Shot%202021-08-24%20at%2004.30.37%20PM.png)

1. Once the provisioning has completed, you will be given the option to log in to Element Web as the `adminbot` or `auditbot` account and shown the `Secure Backup Phrase` you can use to access encrypted messages.

1. The bots will automatically be invited to, joins, and is made room admin in all new rooms created on your local server  
![](images/Screen%20Shot%202021-08-24%20at%2009.15.27%20PM.png)

# Usage

1. If this is the first time you log in using this browser, click `Secure Backup Phrase (click to view)` and copy the phrase to your clipboard  
![](images/Screen%20Shot%202021-08-24%20at%2009.10.29%20PM.png)

1. Click the `Click here to log in` button, a new tab will open a Element Web instance already signed in as the `adminbot` or `auditbot`. You will need to enter the Secure Backup Phrase on first log in with a new browser in order to access Secure Storage and encrypted messages

## Admin Bot


## Audit Bot
