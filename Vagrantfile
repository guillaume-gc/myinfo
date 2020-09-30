Vagrant.configure("2") do |config|
    config.vm.box = "hashicorp/bionic64"

    config.vagrant.plugins = ["vagrant-docker-compose"]

    config.vm.provision :docker
    config.vm.provision :docker_compose,
        yml: [
            "/vagrant/docker-compose.yml"
        ],
        rebuild: true,
        run: "always"

    config.vm.define 'myinfo-app-box' do |node|
        config.vm.network "private_network", type: "dhcp"
    end
end