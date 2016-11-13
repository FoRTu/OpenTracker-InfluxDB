#!/usr/bin/python

# Is necessary to install python-lxml and curl packages

from lxml import etree
import subprocess
import time
import os

# InfluxDB server and port (IP:PORT)
influxdb_server = '172.16.2.58:8086'

# InfluxDB Database name
database = 'testdb'

# InfluxDB Auth
username = 'unflux-suser'
password = 'AtB73HeTqp'

# OpenTracker statistics url
opentracker_url = 'http://172.16.2.1:6969/status?mode=everything'

# Data query interval in seconds:
wait = 15

FNULL = open(os.devnull, 'w')

while True:
    status = etree.parse(opentracker_url)
    stats = status.getroot()

    # Uptime
    uptime = stats[2].text

    # Torrents
    torrents = stats[3][0].text

    # Peers
    peers = stats[4][0].text

    # Seeds
    seeds = stats[5][0].text

    # Completed downloads
    completed = stats[6][0].text

    # leechers
    leechers = int(peers) - int(seeds)

    # Uncomment to debug
    #print("Uptime: " + uptime)
    #print("Torrents: " + torrents)
    #print("Peers: " + peers)
    #print("Seeds: " + seeds)
    #print("Leechers: " + str(leechers))
    #print("Completed: " + completed)

    # Write to InfluxDB
    subprocess.call(["curl", "-i", "-XPOST", "http://" + influxdb_server + "/write?db=" + database, "-u", username + ":" + password, "--data-binary", "uptime value=" + str(uptime)], stdout=FNULL, stderr=subprocess.STDOUT)
    subprocess.call(["curl", "-i", "-XPOST", "http://" + influxdb_server + "/write?db=" + database, "-u", username + ":" + password, "--data-binary", "peers value=" +  str(peers)], stdout=FNULL, stderr=subprocess.STDOUT)
    subprocess.call(["curl", "-i", "-XPOST", "http://" + influxdb_server + "/write?db=" + database, "-u", username + ":" + password, "--data-binary", "seeds value=" + str(seeds)], stdout=FNULL, stderr=subprocess.STDOUT)
    subprocess.call(["curl", "-i", "-XPOST", "http://" + influxdb_server + "/write?db=" + database, "-u", username + ":" + password, "--data-binary", "leechers value=" + str(leechers)], stdout=FNULL, stderr=subprocess.STDOUT)
    subprocess.call(["curl", "-i", "-XPOST", "http://" + influxdb_server + "/write?db=" + database, "-u", username + ":" + password, "--data-binary", "torrents value=" + str(torrents)], stdout=FNULL, stderr=subprocess.STDOUT)
    subprocess.call(["curl", "-i", "-XPOST", "http://" + influxdb_server + "/write?db=" + database, "-u", username + ":" + password, "--data-binary", "completed value=" + str(completed)], stdout=FNULL, stderr=subprocess.STDOUT)

    # wait for 15 seconds
    time.sleep(wait)
