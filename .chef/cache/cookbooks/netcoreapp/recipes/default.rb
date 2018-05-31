#
# Cookbook:: netcoreapp
# Recipe:: default
#
# Copyright:: 2018, The Authors, All Rights Reserved.
aws_s3_file '/home/project.tar.gz' do
  bucket 'trainee-dotnetcore'
  remote_path 'artifacts1.0.tar.gz'
 region 'us-east-1' 
 action :create_if_missing
end
bash 'extract_some_tar' do
code <<-EOH 
sudo cp /home/project.tar.gz /opt/app
cd opt/app/
tar xzvf project.tar.gz
cd 
sudo su root
dotnet /opt/app/project/bin/Release/netcoreapp2.0/project.dll
EOH
end

