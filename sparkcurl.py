#!/usr/bin/python

import os
import subprocess
from nxapi_module import *

response = donxapi('cli_show', 'show version')
print response['body']['kickstart_ver_str']
version = response['body']['kickstart_ver_str']
chassis = response['body']['chassis_id']
updays = response['body']['kern_uptm_days']
uphrs = response['body']['kern_uptm_hrs']
upmins = response['body']['kern_uptm_mins']

response = donxapi('cli_show', 'show hostname')
hostname = response['body']['hostname']

#outj = "\"Hi, I am " + hostname + ", and I am a " + chassis
outj = "\"Hi, I am " + hostname + ", a " + chassis + ". I have been up for " + str(updays) + " days, " + str(uphrs) + " hours, and " + str(upmins) + " minutes."

#cmd = "curl --proxy http://proxy.esl.cisco.com:8080 -X POST --data-urlencode 'payload={ \"channel\": \"#chat9k\", \"username\": \"" + hostname + "\", \"text\": " + outj + "\"}' <slackhook>"
cmd = "curl --proxy http://proxy.esl.cisco.com:80 -X POST -H \"Authorization: Bearer MWEzOTI3NWYtZjkzNC00YTI1LTg2MDQtZGE1NTIzNjVkYmIwYmFhYzA4M2EtMGFm\" -H \"Content-Type: application/json\" -H \"Cache-Control: no-cache\" -d '{\"roomId\" : \"Y2lzY29zcGFyazovL3VzL1JPT00vZWU5MDZiOWUtYzZiMS0zYmY2LWJmMWUtYzkzZGE4ZDdmNTcy\", \"text\": " + outj + "\"}' 'https://api.ciscospark.com/v1/messages'"
print "\n\n\n"
print cmd
print "\n\n\n"
os.system(cmd)

response = donxapi('cli_show', 'show int mgmt0')
intf = response['body']['TABLE_interface']['ROW_interface']
iname = intf['interface']
ipktsin = intf['vdc_lvl_in_pkts']
ibytesin = intf['vdc_lvl_in_bytes']

outj = "\"I have seen " + str(ipktsin) + " packets with a total of " + str(ibytesin) + " bytes on my interface " + iname + "."
print "outj is ", outj

cmd = "curl --proxy http://proxy.esl.cisco.com:80 -X POST -H \"Authorization: Bearer MWEzOTI3NWYtZjkzNC00YTI1LTg2MDQtZGE1NTIzNjVkYmIwYmFhYzA4M2EtMGFm\" -H \"Content-Type: application/json\" -H \"Cache-Control: no-cache\" -d '{\"roomId\" : \"Y2lzY29zcGFyazovL3VzL1JPT00vZWU5MDZiOWUtYzZiMS0zYmY2LWJmMWUtYzkzZGE4ZDdmNTcy\", \"text\": " + outj + "\"}' 'https://api.ciscospark.com/v1/messages'"
os.system(cmd)