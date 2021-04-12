# Ems Server With Custom Domain <!-- omit in toc -->

This article is licensed under the standard MIT license. See [[Home]] for a full copy.

For this guide, I will be using the domain [twily.org](https://twily.org/). I will set up EMS so that the Matrix usernames becomes `@someone:twily.org`, and the Element client will be at [https://chat.twily.org/](https://chat.twily.org/)

From the guide at [[Get-Your-Own-EMS-Server]], I will be replacing the EMS hostname `ems-demo-staging.ems.host` with `ems-custom-demo-staging.ems.host`

The guide assumes you already have a website on the root of your domain with https enabled.  
![](images/Screen%20Shot%202020-07-31%20at%209.06.17%20AM.png)

1. Follow step 1 - 10 from [[Get-Your-Own-EMS-Server]]

1. On step 10 from [[Get-Your-Own-EMS-Server]], turn ON `Custom DNS`  
![](images/Screen%20Shot%202020-07-31%20at%209.07.59%20AM.png)

1. In the `Custom Homeserver domain` field, enter `twily.org`  
![](images/Screen%20Shot%202020-07-31%20at%209.08.47%20AM.png)

1. Create two files on your website according to the instructions given.  
The path cannot be changed, but up to 30 redirects are supported.  
While not required, you should also add the header `Content-Type application/json` to both files.

    1. `https://twily.org/.well-known/matrix/server`  
    ![](images/Screen%20Shot%202020-07-31%20at%209.12.39%20AM.png)
        ```json
        {
            "m.server": "ems-custom-demo-staging.ems.host:443"
        }
        ```

    2. `https://twily.org/.well-known/matrix/client`  
    ![](images/Screen%20Shot%202020-07-31%20at%209.19.07%20AM.png)  
    You need to enable the CORS header `Access-Control-Allow-Origin: *` on the web server for this file. See [https://enable-cors.org/](https://enable-cors.org/) for instructions on how to do this.
        ```json
        {
            "m.homeserver": {
                "base_url": "https://ems-custom-demo-staging.ems.host"
            },
            "m.identity_server": {
                "base_url": "https://vector.im"
            }
        }
        ```

1. Click `Check again` to verify that your `.well-known` files are configured correctly  
![](images/Screen%20Shot%202020-07-31%20at%209.22.19%20AM.png)

1. You can also verify your `.well-known` files from the command line. Note the lines `access-control-allow-origin: *` and `content-type: application/json`

    1. On Mac or Linux, using your `terminal`  
        ```
        $ curl -i https://twily.org/.well-known/matrix/client
        HTTP/2 200 
        date: Fri, 31 Jul 2020 09:11:21 GMT
        content-type: application/json
        content-length: 129
        set-cookie: __cfduid=x...; expires=Sun, 30-Aug-20 09:11:21 GMT; path=/; domain=.twily.org; HttpOnly; SameSite=Lax
        access-control-allow-origin: *
        cf-cache-status: DYNAMIC
        cf-request-id: 0...
        expect-ct: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
        server: cloudflare
        cf-ray: 5...

        {
            "m.homeserver": {
                "base_url": "https://ems-custom-demo-staging.ems.host"
            },
            "m.identity_server": {
                "base_url": "https://vector.im"
            }
        }

        $ curl -i https://twily.org/.well-known/matrix/server
        HTTP/2 200 
        date: Fri, 31 Jul 2020 09:11:25 GMT
        content-type: application/json
        content-length: 52
        set-cookie: __cfduid=x...; expires=Sun, 30-Aug-20 09:11:25 GMT; path=/; domain=.twily.org; HttpOnly; SameSite=Lax
        access-control-allow-origin: *
        cf-cache-status: DYNAMIC
        cf-request-id: 0...
        expect-ct: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
        server: cloudflare
        cf-ray: 5...

        {
            "m.server": "ems-custom-demo-staging.ems.host:443"
        }   
        ```

    2. On Windows, using `PowerShell`  
        ```
        PS C:\Users\twilight> Invoke-WebRequest -Uri https://twily.org/.well-known/matrix/client


        StatusCode        : 200
        StatusDescription : OK
        Content           : {
                                "m.homeserver": {
                                    "base_url": "https://ems-custom-demo-staging.ems.host"
                                },
                                "m.identity_server": {
                                    "base_url": "https://vector.im"
                                }
                            }
        RawContent        : HTTP/1.1 200 OK
                            Connection: keep-alive
                            Access-Control-Allow-Origin: *
                            CF-Cache-Status: DYNAMIC
                            cf-request-id: 0...
                            Expect-CT: max-age=604800, report-uri="https://repor...
        Forms             : {}
        Headers           : {[Connection, keep-alive], [Access-Control-Allow-Origin, *], [CF-Cache-Status, DYNAMIC], [cf-request-id, 0...]...}
        Images            : {}
        InputFields       : {}
        Links             : {}
        ParsedHtml        : System.__ComObject
        RawContentLength  : 129


        PS C:\Users\twilight> Invoke-WebRequest -Uri https://twily.org/.well-known/matrix/server


        StatusCode        : 200
        StatusDescription : OK
        Content           : {
                                "m.server": "ems-custom-demo-staging.ems.host:443"
                            }
        RawContent        : HTTP/1.1 200 OK
                            Connection: keep-alive
                            Access-Control-Allow-Origin: *
                            CF-Cache-Status: DYNAMIC
                            cf-request-id: 0...
                            Expect-CT: max-age=604800, report-uri="https://repor...
        Forms             : {}
        Headers           : {[Connection, keep-alive], [Access-Control-Allow-Origin, *], [CF-Cache-Status, DYNAMIC], [cf-request-id, 0...]...}
        Images            : {}
        InputFields       : {}
        Links             : {}
        ParsedHtml        : System.__ComObject
        RawContentLength  : 52
        ```

1. You can continue without the `.well-known` files in place, but your server will have limited functionality until this is fixed

1. In the `Custom Client domain` field, enter `chat.twily.org`. This can be any domain, except the same as `Custom Homeserver domain`  
![](images/Screen%20Shot%202020-07-31%20at%209.26.35%20AM.png)

1. Create a CNAME DNS record with your DNS provider according to the instructions given  
![](images/Screen%20Shot%202020-07-31%20at%209.51.37%20AM.png)  
`chat.twily.org.  CNAME  ems-custom-demo-staging.element.io.`

1. This shows how this is done with CloudFlare DNS. Depending on your DNS provider this might be different. Consult the documentation for your provider. Note that Proxy must be turned off with CloudFlare.  
![](images/Screen%20Shot%202020-07-31%20at%209.52.41%20AM.png)

1. Back on EMS, click `Check again`. Note that sometimes it might take a while for your new DNS record to propagate. You can still continue, but functionality will be limited. Check back with the Hosts tab on [https://ems.element.io/user/hosting](https://ems.element.io/user/hosting) and click `Rebuild Host` once the DNS record is in place.  
![](images/Screen%20Shot%202020-07-31%20at%209.56.18%20AM.png)

1. You can also verify your CNAME DNS record using the command line

    1. On Mac or Linux, using your `terminal`  
        ```
        $ dig chat.twily.org CNAME

        ; <<>> DiG 9.10.6 <<>> chat.twily.org CNAME
        ;; global options: +cmd
        ;; Got answer:
        ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 57888
        ;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

        ;; OPT PSEUDOSECTION:
        ; EDNS: version: 0, flags:; udp: 512
        ;; QUESTION SECTION:
        ;chat.twily.org.			IN	CNAME

        ;; ANSWER SECTION:
        chat.twily.org.		299	IN	CNAME	ems-custom-demo-staging.element.io.

        ;; Query time: 32 msec
        ;; SERVER: 8.8.4.4#53(8.8.4.4)
        ;; WHEN: Fri Jul 31 10:21:56 BST 2020
        ;; MSG SIZE  rcvd: 91
        ```

    2. On Windows, using `PowerShell`  
        ```
        PS C:\Users\twilight> Resolve-DnsName -Name chat.twily.org -Type CNAME

        Name                           Type   TTL   Section    NameHost
        ----                           ----   ---   -------    --------
        chat.twily.org                 CNAME  299   Answer     ems-custom-demo-staging.element.io
        ```

1. Continue from step 11 on [[Get-Your-Own-EMS-Server]]
