#automate the task of creating a custom HTTP header response with Puppet

package { 'nginx':
  ensure => installed,
}

Facter.add('server_hostname') do
  setcode 'hostname'
end

file { '/etc/nginx/sites-available/custom-header':
  ensure  => 'present',
  content => "
    server {
      listen 80 default_server;
      server_name _;

      location / {
        add_header X-Served-By $hostname;
	}
}
}

file { '/etc/nginx/sites-enabled/custom-header':
  ensure => 'link',
  target => '/etc/nginx/sites-available/custom-header',
}

service { 'nginx':
  ensure    => 'running',
  subscribe => File['/etc/nginx/sites-available/custom-header'],
}
