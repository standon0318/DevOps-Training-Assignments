#default linux recipe

require 'chef/log'
Chef::Log.level = :debug

case node['platform']
when 'centos'
  include_recipe 'telasticsearch::redhat'
when 'ubuntu'
  include_recipe 'telasticsearch::debian'
end

if node['linux']['ulimit']['enable']
  user_ulimit node['linux']['ulimit']['user'] do
    filehandle_limit node['linux']['ulimit']['filehandlers']
    filehandle_soft_limit node['linux']['ulimit']['filehandlers']
    filehandle_hard_limit node['linux']['ulimit']['filehandlers']
  end
end