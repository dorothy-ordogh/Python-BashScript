Python-BashScript
=================

In residence at UBC, they monitor our web usage, capping each student at 7GB. If you reach 7GB, you are put into what they call "the penalty box" but I like to all it internet jail. I am told that if you are a repeat offender in one week (i.e. you pass the 7GB limit twice in one week), they will throw you in jail for the next week–a week of tortuously slow internet in which even a simple web page with only text takes about 6 minutes to load. They say that it is to prevent illegal streaming, but until they figure out a way to differentiate my completely legal Netflix usage from others' illegal streaming, I created a combination bash and python script to warn me when I am reaching the cap. 

UBC respectfully provides a web page that informs you of your usage (which they check every ~15 minutes). What I did was downloaded the web page, extracted the inbound GB usage, and if it is under 6.70GB do nothing, but if it is at or above 6.70GB, show a pop up window that warns me of my usage. Using crontab, I scheduled this script to run every 20 minutes. 

Feel free to use the script. If you do though, please note that this can only run on OS X systems, and please remember to change the paths to the executables. 
