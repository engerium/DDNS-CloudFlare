#!/usr/bin/python

# DDNS - CloudFlare
# Developed By: Preshant Achuthan
# Fork Me on GitHub: github.com/engerium

# Imports
import os
import subprocess


# Constants
API_KEY = ""
DNS_ID = ""
EMAIL = ""
DOMAIN = ""
DNS_NAME = ""


# Main function
def main():
	# Get current IP address
	ip = get_ip()

	# Get log IP address
	log_ip = open_log("./.DDNS-CloudFlare.ip", ip)

	# Check if current IP same as log IP
	if (ip == log_ip):
		print ("No Change")

	# Update CloudFlare with current IP
	else:
		os.system("curl https://www.cloudflare.com/api_json.html \
  					-d 'a=rec_edit' \
 			 		-d 'tkn=" + API_KEY + "' \
  					-d 'id=" + DNS_ID + "' \
  					-d 'email=" + EMAIL + "' \
  					-d 'z=" + DOMAIN + "' \
			  		-d 'type=A' \
			  		-d 'name=" + DNS_NAME + "' \
			  		-d 'content=" + ip + "' \
 		 			-d 'service_mode=1' \
  					-d 'ttl=1'")

		# Remove old log file
		os.remove("./.DDNS-CloudFlare.ip")


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
		return "".join(new_ip)


# Calling of main function
if __name__ == '__main__':
	main()