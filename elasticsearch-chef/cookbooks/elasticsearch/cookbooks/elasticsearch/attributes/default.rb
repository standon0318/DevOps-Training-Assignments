#Java Installation Attributes
default['java']['jdk']['home'] = '/usr/lib/jvm/jdk1.8.0_161'
default['java']['jre']['home'] = '/usr/lib/jvm/jdk1.8.0_161/jre'
default['java']['download']['url'] = 'https://s3.amazonaws.com/kenobi-packages/jdk-8u161-linux-x64.tar.gz'

#Elasticsearch installation
default['elasticsearch']['home'] = '/opt/elasticsearch'
default['elasticsearch']['user'] = 'elasticsearch'
default['elasticsearch']['group'] = 'elasticsearch'
default['elasticsearch']['version'] = '6.3.2'
default['elasticsearch']['download']['url'] = "https://s3.amazonaws.com/kenobi-packages/elasticsearch-6.3.1.tar.gz"
default['elasticsearch']['download']['checksum'] = "https://s3.amazonaws.com/kenobi-packages/elasticsearch-6.3.1.tar.gz.sha512"
default['elasticsearch']['working']['directory'] = '/opt'


# elasticsearch logs,data and config folder
default['elasticsearch']['directory']['data'] = '/var/lib/elasticsearch'
default['elasticsearch']['directory']['log'] = '/var/log/elasticsearch'
default['elasticsearch']['directory']['conf'] = "#{node['elasticsearch']['home']}/conf"

#elasticsearch related python script directory
default['python']['scripts']['directory'] = '/opt/PythonScript'

#ec2discovery plugin installation
default['ec2plugin']['download']['url'] = 'https://s3.amazonaws.com/kenobi-packages/discovery-ec2-6.3.2.zip'

#Elasticsearch Ports Usage
default['elasticsearch']['internode']['communication']['port'] = '9003'
default['elasticsearch']['client']['port'] = '9000'

#Elasticsearch Service Installation Attributes
default['elasticsearch']['service']['pid']['path'] = '/var/run/elasticsearch/'
default['elasticsearch']['service']['MAXOPENFILE'] = '65536'
default['elasticsearch']['service']['LockFile'] = '/var/lock/subsys/$prog'
default['elasticsearch']['service']['MAX_LOCKED_MEMORY'] = 'unlimited'
default['elasticsearch']['service']['LimitMEMLOCK'] = 'infinity'
default['elasticsearch']['service']['Restart'] = 'always'
default['elasticsearch']['service']['path'] = '/etc/systemd/system/elasticsearch.service'


#Elasticsearch Config 
default['elasticsearch']['cluster_name'] = 'travel-qa-elasticsearch'