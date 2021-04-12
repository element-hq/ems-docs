# Change Account Password <!-- omit in toc -->

This article is licensed under the standard MIT license. See [[Home]] for a full copy.

Resetting the account password will log out all your sessions. Before doing this, make sure that
* all your sessions are connected to key backup,
* all sessions have backed up all their keys. See [[Check-Status]], and
* you have your correct key backup passphrase available.

<br />

- [If you know your current password](#if-you-know-your-current-password)
- [If you do not know your current password](#if-you-do-not-know-your-current-password)

## If you know your current password

1. Go to Element `All settings`  
![](images/Screen%20Shot%202020-09-17%20at%205.24.15%20PM.png)

1. Enter your current password and your new password  
![](images/Screen%20Shot%202020-09-17%20at%205.26.13%20PM.png)

1. You might want to export your `E2E room keys`. Just to be on the safe side in case something goes wrong. See also [[Export-and-Import-E2E-Room-Keys]]

1. Click `Continue`.  
Note: This warning is outdated, see [this issue](https://github.com/vector-im/element-web/issues/15226)  
![](images/Screen%20Shot%202020-09-17%20at%205.28.52%20PM.png)

1. Click `OK`  
![](images/Screen%20Shot%202020-09-17%20at%205.31.01%20PM.png)

1. You now need to sign in again on all your other devices

## If you do not know your current password

Note, this will ony work if you have an email address attached to your Matrix account. If you do not have an email address attached, contact the administrators of your homeserver. (support@matrix.org does not reset passwords in any circumstance)

1. Sign out of Element  
![](images/Screen%20Shot%202020-10-26%20at%2012.32.36%20PM.png)

1. Click `Sign out`  
![](images/Screen%20Shot%202020-10-26%20at%2012.15.05%20PM.png)

1. Click "Not sure of your password? `Set a new one`"  
![](images/Screen%20Shot%202020-10-26%20at%2012.15.56%20PM.png)

1. Enter your email address, and a new password. Then click `Send Reset Email`  
![](images/Screen%20Shot%202020-10-26%20at%2012.20.13%20PM.png)

1. Click `Continue`.  
Note: This warning is outdated, see [this issue](https://github.com/vector-im/element-web/issues/15226)  
![](images/Screen%20Shot%202020-10-26%20at%2012.33.47%20PM.png)

1. When you get this message, check your email  
![](images/Screen%20Shot%202020-10-26%20at%2012.22.21%20PM.png)

1. Click the link in the email. Mae sure it opens in  new browser tab, leaving your Element client open  
![](images/Screen%20Shot%202020-10-26%20at%2012.23.42%20PM.png)

1. Click `Confirm changing my password`  
![](images/Screen%20Shot%202020-10-26%20at%2012.26.36%20PM.png)

1. You can now close this tab and return to Element  
![](images/Screen%20Shot%202020-10-26%20at%2012.27.21%20PM.png)

1. Click `i have verified my email address`  
![](images/Screen%20Shot%202020-10-26%20at%2012.22.21%20PM.png)

1. Click `Return to login screen`  
![](images/Screen%20Shot%202020-10-26%20at%2012.28.38%20PM.png)

1. Sign in like normal with your new password. Note that all your other sessions have been signed out and you need to sign in again
