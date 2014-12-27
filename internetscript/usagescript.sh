#!/bin/bash

#Download html to a file
curl http://ubcit.webi.it.ubc.ca/__shared/Pagelet5764.html -o "usage.txt"

#Run python script
python /Users/[user]/Python-BashScript/internetscript/readusage.py

