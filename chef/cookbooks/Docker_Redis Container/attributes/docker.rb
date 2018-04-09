default['Docker_Redis Container']['package']['name'] = "docker"
default['Docker_Redis Container']['package']['version'] = "17.12.1ce-1.135.amzn1"
default['Docker_Redis Container']['service']['name'] = "docker"
default['Docker_Redis Container']['docker_image']['name'] = "redis"
default['Docker_Redis Container']['docker_image']['tag'] = "3.2.11"
default['Docker_Redis Container']['docker_container']['name'] = "redis-container"
default['Docker_Redis Container']['docker_container']['image'] = "redis"
default['Docker_Redis Container']['docker_container']['tag'] = "3.2.11"
default['Docker_Redis Container']['docker_container']['container_name'] = "redis-container"
default['Docker_Redis Container']['docker_container']['detach'] = true
default['Docker_Redis Container']['docker_container']['port'] = "6379:6379"


