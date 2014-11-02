DDNS-CloudFlare
===============
Dynamic DNS using CloudFlare API

###Instructions###
Replace the constant variables in the Python script with those for your account. 

- `API_KEY` - CloudFlare API key available at https://www.cloudflare.com/my-account
- `EMAIL` - Email address registered with CloudFlare
- `DOMAIN` - Top-level domain name
- `NAME` - Subdomain (*optional*)

###Cron###
To run `DDNS-CloudFlare` as a cron job:

- `sudo crontab -e`
- Add the following line to the bottom of the file:
  - `* * * * * /usr/bin/python /path/to/DDNS-CloudFlare.py` (runs every minute)
  - For more information on cron, [read this](http://code.tutsplus.com/tutorials/scheduling-tasks-with-cron-jobs--net-8800)
- Be sure to use the absolute path for both Python and `DDNS-CloudFlare`

