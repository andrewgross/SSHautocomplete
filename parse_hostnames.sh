#!/bin/bash

user_name=$1
file_path=$2

# Long Statement, but not too complex
# Open our known_hosts file
# Take the first field, this should be hostname and/or ip-address format
# Remove results that are just ip addresses
# If a combination of both, just take the hostname
# Slim the results to unique elements
# Sort the results
# Stash it all in a variable
hosts=$(cat ${file_path} | awk '{print $1}' | egrep -v '^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$' | awk -F\, '{print $1}' | uniq | sort)
# Prepend the username to each host
tmp=""
for host in ${hosts}
do
        tmp="${tmp} ${user_name}@${host}"
done
hosts=${tmp}
echo ${hosts}