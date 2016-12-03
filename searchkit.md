#Project Setup
ddd
* Reason 1
* Reason 2
* Reason 3

###1. Provision VM
Installed:
```
slcli vs create --datacenter=sjc01 --domain=finalProject.com --hostname=yt_8m --os=CENTOS_LATEST_64 --cpu=2 --memory=4096 --billing=hourly --disk=100 --key=<mykey>
```
###2. Install pre-requisites

```
yum install -y epel-release && yum install -y java-1.8.0-openjdk-headless net-tools jq
```
Set the proper location of JAVA_HOME and test it:

```
echo export JAVA_HOME=\"$(readlink -f $(which java) | grep -oP '.*(?=/bin)')\" >> /root/.bash_profile
source /root/.bash_profile
$JAVA_HOME/bin/java -version
```

Download the Elasticsearch tarball:

```
curl -OL https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-1.7.0.tar.gz
tar xzf elasticsearch-1.7.0.tar.gz

```

###3. Install python libraries
```
yum -y update
yum -y install python-pip
```
And install everything you need to run this code.

```
python yt_8m2es.py
```
###3. Install cool UI from class

```
bin/plugin install jettro/elasticsearch-gui 
```

Go to my web browser and type this `http://198.23.84.123:9200/_plugin/gui/index.html`.

###4. Set-up Searchkit







