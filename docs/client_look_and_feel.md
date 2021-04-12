# Client Look and Feel <!-- omit in toc -->

This article is licensed under the standard MIT license. See [[Home]] for a full copy.

This feature allows you fo customize the home and welcome page on your EMS provided Element Web client.

The guide assumes you already have a website on any domain with https enabled.

1. Create two files on your web server, for example [https://twily.org/ems_home.html](https://twily.org/ems_home.html) and [https://twily.org/ems_welcome.html](https://twily.org/ems_welcome.html)  
![](images/Screen%20Shot%202020-09-15%20at%2011.01.00%20AM.png)

1. Edit `ems_home.html`. This can be as simple as a couple of lines of html, for example  
    ```html
    <h1>Demo Company LTD</h1>
    <h2>Rooms to join</h2>
    <ul>
        <li><a href='/#/room/#welcome:ems-demo-staging.ems.host'>Welcome to Demo web chat (#welcome)</a></li>
        <li><a href='/#/room/#support:ems-demo-staging.ems.host'>Support (#support)</a></li>
        <li><a href='/#/room/#offtopic:ems-demo-staging.ems.host'>Off topic conversation (#offtopic)</a></li>
    </ul>
    ```
    Or you can add a more complex html and styling

1. Looks like this in browser:  
    ![](images/Screen%20Shot%202020-09-15%20at%2011.02.57%20AM.png)

1. Edit `ems_welcome.html`. This is a bit more complex, but can be almost anything you want as long as it has links to Login (/#/login) and 'Create account' (/#/register). The default design is based off [this template](https://github.com/vector-im/element-web/blob/master/res/welcome.html). You can get creative with the CSS and the `!important` tag.

1. Add links to your files on the EMS control panel and click Save.  
![](images/Screen%20Shot%202020-09-15%20at%2011.21.45%20AM.png)

1. Check that it looks correct and that everything works. You do not need to click save or rebuild in the EMS control panel if you make changes to the files. As long as the URL does not change. Refreshing the Element Web Client page is enough.

1. With some hacking you can make it look as you want. (and this is why I am a developer, not a designer...)   
![](images/Screen%20Shot%202020-09-15%20at%2011.37.18%20AM.png)  
![](images/Screen%20Shot%202020-09-15%20at%2011.38.54%20AM.png)  
![](images/Screen%20Shot%202020-09-15%20at%2011.42.57%20AM.png)
