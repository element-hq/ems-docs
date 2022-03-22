# Public Slack Bridge

Matrix.org provides a public free Slack bridge, which is free to use forever but comes with some limitations:

- You can bridge to an unlimited number of channels, but only public channels.
- You must bridge to a public room.
- Matrix users cannot puppet themselves, or Direct Message other users.

This guide explains how to use the free Slack bridge from the Matrix.org Integration Manager to integrate your Matrix room with a Slack room.

Note that EMS offers a [paid Slack bridge](./ems-Slack-Bridge.md) with more features.

It requires your homeserver to be able to federate with Matrix.org.

An EMS server is not required.

## Setup

1. Create a new room in Matrix, with encryption off  
![temp](/images/Screen%20Shot%202020-10-27%20at%2011.12.35%20AM.png)  
![temp](/images/Screen%20Shot%202020-10-27%20at%2011.12.48%20AM.png)

1. Click `Room Info` in the top right corner of the room  
![temp](/images/Screen%20Shot%202020-10-27%20at%2011.13.57%20AM.png)

1. Click `Add widgets, bridges & bots`  
![temp](/images/Screen%20Shot%202020-10-27%20at%2011.14.55%20AM.png)

1. Choose `Slack` from the list of available bridges and integrations  
![temp](/images/Screen%20Shot%202020-10-27%20at%2011.15.37%20AM.png)

1. Click `Add Bridge`  
**NOTE if you have purchased your Slack bridge from EMS:** Ensure it says `Slack integration on <your ems domain>` here.  
![temp](/images/Screen%20Shot%202020-10-27%20at%2011.16.21%20AM.png)

1. Click `Add to Slack`  
![temp](/images/Screen%20Shot%202020-10-27%20at%2011.17.07%20AM.png)

1. Enter your Slack workspace URL, and click `Continue`  
![temp](/images/Screen%20Shot%202020-10-27%20at%2011.18.22%20AM.png)

1. Enter your Slack email address and password, then click `Sign in`  
![temp](/images/Screen%20Shot%202020-10-27%20at%2011.19.10%20AM.png)

1. Click `Allow`  
![temp](/images/Screen%20Shot%202020-10-27%20at%2011.21.07%20AM.png)

1. Close the Slack tab and return to Element  
![temp](/images/Screen%20Shot%202020-10-27%20at%2011.21.48%20AM.png)

1. Click `List channels`  
![temp](/images/Screen%20Shot%202020-10-27%20at%2011.23.00%20AM.png)

1. Click the Slack channel you want to bridge to the Matrix room  
![temp](/images/Screen%20Shot%202020-10-27%20at%2011.23.42%20AM.png)

1. Slack is now added to the Matrix room  
![temp](/images/Screen%20Shot%202020-10-27%20at%204.51.41%20PM.png)

1. Go to the channel you selected on Slack, and add the Element App via the `Integrations` tab in the members sidebar  
![temp](/images/Screen%20Shot%202022-01-25%20at%203.06.48%20PM.png)  
![temp](/images/Screen%20Shot%202022-01-25%20at%203.06.59%20PM.png)  
![temp](/images/Screen%20Shot%202022-01-25%20at%203.07.06%20PM.png)

1. The Matrix room and Slack channel are now bridged  
![temp](/images/Screen%20Shot%202020-10-27%20at%204.57.34%20PM.png)  
![temp](/images/Screen%20Shot%202020-10-27%20at%204.57.48%20PM.png)
