#!/usr/bin/env bash
#using Puppet to make changes to our configuration file
#SSH client configuration must be configured to use the private key ~/.ssh/school
#SSH client configuration must be configured to refuse to authenticate using a password

file {'etc/ssh/ssh_config':
  ensure  => file,
  content =>'
    Host *
    PasswordAuthentication no
    IdentityFile ~/.ssh/school'
}
