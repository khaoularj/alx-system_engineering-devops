#this script create a file in /tmp with 0744 permission, owner and group are www-data, content is I love Puppet

file { '/tmp/school':
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I Love Puppet',
}
