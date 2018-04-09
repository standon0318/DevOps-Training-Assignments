
# Cookbook:: Docker_Redis Container
# Recipe:: default


#using  docker cookbook for reference
#github path for docker cookbook https://github.com/chef-cookbooks/docker.git

#getting docker package and installing
package node['Docker_Redis Container']['package']['name'] do
	version node['Docker_Redis Container']['package']['version']
	action :install
end

#Starting docker service
service ['Docker_Redis Container']['service']['name'] do
	action [:enable, :start]
end

#pulling redis-container for docker 
docker_image node['Docker_Redis Container']['docker_image']['name'] do
	tag node['Docker_Redis Container']['docker_image']['tag']
	action :pull
end

#install redis from redis image
docker_container node['Docker_Redis Container']['docker_container']['name'] do
	image node['Docker_Redis Container']['docker_container']['image']
	container_name node['Docker_Redis Container']['docker_container']['container_name']
	detach node['Docker_Redis Container']['docker_container']['detach']
	port node['Docker_Redis Container']['docker_container']['port']
	action :create
end

