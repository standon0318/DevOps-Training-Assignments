require 'chefspec'

describe 'Docker_Redis Container::default' do
  let(:chef_run) { ChefSpec::SoloRunner.new(platform: 'centos', version: '7.4.1708').converge(described_recipe) }
   it 'installs a package with the default action' do
    expect(chef_run).to install_package('docker')
	end  
     it 'enables a service with an explicit action' do
    expect(chef_run).to enable_service('docker')
  end
    it 'starts a service with an explicit action' do
    expect(chef_run).to start_service('docker')
  end
  context 'testing default action, default properties' do
    it 'pulls docker_image[redis]' do
      expect(chef_run).to pull_docker_image('redis').with(
        
        repo: 'redis',
       
        tag: '3.2.11',
      
      )
    end
  end
  context 'testing create action' do
    it 'create docker_container[redis-container]' do
      expect(chef_run).to create_docker_container('redis-container').with(
        
        container_name: 'redis-container',
        repo: 'redis',
        tag: '3.2.11',
        detach: true,
      port: "6379:6379"
      )
    end
  end
end