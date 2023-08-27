A Few Basics First
TIG Stack stand for Telegraf, InfluxDB, and Grafana.

InfluxDB is the Time Series Database in the TIG stack. InfluxDB is an open-source database optimized for fast, high-availability storage and retrieval of time series data written in Go. InfluxDB is great for operations monitoring, application metrics, and real-time analytics.

Telegraf is the agent for collecting and reporting metrics and data. Telegraf is part of the TIG Stack and is a plugin-driven server agent for collecting and reporting metrics. Telegraf has integrations to source a variety of metrics, events, and logs directly from the containers and systems it’s running on, pull metrics from third-party APIs, or even listen for metrics via StatsD and Kafka consumer services. It also has output plugins to send metrics to a variety of other data stores, services, and message queues, including InfluxDB, Graphite, OpenTSDB, Datadog, Librato, Kafka, MQTT, NSQ, and many others.

Grafana is an open-source metric analytics & visualization suite. It is most commonly used for visualizing time series data for infrastructure and application analytics but many use it in other domains including industrial sensors, home automation, weather, and process control. The tool provides a beautiful dashboard and metric analytics, with the ability to manage and create your own dashboard for your apps or infrastructure performance monitoring.

Prerequisites
To follow this tutorial, you will need:

```
Ubuntu server
Root Privileges
What will we do?
Install InfluxDB
Create Influxdb database and user
Install and Configure Telegraf
Install Grafana
Setup Grafana Data Source
Setup Grafana Dashboard
```

#Step 1: Install InfluxDB
Let’s first install the time series database InfluxDB using the Homebrew package manager. Install InfluxDB by running the below command in your terminal:

$ sudo apt-get install influxdb influxdb-client
Once the installation is complete, start the influxdb service.

# Unmask influxdb service
$ sudo systemctl unmask influxdb.service
# To launch influxdb:
$ systemctl start influxdb
# To not run influxdb in background
$ influxd -config /etc/influxdb/influxdb.conf
If you now run ps -ef | grep influxdb, you should be able to see influxdb running on your machine.

You can also use netstat to check if the influx is up and running,

netstat -plntu 
There may be errors like a port already in use or you might want to use another port.
Running influxd config | head -n 10 gives you the configuration and port to be used.

Adding bind-address = ":<port>" somewhere at the top of the file in /etc/influxdb/influxdb.conf may solves the problem.

In my case, I was getting port already in use error, this was as I was trying to start influxdb twice:

$ systemctl start influxdb
$ influxd -config /etc/influxdb/influxdb.conf
If you want to keep influxdb running in the background use the first command else go for the second.

You might observe influx listening on two ports, 8086 and 8088. By default, 8086 runs the InfluxDB HTTP service for client-server communication and 8088 runs the RPC service for backup and restore.
Both of these ports can be configured in the configuration file, which can be found at /etc/influxdb/influxdb.conf.

#Step 2: Create Influxdb database and user
In order to store all data from telegraf (or any other) agents, we need to set up the influxdb database and user.

InfluxDB provides the CLI tool named influx for interacting with an InfluxDB server. Influx command is like the mysql on MySQL, and mongo on the MongoDB database.

Now you are connected to the default influxdb server on port 8086.

Create a new database and user telegraf with the password pass-telegraf by running influxdb queries below.

> create database telegraf
> create user telegraf with password 'pass-telegraf'
Now check the database and user.

> show databases
> show users
Make sure you get the database and user named telegraf on the influxdb server.


influx
Step 3: Install and configure Telegraf
Next, let’s install telegraf using the same package manager apt.
Install telegraf by running the below command:

$ sudo apt-get install telegraf
Install from a .deb file:

To manually install the Debian package from a .deb file:

Download the latest Telegraf .deb release from the Telegraf section of the downloads page.
Run the following command (making sure to supply the correct version number for the downloaded file):
sudo dpkg -i telegraf_1.17_amd64.deb
Once the installation is complete, start the telegraf service.

