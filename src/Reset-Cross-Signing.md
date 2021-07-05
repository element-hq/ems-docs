# Reset Cross Signing

This article is licensed under the standard MIT license. See [Home](index.md) for a full copy.

Only do this if you have forgotten or lost your cross signing backup passphrase.

Please read through the entire document before starting to make sure you understand the consequences of doing this.

* **[If you have an active session](#if-you-have-an-active-session)**
* **[If you DO NOT have an active session](#if-you-do-not-have-an-active-session)**


## If you have an active session

1. You may wish to backup your keys before doing this just to be on the safe side if something goes wrong: See [Export and Import E2E Room Keys](Export-and-Import-E2E-Room-Keys.md)

2. Go to Element `Security & Privacy` settings &#8595;<br />
![](images/Screen%20Shot%202020-07-30%20at%203.02.07%20PM.png)

1. Click `Reset cross-signing and secret storage` &#8595;<br />
![](images/Screen%20Shot%202020-07-30%20at%203.05.05%20PM.png)

1. Click `Clear cross-signing keys` &#8595;<br />
![](images/Screen%20Shot%202020-07-30%20at%203.06.18%20PM.png)

1. Click `Generate a Security Key` or `Enter a Security Phrase`. Then `Continue` &#8595;<br />
![](images/Screen%20Shot%202020-07-30%20at%203.06.50%20PM.png)

1. Take note of your key then click `Continue` &#8595;<br />
![](images/Screen%20Shot%202020-07-30%20at%203.07.52%20PM.png)

1. Enter your account password and click `Continue`  &#8595;<br />
![](images/Screen%20Shot%202020-07-30%20at%203.09.47%20PM.png)

1. You can delete any untrusted sessions in Element `Security & Privacy` settings. Select the sessions you want to remove and click `Delete 1 session` &#8595;<br />
![](images/Screen%20Shot%202020-07-30%20at%203.14.55%20PM.png)


## If you DO NOT have an active session

Doing this will destroy all your keys and you will NOT be able to access any historical encrypted messages.

1. Log in to Element &#8595;<br />
![](images/Screen%20Shot%202020-07-30%20at%202.59.21%20PM.png)

1. Click `Skip` &#8595;<br />
![](images/Screen%20Shot%202020-07-30%20at%203.00.40%20PM.png)

1. Click `Skip` again &#8595;<br />
![](images/Screen%20Shot%202020-07-30%20at%203.01.08%20PM.png)

1. Do not connect to Key Backup or verify session when asked

1. Note that you will not be able to decrypt any previous messages after doing this &#8595;<br />
![](images/Screen%20Shot%202020-07-30%20at%203.12.36%20PM.png)

1. Follow the steps from [If you have an active session](#if-you-have-an-active-session)
