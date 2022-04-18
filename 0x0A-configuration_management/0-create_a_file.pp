#Using Puppet, create a file in /tmp
file { '0-create_a_file':
  ensure  => 'present',
  path    => '/tmp/school',
  mode    => '0744',
  content => 'I love Puppet',
  group   => 'www-data',
  owner   => 'www-data',
}

