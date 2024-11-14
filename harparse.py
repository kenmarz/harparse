import re
import sys
import json
import string
from haralyzer import HarParser

### Author: KenMarquez ###


example=("\n"
        "This script helps parse json formatted HAR files\n"
        "\n"
        "options: \n"
        "\n"
        "--url   (ie: --url=favicon) Search and return any url with a match for the given value\n"
        '--gt    (ie: --gt=1000) Returns any url response taking longer in milliseconds than the given value"\n' 
        "--tt    Returns only the url timing breakdown (no headers)\n"
        "\n"
        "example: harparser example.com.har --url='favicon' --gt=1000\n\n"
        "The example returns the headers and timing for any url matching favicon whose total time is greater than 1000ms\n"
        "\n"
        )


if len(sys.argv) < 2:
    print(example)
    sys.exit(1)

if sys.argv[1] == "--help":
    print(example)
    exit()

if len(sys.argv) > 1:
    field_1 = sys.argv[1]




with open(field_1, 'r') as f:
    har_parser = HarParser(json.loads(f.read()))

headers = []
def my_function():
    for page in har_parser.pages:
        for entry in page.entries:

            #Parse request headers
            request = entry['request']
            req_headers = request['headers']

            #Parse response headers
            response = entry['response']
            resp_headers = response['headers']

            #Parse other header values
            field_1 = request['url']            
            cookie = request['cookies']
            status = response['status']
            totaltime = entry['time']
            times = entry['timings']

            if "serverIPAddress" in entry:
                remote_server = entry['serverIPAddress']
            else:
                remote_server = "Empty"

            if "_priority" in entry:
                priority = entry['_priority']
            else:
                priority = "None"
 
           # if re.match(r'H|L|M|h|l|m|V|v', entry['_priority']):
           #     priority = entry['_priority']
           # else:
           #     priority = "NONE"

            ##if not re.search(r'H|L|M|h|l|m', priority):
                ##priority = "NONE"


            #function to separate request headers name/values and call condition requirement
            def my_req_headers():
                print('\n============================================================\n')
                print('RemoteServerIP:' + remote_server + '\n')
                print('REQUEST HEADERS:')
                print(field_1)
                #print cookie
                for header in req_headers:
                    req_header = header
                    req_header_name = req_header['name']
                    req_header_value = req_header['value']
                    req_entries = req_header_name +":"+ req_header_value
                    print(req_entries)

            #function to separate response headers name/values and call condition requirement
            def my_resp_headers():
                print('\n')
                print('RESPONSE HEADERS:')
                print(status)

                for header in resp_headers:
                    resp_header = header
                    resp_header_name = resp_header['name']
                    resp_header_value = resp_header['value']
                    resp_entries = resp_header_name + ":" + resp_header_value
                    print(resp_entries)

                print('\n')
                print('tt: ' + str(totaltime))
                print('timings: ' + str(times) + '\n')
                print('\n')

            def timing_metrics():
                print('\n============================================================\n')
                print('- RemoteServerIP:' + remote_server + "\n")
                print("- url: " + field_1 + "\n\n" + '- tt: ' + str(totaltime))
                print("- timings: " + str(times))
                print('\n')


            global tt
            global url
            global greaterthan
            global regex_value
            global stringoffields
            global greaterthan_value


            tt = "none"
            url = "none"
            greaterthan = "none"
            greaterthan_value = 0

            stringoffields = str(sys.argv[2:])
            tt_match = re.search(r"--t{2}",stringoffields)
            if tt_match:
                tt = "present"

            greaterthan_match = re.search(r'--gt=(\d+)',stringoffields)
            if greaterthan_match:
                greaterthan_regex = (greaterthan_match.group())
                #greaterthan_value = re.escape(greaterthan_regex[5:])
                greaterthan_value = greaterthan_regex[5:]
                greaterthan = "present"
                
            url_match = re.search(r'--url=([^\s]*\w+)',stringoffields)
            if url_match:
                url_value = url_match.group()
                url = "present"
                regex_value = re.escape(url_value[6:])


            #====================================================


                if tt == "present": 
                    if url == "present" and greaterthan is "present":
                        if float(totaltime) >= float(greaterthan_value) and re.search(regex_value, field_1):
                            timing_metrics()
                    elif url == "present" and greaterthan != "present":
                        if re.search(regex_value, field_1):
                            timing_metrics()
                    else:
                        timing_metrics()

                
                if tt != "present": 
                    if url == "present" and greaterthan == "present":
                        if float(totaltime) >= float(greaterthan_value) and re.search(regex_value, field_1):
                            my_req_headers()
                            my_resp_headers()

                    elif url == "present" and greaterthan != "present":
                        if re.search(regex_value, field_1):
                            my_req_headers()
                            my_resp_headers()


                continue


              

my_function()


### NEED TO MAKE SOME TIME TO COMPLETE ###
