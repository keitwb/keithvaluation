# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # All Vagrant configuration is done here. The most common configuration
  # options are documented and commented below. For a complete reference,
  # please see the online documentation at vagrantup.com.

  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "ubuntu/trusty64"

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  config.vm.network "forwarded_port", guest: 80, host: 18080
  config.vm.network "forwarded_port", guest: 443, host: 18443

  config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyvm", :id, "--memory", "2048"]
    vb.customize ["modifyvm", :id, "--cpus", "2"]
  end

  config.vm.synced_folder ".", "/srv/keithvaluation", :mount_options => ['uid=0','gid=0']

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "ansible/playbook.yml"
    ansible.sudo = true
    #ansible.verbose = 'vvvv'
    ansible.extra_vars = {
      ansible_ssh_user: 'vagrant',
      clone_repo: false,
      app_hostname: 'kv.dev',
      admin_hostname: 'kv-admin.dev',
      admin_users: [
        {
          :username => 'ben.keith',
          :email => 'keitwb@gmail.com',
          :first_name => 'Ben',
          :last_name => 'Keith',
          :password => 'valuation',
        }
      ]
    }
    ansible.vault_password_file = '../ansible-key'
    #ansible.raw_arguments = ['--tags', 'debug']
  end
end
