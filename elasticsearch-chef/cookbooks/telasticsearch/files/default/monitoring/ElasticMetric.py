#! /usr/bin/python2.7 -tt

import os
import os.path
import commands
import sys
import datetime
import urllib2
import threading
import boto.ec2.cloudwatch
import time
from boto.ec2.cloudwatch import CloudWatchConnection


def __sendToCloudWatch(instanceId,hostname, ipv4):
	profileName = 'Oski-Cloudwatch'
	from boto import Config
	cfg = Config()
	regionName = cfg.get_value('profile ' + str(profileName), 'oski_region_name')  
	cwc = boto.ec2.cloudwatch.connect_to_region(regionName, profile_name = profileName)

	CONSOLE_DEBUG = True
	status_running = False
	SERVICE_START_CMD = 'sudo service elasticsearch start'
	STATSD_CHECK_CMD = 'sudo service elasticsearch status'
	PIDFILE = "/var/run/elasticsearch.pid"
	metricData = dict({'InstanceId' : instanceId,'Machine' : hostname,'IP' : ipv4})
	dateutc = datetime.datetime.utcnow()

	if os.path.isfile(PIDFILE) :
		print 'Pid file exists!'
		(rc, output) = commands.getstatusoutput(STATSD_CHECK_CMD)
		print 'cmd: ', STATSD_CHECK_CMD
		print 'rc: ', rc
		if '* elasticsearch is running' in output:
			print 'out: ', output
			status_running = True
			print 'elasticsearch running'
			cwc.put_metric_data(namespace="Production Service Monitor",name="ElasticSearch healthy",unit="Count",value=1.0, timestamp=dateutc, dimensions=metricData,)
		else :
			status_running = False
	else :
		status_running = False

	if not status_running:
    		(rc, output) = commands.getstatusoutput(SERVICE_START_CMD)
	      	print 'cmd: ', SERVICE_START_CMD
	       	print 'rc: ', rc
       		print 'out: ', output
		time.sleep(10)
		(rc, output) = commands.getstatusoutput(STATSD_CHECK_CMD)
		print 'cmd: ', STATSD_CHECK_CMD
		print 'rc: ', rc
		if '* elasticsearch is running' in output:
			print 'out: ', output
			cwc.put_metric_data(namespace="Production Service Monitor",name="ElasticSearch restarted",unit="Count",value=1.0, timestamp=dateutc, dimensions=metricData,)
		else:
			cwc.put_metric_data(namespace="Production Service Monitor",name="ElasticSearch unhealthy",unit="Count",value=1.0, timestamp=dateutc, dimensions=metricData,)

def main(argv=None):
	tempFile = '/tmp/Cloud.info'
    	try:
        	hostname = 'AWS-EC2'
	        ipv4 = '127.0.0.1'
        	instanceId = 'Unknown'

		if os.path.exists(tempFile) == True:
			fileCreateTime = datetime.datetime.fromtimestamp(os.path.getctime(tempFile))
			checkTime = datetime.datetime.now() - datetime.timedelta(hours=1)
			if (checkTime > fileCreateTime):
				os.remove(tempFile)

		if os.path.exists(tempFile) == False:			
			try:
				instanceId = urllib2.urlopen("http://169.254.169.254/latest/meta-data/instance-id").read()
				hostname = urllib2.urlopen("http://169.254.169.254/latest/meta-data/hostname").read()
				ipv4 = urllib2.urlopen("http://169.254.169.254/latest/meta-data/local-ipv4").read()
				file = open(tempFile,'w+')
				file.write(str(instanceId) + '\n')        
				file.write(str(hostname) + '\n')        
				file.write(str(ipv4) + '\n')             
				file.close()		
			except:
				pass
		else :
			file = open(tempFile,'r')
			lst = file.readlines()
			instanceId = lst[0].strip()
			hostname = lst[1].strip()
			ipv4 = lst[2].strip()
			file.close()

		__sendToCloudWatch(instanceId,hostname,ipv4)
	except:
      	  print(sys.exc_info())
     	  pass

if __name__ == "__main__":
    main()
