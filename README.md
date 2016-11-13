# OpenTracker-InfluxDB

A script that take statistics from [Bittorrent OpenTracker](https://erdgeist.org/arts/software/opentracker/) and write it into a [InfluxDB](https://www.influxdata.com/time-series-platform/influxdb/) database to use it later with any type of graph generator software like [Grafana](http://grafana.org/) or [Chronograf](https://www.influxdata.com/time-series-platform/chronograf/).

### Configure
Before install the script edit the next variables on it with the correct values:

```python
# InfluxDB server and port (IP:PORT)
influxdb_server = '172.16.2.58:8086'

# InfluxDB Database name
database = 'testdb'

# InfluxDB Auth
username = 'unflux-suser'
password = 'AtB73HeTqp'
```
### Install
Copy the script to /usr/local/bin:

```bash
sudo cp opentracker-stats.py /usr/local/bin
```

Copy the systemd service and enable it:

```bash
sudo cp opentracker-stats.service /etc/systemd/system
sudo systemctl enable /etc/systemd/system/opentracker-stats.service
```

### Start, Stop... the script

```bash
sudo service opentracker-stats start
sudo service opentracker-stats stop
sudo service opentracker-stats status
sudo service opentracker-stats reload
sudo service opentracker-stats....
```
