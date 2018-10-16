import re		#Special sequence of characters that helps you match or find other strings
import os.path 	#Always the path module suitable for the OS python is running on 
import sys		#System-specific parameters and functions 
from urllib.request import urlretrieve 	#Module for fetching URLs


URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'http_access_log.log'
ERRORS = []
REQUESTED_FILES = []
first_date = '1/1/1900'

if not os.path.isfile(LOCAL_FILE):
	print("Downloading log file from: {0} to {1}/{2}".format(URL_PATH,os.path.dirname(sys.argv[0]),LOCAL_FILE))
local_file, headers = urlretrieve(URL_PATH,LOCAL_FILE)
print("\nFile{} saved to directory.".format(LOCAL_FILE))

fh = open(LOCAL_FILE)