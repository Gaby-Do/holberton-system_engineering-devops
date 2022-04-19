#using Puppet change the configuration file. Just as in the previous configuration file task, set up client SSH configuration file so that it can connect to a server without typing a password.
file { '/etc/ssh/ssh_config':
  ensure  => 'present',
  mode    => '0744',
  content => 'Host * \n PasswordAuthentication no \n IdentityFile ~/.ssh/school',
  group   => 'root',
  owner   => 'root',
}