# To have launchd start telegraf now and restart at login:
$ systemctl start telegraf
# If you don’t want/need a background service you can just run:
$ telegraf -config /etc/telegraf/telegraf.conf
Telegraf is a plugin-driven agent and has 4 concept plugins type.

Using the Input Plugins to collect metrics.
Using the Processor Plugins to transform, decorate, and filter metrics.
Using the Aggregator Plugins to create and aggregate metrics.
And using the Output Plugins to write metrics to various destinations, including influxdb.
Now when you run ps -ef | grep telegraf, you should be able to see telegraf running on your machine. In case you do not see one, it could be because all output plugins in the telegraf config are commented. In order to solve this, edit the telegraf config as below (if required, backup the configuration file before any changes).

$ cp /etc/telegraf/telegraf.conf /etc/telegraf/telegraf.conf.default
$ vim /etc/telegraf/telegraf.conf
You may need to use sudo for root privileges to execute the command.

Now in telegraf.conf, uncomment the following line and save the file:

[[outputs.influxdb]]
Restart the telegraf service.

$ systemctl restart telegraf
If you re-run ps -ef | grep telegraf, you should now be able to see the telegraf process running.

Next, let’s login into InfluxDB’s command-line interface and check our system metrics.
To access the CLI, launchinflux in your terminal. Once you’ve entered the shell and successfully connected to an InfluxDB node, you’ll see the following output:

$ influx
Connected to http://localhost:8086 version v1.6.4
InfluxDB shell version: v1.6.4
Once you are inside the influx CLI, execute the following set of commands to check the system metrics (includes sample output of each command).

> show databases
name: databases
name
----
_internal
telegraf
> use telegraf
Using database telegraf
> show measurements
name: measurements
name
----
cpu
disk
diskio
mem
processes
swap
system
Now that we have seen system metrics in influxdb, let’s try publishing a custom metric using another input plugin. For demonstration purposes, I have chosen statsd.
Let’s go back to the telegraf.conf and this time uncomment the following line and restart telegraf service:

[[inputs.statsd]]
You should be able to see telegraf listening on port 8125 which is the default port for statsd service.

Let’s say you have a service that is publishing a metric custom_metric to statsd. In this case, you should be able to see custom_metric under telegraf database measurements.

> show measurements
name: measurements
name
----
cpu
custom_metric
disk
diskio
mem
processes
swap
system
Great! Both InfluxDB and Telegraf have now been configured. It’s time to visualize them on a dashboard.

Step 4: Install Grafana
In this first step, you will install Grafana onto your Ubuntu server. You can install Grafana either by downloading it directly from its official website or by going through an APT repository. Because an APT repository makes it easier to install and manage Grafana’s updates, you’ll use that method in this tutorial.

Although Grafana probably will be available in the official Ubuntu packages repository, the version of Grafana there may not be the latest, so use Grafana’s official repository.

Download the Grafana GPG key with wget, then pipe the output to apt-key. This will add the key to your APT installation’s list of trusted keys, which will allow you to download and verify the GPG-signed Grafana package.

To install Grafana, just run the following commands.

$ wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
$ sudo add-apt-repository "deb https://packages.grafana.com/oss/deb stable main"
$ sudo apt update
$ apt-cache policy grafana
The output of the previous command tells you the version of Grafana that you are about to install, and where you will retrieve the package from. Verify that the installation candidate at the top of the list will come from the official Grafana repository at https://packages.grafana.com/oss/deb.

Output of apt-cache policy grafana 
grafana:
  Installed: (none)
  Candidate: 6.3.3
  Version table:
     6.3.3 500
        500 https://packages.grafana.com/oss/deb stable/main amd64 Packages
... 
You can now proceed with the installation:

$ sudo apt install grafana
Once Grafana is installed, use systemctl to start the Grafana server:

$ sudo systemctl start grafana-server
Next, verify that Grafana is running by checking the service’s status:

$ sudo systemctl status grafana-server
You will receive output similar to this:

