#
# Cookbook:: filewrite
# Recipe:: default

# Copyright:: 2018, The Authors, All Rights Reserved
package 'docker' do
	action :install
	not_if 'docker --version'
end
service 'docker' do
	action [:enable, :start]
	not_if 'service docker status'
end

docker_image 'redis' do
	tag 'latest'
	action :pull
end
docker_container 'redis-container' do
	image 'redis'
	container_name 'redis-container'
	detach true
	port '6379:6379'
	action :create
end
execute 'docker_status' do
	command 'docker ps -a'
end
