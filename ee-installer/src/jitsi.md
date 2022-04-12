# Configuring Jitsi

By default, our installer will give you an instance of element-web configured to use the `meet.element.io` Jitsi server. If you would like to specify your own Jitsi server for your element-web instance to use, please follow these directions.

## Element Extra Configurations

- Create a file called `jitsi.json` in the `extra-config/element` directory.
- Edit the file :

```lang-none
{
      "jitsi": {
            "preferredDomain": "your.jitsi.example.org"
      }
}
```

replacing `your.jitsi.example.org` with the hostname of your Jitsi server.

- Restart the install script
