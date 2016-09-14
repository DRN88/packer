## Synopsis
Packer is easy to use and automates the creation of any type of machine image. It embraces modern configuration management by encouraging you to use automated scripts to install and configure the software within your Packer-made images. Packer brings machine images into the modern age, unlocking untapped potential and opening new opportunities.

## Prerequisites
1. AWS S3 bucket dedicated to 'vmimport' process
2. AWS user with Key and Secret key with correct IAM Access
  * In 'iam' folder you need to apply those to your AWS user
  * http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/VMImportPrerequisites.html
3. Edit packer template json files
  * Set AWS Keys
  * Memory and CPU settings
  * ks.cfg settings
  * Use misc/genpw.py to generate a new hashed SHA-512 root password. Set this in ks.cfg

## Start Packer
```
cd packer-templates/centos-7-aws-virtualbox
packer build -force CentOS-7-x86_64-Minimal-1511-packer.json
```

## To install Virtualbox in VMWare infrastructure - WORKS
1. Enable Nested Virtualization  
  * http://docs.openstack.org/developer/devstack/guides/devstack-with-nested-kvm.html
  * Tick in VM's CPU Settings: "Expose hardware assisted virtualization to the guest OS"
  * Set VM's Guest OS to: Other, Other (64-bit)
2. Install kernel-devel package: ```yum -y install kernel-devel```
3. Install Virtualbox - https://www.virtualbox.org/wiki/Linux_Downloads
4. Run vboxconfig
5. Install Virtualbox Guest Additions
```
wget http://download.virtualbox.org/virtualbox/5.1.6/Oracle_VM_VirtualBox_Extension_Pack-5.1.6-110634.vbox-extpack
vboxmanage extpack install Oracle_VM_VirtualBox_Extension_Pack-5.1.6-110634.vbox-extpack
```

## Test if nested virtualization works
```
[root@lxbuilder01 CentOS7]# virt-host-validate
QEMU: Checking for hardware virtualization                                 : PASS
QEMU: Checking for device /dev/kvm                                         : PASS
QEMU: Checking for device /dev/vhost-net                                   : PASS
QEMU: Checking for device /dev/net/tun                                     : PASS
LXC: Checking for Linux >= 2.6.26                                          : PASS
[root@lxbuilder01 CentOS7]#
```

## To install QEMU KVM in VMWare infrastructure - DID NOT WORK USE VBOX
1. Use vSphere 6
2. Enable Nested Virtualization  
  * http://docs.openstack.org/developer/devstack/guides/devstack-with-nested-kvm.html
  * Tick in VM's CPU Settings: "Expose hardware assisted virtualization to the guest OS"
  * Set VM's Guest OS to: Other, Other (64-bit)
3. Install QEMU KVM
```
yum -y install qemu-kvm libvirt qemu-system-x86
```

## Todo
2. Have packer with Jenkins for better job management
