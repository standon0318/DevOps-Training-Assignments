import os
import os.path
import commands
from elasticsearch import Elasticsearch
import sys
import datetime
import urllib2
import threading
import boto.ec2.cloudwatch
import time
from boto.ec2.cloudwatch import CloudWatchConnection

def checkClusterStatus():
	es = Elasticsearch()
	cluster_status = es.cluster.health()
	status = cluster_status['status']
	return status
	
def __sendToCloudWatch(instanceId,hostname,ipv4,val):
	profileName = 'Oski-Cloudwatch'
	from boto import Config
	cfg = Config()
	regionName = cfg.get_value('profile ' + str(profileName), 'oski_region_name')  
	cwc = boto.ec2.cloudwatch.connect_to_region(regionName, profile_name = profileName)
	metricData = dict({'InstanceId' : instanceId,'Machine' : hostname,'IP' : ipv4})
	dateutc = datetime.datetime.utcnow()
	print metricData
	print val
	cwc.put_metric_data(namespace="Production Service Monitor",name="Elastic Search Cluster Status  ",unit="Count",value=val, timestamp=dateutc, dimensions=metricData,)
	print cwc		
	
def main(argv=None):
	status = checkClusterStatus()
	print status
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
		if(status != 'green'):
			val = 1.0	
			__sendToCloudWatch(instanceId,hostname,ipv4,val)
		else:
			val = 0.0	
			__sendToCloudWatch(instanceId,hostname,ipv4,val)
	except:
		print(sys.exc_info())
		pass
	


if __name__ == "__main__":
    main()

