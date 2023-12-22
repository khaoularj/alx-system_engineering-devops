#execute the command pkill using puppet

exec {'killmenow':
  command => 'pkill killmenow',
}
