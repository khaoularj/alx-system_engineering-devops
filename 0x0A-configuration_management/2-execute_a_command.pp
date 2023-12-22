#execute the command pkill using puppet

exec {'pkill':
  command => 'pkill killmenow',
  provider => 'shell',
}
