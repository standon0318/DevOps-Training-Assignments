#
# Cookbook:: elasticsearch
# Recipe:: default
#
# Copyright:: 2018, The Authors, All Rights Reserved.

# installs java8

bash 'install-java' do
  code <<-EOH
  cd /opt/
  sudo wget "#{node['java']['download']['url']}"
  sudo tar -xvf jdk-8u161-linux-x64.tar.gz
  sudo mv jdk1.8.0_161 /usr/lib/jvm/
  sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/jdk1.8.0_161//jre/bin/java 2000
  sudo update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/jdk1.8.0_161/bin/javac 2000
  EOH
  not_if { ::File.exist?("#{node['java']['jdk']['home']}") }
end
#create a group node for elasticsearch
#group node['elasticsearch']['group'] do
#  system  true
#  action  :create
#end

#Create a user which will run elasticsearch as a service
#user node['elasticsearch']['user'] do
#  system true
#  home node['elasticsearch']['home']
#  gid node['elasticsearch']['group']
#  shell '/bin/bash'
#  action :create
#  manage_home true
#end
#Download and install elasticsearch
bash 'download_and _install_elasticsearch' do
  code <<-EOH
  cd #{node['elasticsearch']['working']['directory']}
  sudo wget #{node['elasticsearch']['download']['url']}
  sudo wget "#{node['elasticsearch']['download']['checksum']}"
  shasum -a 512 -c elasticsearch-#{node['elasticsearch']['version']}.tar.gz.sha512
  mkdir -p elasticsearch
  tar -xvf elasticsearch-#{node['elasticsearch']['version']}.tar.gz
  sudo cp -a elasticsearch-#{node['elasticsearch']['version']}/. elasticsearch/
  sudo chown elasticsearch:elasticsearch  #{node['elasticsearch']['home']} -R
  sudo chmod 0755 #{node['elasticsearch']['home']} -R
  EOH
  not_if { ::File.exist?(node['elasticsearch']['home']) }
end

#setting environment path for elasticsearch and java
bash 'set_environment_variables' do
  code <<-EOH
    echo "export JAVA_HOME=#{node['java']['jdk']['home']}" >> /etc/bashrc
    echo "export JRE_HOME=#{node['java']['jre']['home']}" >> /etc/bashrc
    echo "export Elasticsearch_Home=#{node['elasticsearch']['home']}" >> /etc/bashrc
    echo "export PATH=\\$PATH:$JAVA_HOME/bin:\\$JRE_HOME/bin:\\$Elasticsearch_HOME/bin" >> /etc/bashrc
    source /etc/bashrc
  EOH
  not_if { ::File.exist?(node['elasticsearch']['home']) }
end

#Give Read,Write and Exceute permissions to elasticsearch user on elasticsearch directories
bash 'make_data_directories_and_change_permissions' do
  code <<-EOH
    sudo mkdir #{node['elasticsearch']['directory']['data']}
    sudo mkdir #{node['elasticsearch']['directory']['data']}/data
    sudo mkdir #{node['elasticsearch']['directory']['log']}
    

    sudo chown elasticsearch:elasticsearch #{node['elasticsearch']['directory']['data']}/data -R
    sudo chown elasticsearch:elasticsearch #{node['elasticsearch']['directory']['log']} -R
	   
	sudo chmod 0777 #{node['elasticsearch']['directory']['data']} -R
    sudo chmod 0777 #{node['elasticsearch']['directory']['data']}/data -R
   sudo chmod 0777 #{node['elasticsearch']['directory']['log']} -R
    
 
 EOH
end

#Create a directory for keeping all the python scripts related to elasticsearch
directory 'create directory for python script' do
  path node['python']['scripts']['directory']
	mode '0755'
  action :create
#  not_if { ::File.exist?(node['python']['scripts']['directory']) }
end

#copying python script from cookbook 
cookbook_file 'Put python script files into script directory' do
  path "#{node['python']['scripts']['directory']}/ClusterIp.py"
  source 'ClusterIp.py'
  action :create
#  not_if { ::File.exist?("#{node['python']['scripts']['directory']}/ClusterIp.py") }
end

#Overriding elasticsearch.yaml to our desired settings
template "#{node['elasticsearch']['directory']['conf']}"+"/elasticsearch.yml" do
  source 'elasticsearch.yaml.erb'
end

#To install ec2 discovery plugin
bash 'download_and_install_elasticsearch_plugin' do
  code <<-EOH
    cd #{node['elasticsearch']['home']}

    sudo wget #{node['ec2plugin']['download']['url']}

   sudo bin/elasticsearch-plugin -y  install file:///opt/elasticsearch/discovery-ec2-6.3.1.zip
  EOH
  not_if { ::File.exist?(node['elasticsearch']['home']) }
end

#Populating seeds(all nodes in cluster) ipaddress in elasticsearch.yaml
#bash "Get_IP_address" do
#  code <<-EOH
#    sudo pip-2.7 install boto3
#	  ipaddress=$(curl http://169.254.169.254/latest/meta-data/local-ipv4)
#    instance_id=$(curl http://169.254.169.254/latest/meta-data/instance-id)
#    cd #{node['python']['home']}
#	  SeedIps=$(sudo python2.7 #{node['python']['scripts']['directory']}/ClusterIp.py $instance_id 2>&1) 
#  EOH
#end

#Opening port 9003 for communication among nodes in cluster
#Opening port 9000 for communication of load balancer with nodes
#save iptables rules 
bash 'open_ports_for_elasticsearch_service' do
  code <<-EOH
    iptables -A INPUT -p tcp -m tcp --dport #{node['elasticsearch']['internode']['communication']['port']} -j ACCEPT
    iptables -A INPUT -p tcp -m tcp --dport #{node['elasticsearch']['client']['port']} -j ACCEPT
    /sbin/service iptables save
  EOH
end

#Create a service elasticsearch
service "elasticsearch" do
  supports :restart => true, :start => true, :stop => true, :reload => true
  action :nothing
end 

#creating a service file in /etc/init.d/elasticsearch
template '/etc/init.d/elasticsearch' do
  source 'elasticsearch.erb'
  mode '0755'
  owner 'elasticsearch'
  notifies :enable, 'service[elasticsearch]'
  notifies :start, 'service[elasticsearch]' 
end
