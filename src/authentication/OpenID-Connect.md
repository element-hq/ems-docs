# Authentication via OpenID Connect

Your homeserver can be configured to authenticate its users with an OpenID Connect provider. Here we list the most popular providers and how to configure them.

## Google

For detailed information, read [Google's guide on OpenID](https://developers.google.com/identity/protocols/oauth2/openid-connect).

1. Create a [new application on Google](https://console.developers.google.com/apis/credentials).
1. Click `Create credentials` and `OAuth client ID`.
1. Select the application type `Web application`.
1. Choose a name for you and your users to recognize.
1. Add an authorized redirect URI with your homeserver URL, like `https://my-host.ems.host/_synapse/client/oidc/callback`.
1. Save and note the client ID and client secret. Those are needed when adding the OpenID Connect integration in our interface.

<embed type="video/webm" src="/images/authentication/OpenID-Connect/create-google-oauth.webm" width="600" height="309" autoplay="0">

### In the Element Matrix Services configuration form

Use the preset `Google` for a simplified form or use `Custom` with the following values:

- Issuer must be `https://accounts.google.com/`.
- Use the client id and secret from above.
- Discover must be turned on.
- The scopes should be `openid,profile,email,name`.
- Leave Subject Claim empty.
- Username attribute can be `email`. This means your Matrix addresses will include the server domain of the user's e-mail address.
- Display name attribute can be `name`.

If you want shorter usernames and are not worried about username collisions within your domain, please consider [using SAML2 to authenticate with Google](https://ems.element.io/guides/saml2-google).

## GitHub

For detailed information, read [GitHub's guide on OpenID](https://docs.github.com/en/developers/apps/authorizing-oauth-apps).

1. Create a [new application on GitHub.com](https://github.com/settings/applications/new).
1. Choose a name for you and your users to recognize.
1. Choose a homepage URL. You can pick any URL. If your company maintains a guide on how to use Matrix, this would be most helpful.
1. The Authorization callback URL needs to be `https://my-host.ems.host`. Adapt the URL to match your homeserver's address.
1. Save and note the client ID and client secret. Those are needed when adding the OpenID Connect integration in our interface.

### In the Element Matrix Services configuration form

Use the preset `GitHub` for a simplified form or use `Custom` with the following values:

- Issuer must be `https://github.com/`
- Use the client id and secret from above.
- Discover must be turned off.
- Authorization URI must be `https://github.com/login/oauth/authorize`.
- Token URI must be `https://github.com/login/oauth/authorize`.
- User Info URI must be `https://api.github.com/user`.
- JWKS URI is not required, because the scope `profile` will be requested.
- The scopes should be `openid,profile,read:user`.
- Subject Claim must be `id`.
- Username attribute should be `login`.
- The display name can be `name` (GitHub's display name) or `login` (GitHub's user handle).

## GitLab

For detailed information, read [GitLab's guide on OpenID](https://docs.gitlab.com/ee/integration/openid_connect_provider.html).

1. Create a [new application on GitLab.com](https://gitlab.com/profile/applications).
1. Choose a name for you and your users to recognize.
1. Choose a homepage URL. You can pick any URL. If your company maintains a guide on how to use Matrix, this would be most helpful.
1. The Redirect URL needs to be `https://my-host.ems.host/_synapse/client/oidc/callback`. Adapt the URL to match your homeserver's address.
1. Check the scopes `read_user`, `openid` and `profile`.
1. Save and note the client ID and client secret. Those are needed when adding the OpenID Connect integration in our interface.

To connect your own GitLab instance, simply adapt the URL path.

### In the Element Matrix Services configuration form

- Issuer must be `https://gitlab.com/` or the URL of your GitLab instance.
- Use the client id and secret from above.
- Discover must be turned on.
- The scopes should be `openid,profile,read_user`.
- Leave Subject Claim empty.
- Username attribute should be `nickname`.
- Display name attribute can be `name` (GitLab's display name) or `nickname` (GitLab's user handle).
