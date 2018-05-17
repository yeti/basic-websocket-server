# -*- mode: ruby -*-
# vi: set ft=ruby :


Vagrant.configure("2") do |config|
  config.vm.provider "docker"

  config.vm.box = "tknerr/baseimage-ubuntu-16.04"

  config.vm.network "forwarded_port", guest: 8766, host:8766
  config.vm.network "forwarded_port", guest: 8768, host:8768

  config.vm.synced_folder "./src", "/server"

  config.vm.provision "shell",
    inline: ". /server/setup/setup.sh"
end
