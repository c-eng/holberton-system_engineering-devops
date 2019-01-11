# Puppet manifest to terminate the killmenow process
exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => '/usr/bin'
}
