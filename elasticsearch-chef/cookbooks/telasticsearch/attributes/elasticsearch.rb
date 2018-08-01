# elasticsearch attributes

default['elasticsearch']['version'] = '2.1.1'
default['elasticsearch']['user'] = 'elasticsearch'
default['elasticsearch']['group'] = 'elasticsearch'
default['elasticsearch']['log_dir'] = '/var/log/elasticsearch'
default['elasticsearch']['pid_dir']  = '/var/run/'
default['elasticsearch']['home_dir'] = '/usr/share/elasticsearch'
default['elasticsearch']['config_dir'] = '/etc/elasticsearch'
default['elasticsearch']['data_dir'] = '/var/lib/elasticsearch'
default['elasticsearch']['default'] = '/etc/default'
default['elasticsearch']['loglevel']  = 'notice'
default['elasticsearch']['script_dir'] = '/etc/elasticsearch/scripts'
default['elasticsearch']['release_url'] = 'https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-:version:.tar.gz'


default['elasticsearch']['cluster_name'] = 'elasticsearch'
default['elasticsearch']['node_name'] = 'node-1'  											
default['elasticsearch']['ES_HEAP_SIZE'] = '512m'

# atttributes that will be loaded from or overidden according to environment

# ******************aws-monitoring-attributes********************

default['elasticsearch']['monitoring']['enable'] = true
default['elasticsearch']['monitoring']['image_id'] = nil
default['elasticsearch']['monitoring']['instance_id'] = nil
default['elasticsearch']['monitoring']['interval'] = ['*', '*', '*', '*', '*']

# ********************configuration-attributes**************************

default['elasticsearch']['path_repo'] = nil
default['elasticsearch']['aws_discovery']['access_key'] = nil
default['elasticsearch']['aws_discovery']['secret_key'] = nil

# **********************elasticsearch-config-to-be-used(set by environment)***********
default['elasticsearch']['config_source'] = 'dev-elasticsearch.conf.erb'

#*******************************cron-restart-elasticsearch-attributes************************************

default['elasticsearch']['cron']['monitoring_dir'] = '/etc/elasticsearch/monitoring'
default['elasticsearch']['cluster_check']['interval'] = ['*', '*', '*', '*', '*']
default['elasticsearch']['metric']['interval'] = ['*', '*', '*', '*', '*']



