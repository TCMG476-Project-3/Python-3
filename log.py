import re		#Special sequence of characters that helps you match or find other strings
import os.path 	#Always the path module suitable for the OS python is running on 
import sys		#System-specific parameters and functions 
from datetime import datetime
from urllib.request import urlretrieve 	#Module for fetching URLs


URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'http_access_log.log'
ERRORS = []
REQUESTED_FILES = []
first_date = '1/1/1900'

#Dictionaries to store counts
#Created dictionary using key value pairs. The months are the keys and each of their values are initialized at 0
COUNT_REQUESTS_MONTH = {'January': 0, 'February': 0, 'March': 0, 'April': 0, 'May': 0, 'June': 0, 'July': 0, 'August': 0, 'September': 0, 'October': 0, 'November': 0, 'December': 0}
STORE_REQUESTS_MONTH = {'January': [], 'February': [], 'March': [], 'April': [], 'May': [], 'June': [], 'July': [], 'August': [], 'September': [], 'October': [], 'November': [], 'December': []}
COUNT_REQUESTS_DAY = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0, 24: 0, 25: 0, 26: 0, 27: 0, 28: 0, 29: 0, 30: 0, 31: 0}
COUNT_REQUESTS_WEEKDAY = {'Sunday': 0, 'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0}
COUNT_REQUESTS_WEEK = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0, 24: 0, 25: 0, 26: 0, 27: 0, 28: 0, 29: 0, 30: 0, 31: 0, 32: 0, 33: 0, 34: 0, 35: 0, 36: 0, 37: 0, 38: 0, 39: 0, 40: 0, 41: 0, 42: 0, 43: 0, 44: 0, 45: 0, 46: 0, 47: 0, 48: 0, 49: 0, 50: 0, 51: 0, 52: 0}

#Define Counter Variables
s3_count = 0
s4_count = 0
total_count = 0
TOTAL_WEEK_REQUESTS = 0

if not os.path.isfile(LOCAL_FILE):
	print("Downloading log file from: {0} to {1}/{2}".format(URL_PATH,os.path.dirname(sys.argv[0]),LOCAL_FILE))
local_file, headers = urlretrieve(URL_PATH,LOCAL_FILE)
print("\nFile{} saved to directory.".format(LOCAL_FILE))

fh = open(LOCAL_FILE)

# prepare the REgEx
regex = re.compile(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*")

# Let the user know we are parsing the log file.
print("")
print("Parsing {0}/{1}".format(os.path.dirname(sys.argv[0]), LOCAL_FILE))
print("")
# Process each line of the file
for line in fh:
    # Splitting the line into distinct data points
    parts = regex.split(line)

    # Validating the current line appears to be in proper log format.
    if not parts or len(parts) < 7:
        #print("Line {0} is not in expected format, adding to error count.".format(line))
        ERRORS.append(line)
        continue
    # increment the total counter
    total_count += 1

    # parse the log file line date into a date object
    r_date = datetime.strptime(parts[1], "%d/%b/%Y")
    if first_date == '1/1/1900':
        first_date = r_date

    # track the counts by month
    COUNT_REQUESTS_MONTH[calendar.month_name[r_date.month]] += 1
    STORE_REQUESTS_MONTH[calendar.month_name[r_date.month]].append(line)

    # track the counts by month
    COUNT_REQUESTS_DAY[r_date.day] += 1

    # track the counts by day of the week
    COUNT_REQUESTS_WEEKDAY[calendar.day_name[r_date.weekday()]] += 1

    # track the counts by week of the year
    COUNT_REQUESTS_WEEK[r_date.isocalendar()[1]] += 1

print("--------------------")
print("Log File Statistics:")
print("--------------------")
print("Start Day: {}".format(first_date))
print("Total requests: {}".format(total_count))
print("End Day: {}".format(r_date))
print("")
