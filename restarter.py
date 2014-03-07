#!/usr/bin/env python
"""
Check to see if an process is running. If not, restart.
Run this in a cron job
"""
import os
process_name= "/home/xj2alarm.py" # change this to the name of your process
tmp2 = os.popen("ps -Af").read()

if process_name not in tmp2[:]:
    newprocess="nohup python %s &" % (process_name)
    os.system(newprocess)
