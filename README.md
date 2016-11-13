# OpenTracker-InfluxDB

A script that take statistics from Bittorrent OpenTracker and write it into a InfluxDB database.

### Install
Copy the script to /usr/local/bin:

```bash
sudo cp opentracker_stats.py /usr/local/bin
```

Copy the SystemD service and enable it
sudo cp opentracker-stats.service /etc/systemd/system
sudo systemctl enable sudo systemctl enable /etc/systemd/system/opentracker-stats.service
