# OpenTracker-InfluxDB

A script that take statistics from [Bittorrent OpenTracker](https://erdgeist.org/arts/software/opentracker/) and write it into a [InfluxDB](https://www.influxdata.com/time-series-platform/influxdb/) database to use it later with any type of graph generator software like [Grafana](http://grafana.org/) or [Chronograf](https://www.influxdata.com/time-series-platform/chronograf/).

### Dependencies

You need to install **python-lxml** package
```bash
sudo apt install python-lxml
```

### Configure
Before install the script edit the next variables on it with the correct values:

```python
# InfluxDB server and port (IP:PORT)
influxdb_server = 'MyInfluxDB.com:8086'

# Uncomment the line below if you use 'https://' to access to your server
influxdb_server = 'https://' + influxdb_server + "/write"

# Uncomment the line below if you use 'http://' to access to your server
#influxdb_server = 'http://' + influxdb_server + "/write"


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

Now you can create your graphs, for example with [Grafana](http://grafana.org/)....

![Grafana-graph](http://i.imgur.com/fz8ntes.png)
