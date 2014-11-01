#!/usr/bin/python

# DDNS - CloudFlare
# Developed By: Preshant Achuthan
# Fork Me on GitHub: github.com/engerium

# Imports
import os
import subprocess


# Constants
API_KEY = ""


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
		print ip
		print log_ip


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