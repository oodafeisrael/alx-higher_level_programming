#!/bin/bash
# A Bash script that takes in a URL as an argument, sends GET request to the URL, and displays the body of the response.
curl -s "$1" -X GET -H "X-School-User-Id: 98"
