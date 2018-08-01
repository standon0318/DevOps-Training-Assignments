#redhat specific configuration

bash 'yum groupinstall Development tools' do
  user 'root'
  group 'root'
  code <<-EOC
    yum groupinstall "Development tools" -y
  EOC
  not_if 'yum grouplist installed | grep "Development tools"'
end
