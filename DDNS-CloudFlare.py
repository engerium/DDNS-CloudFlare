#!/usr/bin/python

# DDNS - CloudFlare
# Developed By: Preshant Achuthan
# Fork Me on GitHub: github.com/engerium

# Imports
import os, subprocess, urllib, urllib2, json

# Declare constants
global API_KEY
global EMAIL
global DOMAIN
global NAME

API_KEY = ""
EMAIL = ""
DOMAIN = ""
NAME = ""

# Main function
def main():
	# Get DNS ID
	get_dns_id()

	# Get current IP address
	ip = get_ip()

	# Get log IP address
	log_ip = open_log("/.DDNS-CloudFlare", ip)

	# Check if current IP same as log IP
	if (ip == log_ip):
		print ("No Change")

	# Update CloudFlare with current IP
	else:
		os.system("curl --silent https://www.cloudflare.com/api_json.html \
  					-d 'a=rec_edit' \
 			 		-d 'tkn=" + API_KEY + "' \
  					-d 'id=" + DNS_ID + "' \
  					-d 'email=" + EMAIL + "' \
  					-d 'z=" + DOMAIN + "' \
			  		-d 'type=A' \
			  		-d 'name=" + NAME + "' \
			  		-d 'content=" + ip + "' \
 		 			-d 'service_mode=1' \
  					-d 'ttl=1' \
					> /dev/null")
		
		print ("DNS Updated")

		# Update log file
		update_log('/.DDNS-CloudFlare', ip)

# Get DNS ID
def get_dns_id():
	global DNS_ID

	# Get DNS records from CloudFlare
	raw_args = {'a': 'rec_load_all', 'tkn': API_KEY, 'email': EMAIL, 'z': DOMAIN}
	args = urllib.urlencode(raw_args)
	request = urllib2.Request('https://www.cloudflare.com/api_json.html', args)
	response = urllib2.urlopen(request)
	data = json.load(response)
	filtered_data = data['response']['recs']['objs']

	# Look for desired DNS record and extract DNS ID
	for rec in filtered_data:
		if rec['display_name'] == NAME:
			DNS_ID = rec['rec_id']

# Get current Public IP address
def get_ip():
	return subprocess.check_output(["curl", "-s", "http://icanhazip.com/"]).strip("\n") 

# Open log file to get old ip address
def open_log(filename, new_ip):
	try:
		file = open(filename, "r")
		log_ip = file.readlines()
		file.close()
		return "".join(log_ip)
	
	# Create log file with current IP address
	except:
		file = open(filename, "w")
		file.write(new_ip)
		file.close()
		return 0

# Update log
def update_log(filename, new_ip):
	file = open(filename, 'w')
	file.write(new_ip)
	file.close()

# Calling of main function
if __name__ == '__main__':
	main()
