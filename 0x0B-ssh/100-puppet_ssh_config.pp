# Client side config with Puppet

file { '/etc/ssh/ssh_config':
  ensure  => present,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => template('/home/ubuntu/alx-system_engineering-devops/0x0B-ssh/ssh_config.erb'),
}
