off-by-slash
============

Link: https://backdoor.sdslabs.co/challenges/Off-by-slash \
Tags: [n00b19CTF] [web]

Description:
------------

Fetch a flag from an nginx web server.

Solution:
---------

If you look inside the nginx config file, you'll see that the URL `/nginx/flag.txt` has been rerouted to an error page:

```
location /nginx {
    alias /var/www/html/nginx/;
}

location /nginx/flag.txt {
    return 301 http://$host/disallow.html;
}
```

So how can we access `/nginx/flag.txt` on this server? Well, it turns out that the title of this challenge is a huge clue. If you search for "nginx off-by-slash vulnerability", you'll probably end up looking at [this Tweet by @xOrz](https://twitter.com/x0rz/status/1052899891624710145). I'm sure you can figure out the rest.
