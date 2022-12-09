# Create a manifest that kills a process named killmenow

exec { 'pkill':
  path    =>  '/usr/local/bin/:/bin/',
  command =>  'pkill killmenow'
}
