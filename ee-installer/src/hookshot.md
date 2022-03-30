# GitLab, GitHub, and JIRA Integrations

In Element Enterprise On-Premise, our GitLab, GitHub, and JIRA integrations
are provided by the hookshot package. This documentation explains how to
configure the installer to install hookshot and then how to interact with
hookshot once installed.

## Configuring Hookshot with the Installer

- Copy sample file from `config-sample/hookshot/hookshot.yml` to
 `extra-config/hookshot`
- Edit the file with the following values :
  - `ems_bridges_registry_username` :  ems bridges registry token name
  - `ems_bridges_registry_password` :  ems bridges registry token password
  - `logging_level` : The logging level
  - `hookshot_fqdn` : The adress of hookshot webhook fqdn. It should match
  something like `hookshot.<fqdn.tld>`
  - `passkey` : The name of the local key file. It can be generated using
     openssl - `openssl genrsa -out key.pem 4096`
  - `provisioning_secret` : The provisioning secret used with integration
     managers. Necessary for integration with dimension.
  - `bot_name` : The name of hookshot bot
  - `bot_avatar` : An `mxc://` uri to the hookshot bot avatar image.
- Restart the install script

## Enabling GitHub Integration

### On GitHub

- This bridge requires a [GitHub
 App](https://github.com/settings/apps/new). You will need to create one.
- On the callback URL, set the following one : `https://<hookshot_fqdn>/oauth`
 and enable `Request user authorization (OAuth) during installation`
- On the webhook URL, set the following one : `https://<hookshot_fqdn>/`
- For the webhook secret, you can generate one using `pwgen 32 1`
 to generate one for example. Keep it somewhere safe, you'll need to to
 configure the bridge.
- Set the following permissions for the webhook :
  - Repository
    - Actions (read)
    - Contents (read)
    - Discussions (read & write)
    - Issues (read & write)
    - Metadata
    - Projects (read & write)
    - Pull requests (read & write)
  - Organisation
    - Team Discussions (read & write)

### On the installation

- Copy sample file from `config-sample/hookshot/github.yml` to
 `extra-config/hookshot`
- Edit the file with the following values :
  - `github_auth_id` : The AppID given in your github app page
  - `github_key_file` : The key file received via the `Generate a private
     key` button under `Private keys` section of the github app page.
  - `github_webhook_secret` : The webhook secret configured in the app.
  - `github_oauth_client_id` : The OAuth ClientID of the github app page.
  - `github_oauth_client_secret` : The OAuth Client Secret of the github
     app page.
  - `github_oauth_default_options` A mapping to enable special oauth
     options.
- Restart the install script

### In Element's room

- As an administrator of the room, invite the hookshot bot
- Start a private conversation with the bot
- Type `github login`
- Follow the link to connect the bot to the configured app
- If you have setup Dimension, you can use the integration manager to add
 a bridge to github

## Enabling Gitlab integration

### On Gitlab

- Add a webhook under the group or the repository you are targeting
- On the webhook URL, set the following one : `https://<hookshot_fqdn>/`
- For the webhook secret, you can generate one using `pwgen 32 1`
 to generate one for example. Keep it somewhere safe, you'll need to to
 configure the bridge.
- You should add the events you wish to trigger on. Hookshot currently
 supports:
  - Push events
  - Tag events
  - Issues events
  - Merge request events
  - Releases events

### On the installation

- Copy sample file from `config-sample/hookshot/gitlab.yml` to
 `extra-config/hookshot`
- Edit the file with the following values :
  - `gitlab_instances`: A mapping of the gitlab servers
    - `git.example.org`: Replace with name of the gitlab server
      - `url`: Replace with URL of the gitlab server
  - `gitlab_webhook_secret`: The secret configured in the webhook.

### In Element's room

- As an administrator of the room, invite the hookshot bot
- As an administrator of the room, run the command `/devtools`
- Choose `Send Custom Event`
- Switch the button `Event` to `State Event` by clicking on it
- In `Event Type`, enter `uk.half-shot.matrix-hookshot.gitlab.repository`
- In `State key`, enter a random value, for example generated after `pwgen
 32 1`
- In `Event Content`, enter :

```yaml
{
    "instance": "<your instance name in gitlab.yml>",
    "path": "<username-or-group/repo>"
}
```

## Enabling JIRA integration

### On JIRA

- This should be done for all JIRA organisations you wish to bridge. The
 steps may differ for SaaS and on-prem, but you need to go to the
 webhooks configuration page under Settings > System. It should point to
 `https://<hookshot_fqdn>/`
- For the webhook secret, you can generate one using `pwgen 32 1`
 to generate one for example. Keep it somewhere safe, you'll need to to
 configure the bridge.

#### Enable OAuth

The JIRA service currently only supports atlassian.com (JIRA SaaS) when
handling user authentication. Support for on-prem deployments is hoping to
land soon.

- You'll first need to head to
 <https://developer.atlassian.com/console/myapps/create-3lo-app/> to create a
 "OAuth 2.0 (3LO)" integration.
- Once named and created, you will need to:
- Enable the User REST, JIRA Platform REST and User Identity APIs under
  Permissions.
- Use rotating tokens under Authorisation.
- Set a callback url. This will be the public URL to hookshot with a path
  of /jira/oauth.
- Copy the client ID and Secret from Settings

### On the installation

- Copy sample file from `config-sample/hookshot/jira.yml` to
 `extra-config/hookshot`
- Edit the file with the following values :
  - `jira_webhook_secret`: The webhook secret configured
  - `jira_oauth_client_id`: If Oauth is enabled, it should point to the
   ClientID in Jira's App page. Else, you can keep it empty.
  - `jira_oauth_client_secret`: If Oauth is enabled, it should point to
   the Client secret in Jira's App page. Else, you can keep it empty.

### In Element's room

- As an administrator of the room, invite the hookshot bot
- If you have setup Dimension, you can use the integration manager to add
 a bridge to JIRA

## Enabling generic webhooks integration

### On the installation

- Copy sample file from `config-sample/hookshot/generic.yml` to
 `extra-config/hookshot`
- Edit the file with the following values :
  - `generic_enabled`: `true` to enable it
  - `generic_allow_js_transformation_functions`:
   `true` if you want to enable [javascript
   transformations](https://matrix-org.github.io/matrix-hookshot/setup/webhooks.html#javascript-transformations)
  - `generic_user_id_prefix`: Choose a prefix for the users generated by
   hookshot for webhooks you'll create

### In Element's room

- As an administrator of the room, invite the hookshot bot
- Type `!hookshot webhook <name of the webhook>`
- The bot will answer with a URL that you can set up as a webhook.
- Please ensure that the `Content-Type` is set to the type matching what
 the webhook sends
- If you have setup Dimension, you can use the integration manager to add
 a bridge to a new webhook
