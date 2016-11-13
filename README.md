# OpenTracker-InfluxDB

A script that take statistics from [Bittorrent OpenTracker](https://erdgeist.org/arts/software/opentracker/) and write it into a [InfluxDB](https://www.influxdata.com/time-series-platform/influxdb/) database to use it later with any type of graph generator software like [Grafana](http://grafana.org/) or [Chronograf](https://www.influxdata.com/time-series-platform/chronograf/).

### Install
Copy the script to /usr/local/bin:

```
sudo cp opentracker-stats.py /usr/local/bin
```

Copy the systemd service and enable it:

```
sudo cp opentracker-stats.service /etc/systemd/system
sudo systemctl enable /etc/systemd/system/opentracker-stats.service
```

### Start, Stop... the script
```
sudo service opentracker-stats start
sudo service opentracker-stats stop
sudo service opentracker-stats status
sudo service opentracker-stats reload
sudo service opentracker-stats....
```
