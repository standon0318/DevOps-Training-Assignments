#debian specific configuration

execute 'update-apt' do
  command 'apt-get update'
  action  :run
end

package 'build-essential' do
  action :install
end

package 'git-core' do
  action :install
  ignore_failure true
end
