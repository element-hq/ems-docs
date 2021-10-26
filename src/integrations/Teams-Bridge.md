# Teams Bridge

## Introduction

This guide explains how to set up a Teams bridge with your Element host. You will need to be an administrator of your Teams group to set the bridge up. Connecting to a Teams workspace that you do not control is currently not supported.

## Setup

The setup process requires fetching a few details from your Teams workspace.

### Teams Link

![`Get link to team` item on the Team context menu](/images/integrations/Teams-Bridge/get-link.png)

You can get the link to your team by copying it from the Teams interface. Pasting it into this form will bring up a button which will take you into the consent flow. Consenting to the form will allow Element to access your Team on Microsoft.

### Bot Username and Password

The bridge requires a Teams user to be registered as a `bot` to send messages on behalf of Matrix users. You just need to allocate one user from the Teams interface to do this.

1. First, you must go to the [Azure Active Directory page](https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/Overview).
1. Click users.
1. Click New user.
1. Ensure `Create user` is selected.
    - Enter a User name ex. `matrixbridge`.
    - Enter a Name ex. `Matrix Bridge`.
    - Enter an Initial password.
    - Create the user.
    - Optionally, set more profile details like an avatar.
1. You will now need to log in as this new bot user to set a permanent password (Teams requires you to reset the password on login).
1. After logging in you should be prompted to set a new password.
1. Enter the bot username and password into the integration form.

### Welcome room

Users can be automatically prompted to link their Teams account to their Element account when they join an Element workspace. Ticking the **Send a welcome message to new users of the bridge** checkbox will make the bridge bot user start a DM with any new joining Element users and let them know how to get connected. If you wish to disable this behavior, leave this box unchecked.

### Max Teams users

The bridge is billed based upon the number of participating Teams-side users, so you should set the maximum number of users you'd expect to see using the bridge to ensure your costs meet expectations. If the number of active Teams users exceeds this value, the bridge will be blocked, until you increase the limit. **Whatever you set the limit to, you will only be charged for the number of remote users actively using the bridge.**
