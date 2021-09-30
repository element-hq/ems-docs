# Verify new Login

When you log in to a new device/session, you must verify the login and connect it to cross signing and secret storage to access your backed up encryption keys for historical messages. This assumes you already have configured cross signing, see [Set up Cross Signing](Set-up-Cross-Signing.md).

1. Log in to Element with your username and password  
![Element Web login screen](images/Verify-new-Login/Screen%20Shot%202021-09-28%20at%2011.55.36%20AM.png)

1. Choose one of the methods below for cross signing

## Compare emojis using another login

1. Click `Use another login`  
![Element login screen](images/Verify-new-Login/Screen%20Shot%202021-09-28%20at%2011.59.21%20AM.png)
1. On another device/session that is connected to cross signing, click `Accept`  
![New session Verification request](images/Verify-new-Login/Screen%20Shot%202021-09-28%20at%2001.48.41%20PM.png)
1. Click `Start`
![Choose method to Verify other login](images/Verify-new-Login/Screen%20Shot%202021-09-28%20at%2001.48.46%20PM.png)
1. Compare the emojis on your new and old sessions. They should be the same emojis and in the same order. Click `They match` on both sessions  
![Compare emojis](images/Verify-new-Login/Screen%20Shot%202021-09-28%20at%2001.48.52%20PM.png)
1. If all was successful, you should get this green shield on both sessions. Click `Got it`. Your new device/session is now verified and will download your backed up message encryption keys  
![Session verified green shield](images/Verify-new-Login/Screen%20Shot%202021-09-28%20at%2001.49.01%20PM.png)

## Scan QR code on another login

Login is here demonstrated on Element Android

1. On your phone, tap `Verify this login`  
![Verify this login from Element Android](images/Verify-new-Login/Screenshot_20210928-135639.png)
1. Your phone is now waiting for you to accept from another device  
![Waiting for another session to accept verification request](images/Verify-new-Login/Screenshot_20210928-135647.png)
1. On another device/session that is connected to cross signing, click `Accept`  
![New session Verification request](images/Verify-new-Login/Screen%20Shot%202021-09-28%20at%2001.48.41%20PM.png)
1. On your phone, tab `Scan with this device`  
![Scan with this device](images/Verify-new-Login/Screenshot_20210928-135701.png)
1. Using your phone, scan the QR code shown on your other session  
![QR code scanner on Element Android](emages/../images/Verify-new-Login/Screenshot_20210928-140736.png)  
![QR code for verification shown on the other session](images/Verify-new-Login/Screen%20Shot%202021-09-28%20at%2001.57.15%20PM.png)
1. Your phone waits for you to confirm green shield on your other session. Click `Yes`  
![Element Android waiting for other session](images/Verify-new-Login/Screenshot_20210928-135853.png)  
![Verify by scanning - both sessions should show the same green shield](images/Verify-new-Login/Screen%20Shot%202021-09-28%20at%2001.58.43%20PM.png)
1. Tap `Done` on your phone  
![Element Android - session verified](images/Verify-new-Login/Screenshot_20210928-135859.png)
1. If all was successful, you should get this green shield on both sessions. Click `Got it`. Your new device/session is now verified and will download your backed up message encryption keys  
![Session verified green shield](images/Verify-new-Login/Screen%20Shot%202021-09-28%20at%2001.49.01%20PM.png)

## Using your Security Key

1. Click `Use Security Key`  
![Verify this login, choose between using another device or entering security key](images/Verify-new-Login/Screen%20Shot%202021-09-28%20at%2011.59.21%20AM.png)
1. Enter your Security key when prompted and click `Continue`  
![Enter Security Key](images/Verify-new-Login/Screen%20Shot%202021-09-28%20at%2012.00.38%20PM.png)
1. If all was successful, you should get this green shield on both sessions. Click `Got it`. Your new device/session is now verified and will download your backed up message encryption keys  
![Session verified green shield](images/Verify-new-Login/Screen%20Shot%202021-09-28%20at%2001.49.01%20PM.png)
