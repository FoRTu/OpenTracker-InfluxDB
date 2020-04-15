#!/usr/bin/python

# Is necessary to install python-lxml and curl packages

from lxml import etree
import requests
import time
import os

# InfluxDB server and port (IP:PORT or domain:port)
influxdb_server = 'MyInfluxDB.com:8086'

# Uncomment the line below if you use 'https://' to access to your server
influxdb_server = 'https://' + influxdb_server + "/write"

# Uncomment the line below if you use 'http://' to access to your server
#influxdb_server = 'http://' + influxdb_server + "/write"

# InfluxDB Database name
database = 'testdb'

# InfluxDB Auth
username = 'influx-user'
password = 'AtB73HeTqp'

# OpenTracker statistics url
opentracker_url = 'http://mytracker:6969/stats?mode=everything'

# Data query interval in seconds:
wait = 30

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
    params = (
     ('db', database),
     ('precision', 's'),
     ('u', username),
     ('p', password),
    )

    data = 'uptime value=' + uptime + '\ntorrents value=' + torrents + '\npeers value=' + peers + '\nseeds value=' + seeds + '\nleechers value=' + str(leech$
    response = requests.post(influxdb_server, params=params, data=data)

    # wait for 15 seconds
    time.sleep(wait)
