# elasticsearch recipe to install from source

include_recipe 'telasticsearch'

group node['elasticsearch']['group'] do
  system  true
  action  :create
end

user node['elasticsearch']['user'] do
  gid     node['elasticsearch']['user']
  system  true
  shell   '/bin/false'
  action  :create
end

directories = [node['elasticsearch']['home_dir'],
                node['elasticsearch']['config_dir'],
                node['elasticsearch']['log_dir'],
								node['elasticsearch']['data_dir'],
								node['elasticsearch']['script_dir'],
								node['elasticsearch']['cron']['monitoring_dir']]

directories.each do |dir|
  directory dir do
    owner     node['elasticsearch']['user']
    group     node['elasticsearch']['group']
    mode      '0755'
    recursive true
    action    :create
  end
end

release_url = node['elasticsearch']['release_url']
release_url.gsub!(/:version:/, node['elasticsearch']['version'])

release_file = ::File.join("#{Chef::Config['file_cache_path']}", \
                release_url[release_url.rindex('/') +1, \
                release_url.length - release_url.rindex('/')])
								
remote_file release_file do
  source  release_url
  mode    '0755'
  action  :create_if_missing
end

bash 'Extract-tar-to-home-directory' do
  user  node['elasticsearch']['user']
  group node['elasticsearch']['group']
  cwd   node['elasticsearch']['home_dir']
  code <<-EOC
    tar zxf #{release_file} -C #{node['elasticsearch']['home_dir']} --strip-components=1
		rm -rf #{node['elasticsearch']['home_dir']}/config
  EOC
end

bash 'elasticsearch-plugin-install' do
	code <<-EOC
		#{node['elasticsearch']['home_dir']}/bin/plugin install mobz/elasticsearch-head
		#{node['elasticsearch']['home_dir']}/bin/plugin install cloud-aws
	EOC
end

remote_directory node['elasticsearch']['cron']['monitoring_dir'] do
  source 'monitoring'
  owner 'root'
  group 'root'
  mode '0755'
  action :create
end

bag_item = Chef::EncryptedDataBagItem.load('aws_secret', 'elasticsearch_discovery')
node.default['elasticsearch']['aws_discovery']['access_key'] = bag_item[node.chef_environment]['AWSAccessKeyId']
node.default['elasticsearch']['aws_discovery']['secret_key'] = bag_item[node.chef_environment]['AWSSecretKey']

template ::File.join("#{node['elasticsearch']['config_dir']}",'elasticsearch.yml') do
  source    node['elasticsearch']['config_source']
  owner     node['elasticsearch']['user']
  group     node['elasticsearch']['group']
  mode      '0644'
  variables 'elasticsearch' => node['elasticsearch']
  action    :create
end

template ::File.join("#{node['elasticsearch']['config_dir']}",'logging.yml') do
  source    'logging.conf.erb'
  owner     node['elasticsearch']['user']
  group     node['elasticsearch']['group']
  mode      '0644'
  variables 'elasticsearch' => node['elasticsearch']
  action    :create
end


if (node['platform'] == 'ubuntu' && node['platform_version'].to_f <= 14.04)

  template '/etc/init/elasticsearch.conf' do
    source  'elasticsearch.upstart.conf.erb'
    owner   'root'
    group   'root'
    mode    '0644'
    action  :create
  end

  service 'elasticsearch' do
    provider  Chef::Provider::Service::Upstart
    supports  :restart => true, :start => true, :stop => true, :status => true
    action    [:enable, :start]
  end

elsif (node['platform'] == 'ubuntu' && node['platform_version'].to_f > 14.04) \
    || (node['platform'] == 'centos' && node['platform_version'].to_f >= 7.0)

  template '/usr/lib/systemd/system/elasticsearch.service' do
    source  'elasticsearch.systemd.service.erb'
    owner   'root'
    group   'root'
    mode    '0644'
    action  :create
  end

  service 'elasticsearch' do
    provider  Chef::Provider::Service::Redhat
    supports  :restart => true, :start => true, :stop => true, :status => true
    action    [:enable, :start]
  end

else
  Chef.Log.warn 'elasticsearch: update linux INIT system.'
end

cron 'elasticsearch-health-metric' do
  user node['elasticsearch']['user']
  minute node['elasticsearch']['metric']['interval'][0]
  hour node['elasticsearch']['metric']['interval'][1]
  day node['elasticsearch']['metric']['interval'][2]
	month node['elasticsearch']['metric']['interval'][3]
  weekday node['elasticsearch']['metric']['interval'][4]
  command  "#{node['elasticsearch']['cron']['monitoring_dir']}/ElasticMetric.sh >> #{node['elasticsearch']['cron']['monitoring_dir']}/ElasticMetric.log"
	only_if {File.exists?("#{node['elasticsearch']['cron']['monitoring_dir']}/ElasticMetric.sh")}
  action :create
end

cron 'elasticsearch-cluster-check-status' do
  user node['elasticsearch']['user']
  minute node['elasticsearch']['cluster_check']['interval'][0]
  hour node['elasticsearch']['cluster_check']['interval'][1]
  day node['elasticsearch']['cluster_check']['interval'][2]
	month node['elasticsearch']['cluster_check']['interval'][3]
  weekday node['elasticsearch']['cluster_check']['interval'][4]
  command  "#{node['elasticsearch']['cron']['monitoring_dir']}/ElasticClusterCheck.sh >> #{node['elasticsearch']['cron']['monitoring_dir']}/ElasticClusterCheck.log"
	only_if {File.exists?("#{node['elasticsearch']['cron']['monitoring_dir']}/ElasticClusterCheck.sh")}
  action :create
end


if node['elasticsearch']['monitoring']['enable']
  tlinux_sysmonitor_sysmonitor 'elasticsearch-system-monitoring' do
    image_id      node['elasticsearch']['monitoring']['image_id']
    instance_id   node['elasticsearch']['monitoring']['image_id']
    interval      node['elasticsearch']['monitoring']['interval']
    user          node['elasticsearch']['user']
    target_path   node['elasticsearch']['home_dir']
    action        [:create, :run]
  end
end




