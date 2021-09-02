# Discord Bridge

## Setup

First, you need to register a Discord application for your bridge. Discord applications can be registered and managed in the [Discord Developer Portal](https://discord.com/developers/applications/).

1. Click on the `New Application` button in the upper right corner.
1. Give it a name (visible when authorizing the bridge), read Discord's Terms and click `Create`.
1. Note the Client ID. It's required for the bridge.
1. Navigate to the `Bot` tab. The navigation can be found on the left.
1. Click `Add Bot`. You may also need to click `Yes, do it!` to confirm your action.
1. Note the Bot Token. It's required for the bridge.

### Connect Discord server(s)

You need to authorize your Discord App to each Discord server you wish to bridge. Give the following URL to a Discord server admin, if you aren't the Discord server admin.

The authorization URL is `https://discordapp.com/api/oauth2/authorize?client_id=YOUR_CLIENT_ID&scope=bot&permissions=607250432`. Replace `YOUR_CLIENT_ID` with your Client ID mentioned above.

## Usage

### Bridge a room

1. In a web browser, navigate to the Discord room you wish to bridge. The URL includes the server ID (also called guild ID) and the channel ID. The URL format is `https://discord.com/channels/GUILD_ID/CHANNEL_ID`.  
    ![Discord showing Channel ID in URL bar](images/Discord-Bridge/1-discord-channel-url.png)
1. In a Matrix room you want to bridge, invite `@discord:example.ems.host` (replace the domain with the one of your homeserver).  
1. Post the message `!discord bridge GUILD_ID CHANNEL_ID` after replacing the two placeholders.  
    ![Element showing the Discord bridge command](images/Discord-Bridge/2-element-bridge-command.png)
1. A privileged Discord user will need to approve the bridge request by responding with `!matrix approve`  
    ![Discord message showing the approve command](images/Discord-Bridge/3-discord-approve-bridge.png)
1. Messages from Discord are now bridged to Matrix and vice versa.  
    ![Element showing a message bridges from Discord](images/Discord-Bridge/4-message-from-discord.png)

### Unbridge

To unbridge a room post `!discord unbridge` in the Matrix room.
