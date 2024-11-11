# This script allows for quick analysis of a HAR (.har) json formatted file.
# A HAR file is the recording of a browsers interaction with a web server/proxy.

If you have added this script into your root directory, you can create and test an alias using the below commands.

echo "alias harparse='python ~/harparse.py'" >> .bash_aliases

source ~/.bash_aliases

harparse --help

OUTPUT:


This script helps parse json formatted HAR files

options: 

--url   (ie: --url=favicon) Search and return any url with a match for the given value
--gt    (ie: --gt=1000) Returns any url response taking longer in milliseconds than the given value"
--tt    Returns only the url timing breakdown (no headers)

example: harparser example.com.har --url='favicon' --gt=1000

The example returns the headers and timing for any url matching favicon whith a total time greater than 1000ms