Output of grafana-server status
● grafana-server.service - Grafana instance
   Loaded: loaded (/usr/lib/systemd/system/grafana-server.service; disabled; vendor preset: enabled)
   Active: active (running) since Tue 2019-08-13 08:22:30 UTC; 11s ago
     Docs: http://docs.grafana.org
 Main PID: 13630 (grafana-server)
    Tasks: 7 (limit: 1152)
...
This output contains information about Grafana’s process, including its status, Main Process Identifier (PID), and more. active (running) shows that the process is running correctly.

Lastly, enable the service to automatically start Grafana on boot:

$ sudo systemctl enable grafana-server
You will receive the following output:

Output of systemctl enable grafana-server
Synchronizing state of grafana-server.service with SysV service script with /lib/systemd/systemd-sysv-install.
Executing: /lib/systemd/systemd-sysv-install enable grafana-server
Created symlink /etc/systemd/system/multi-user.target.wants/grafana-server.service → /usr/lib/systemd/system/grafana-server.service.
This confirms that systemd has created the necessary symbolic links to autostart Grafana.
Grafana is now installed and ready for use.

Hosting Grafana on Different Port
Grafana is hosted by default on port 3000 If you want to host grafana on a different port you have the change the http_port field in the following files:

/etc/grafana/grafana.ini
/usr/share/grafana/conf/defaults.ini
/usr/share/grafana/conf/sample.ini
Remember: Not only change in /etc/grafana/grafana.ini you have to change in /usr/share/grafana/conf/defaults.ini and /usr/share/grafana/conf/sample.ini files. Just search 3000 port(which is the default port for grafana) in these three files and replace it with your preferred port.

Step 5: Setup Grafana Data Source
Launch the grafana service UI on your web browser by opening http://localhost:3000


Grafana Login Page
Now you will be prompted with the page for changing the default password, type your new password and click the ‘Save’ button or Skip this.


You will then be redirected to the default Grafana Dashboard.


Default Grafana Dashboard
Click on Add data source button to add InfluxDB data source. Fill in the influxdb server configurations and database settings as follows.

Type details about the influxdb server configurations.

Name: Influxdb
Type: Influxdb
URL: http://localhost:8086/

Scroll to the bottom page and type details of influxdb database settings.

Database: telegraf
User: telegraf
Password: pass-telegraf

Click on Save and Test at the bottom of the page and make sure you get Data source is working result.


InfluxDB data source configurations
Step 6: Setup Grafana Dashboard
After adding influxdb as a data source to the grafana server, we can now create a dashboard for our system and custom metrics.

We will create a new dashboard from scratch and import one from grafana.

Grafana provides the repository for grafana plugins and dashboards.

Grafana Plugins
Grafana Dashboards
Create New Dashboard from Scratch
On the Grafana home page, click on New dashboard.


Grafana Homepage
Click the Empty Page Button.


Grafana New Dashboard
A dashboard editing panel will show like below.


Edit Dashboard
Choose our previously configured data source InfluxDB from the drop next to Queries to. Select your measurement of interest and then select a value from this measurement. For example, measurement chosen can be cpu and value chosen under this could be usage_user.


Example dashboard showing cpu usage of user
You can choose to add multiple queries to the same panel by clicking Add Query. Modify the Panel title under General section. You can add an optional description. Finally, save the dashboard.

Import Dashboard from Grafana
To import the grafana dashboard, click on the ➕ menu on the left panel and click ‘Import’.


Grafana Homepage
The following Page will open to import dashboard via id or panel json.


Import Grafana Dashboard
Now open the sample Grafana dashboard from URL https://grafana.com/dashboards/5955 and click the Copy the ID to Clipboard button. 📋


Paste the dashboard id on the grafana page.

And you will be redirected automatically to the dashboard setup.


Dashboard Setup
On the options section, click the InfluxDB and choose your influxdb server, then click Import button.

The dashboard will look like below.


Grafana Influxdb Dashboard — Id 5955
We have now successfully installed the TIG stack on Ubuntu! 😃
