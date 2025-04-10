Vagrant.configure("2") do |config|
  ENV['VAGRANT_SERVER_URL'] = 'https://vagrant.elab.pro'

  config.vm.box = "almalinux/9"
  config.vm.hostname = "prometheus-vm"
  config.vm.network "forwarded_port", guest: 8080, host: 8080

  config.vm.provider "virtualbox" do |vb|
    vb.gui = true                      
    vb.memory = "4096"                 
    vb.cpus = 2                        
    vb.customize ["modifyvm", :id, "--vram", "64"]  
  end

  config.vm.provision "ansible_local" do |ansible|
    ansible.playbook = "/vagrant/ansible/playbook.yml"
  end
end