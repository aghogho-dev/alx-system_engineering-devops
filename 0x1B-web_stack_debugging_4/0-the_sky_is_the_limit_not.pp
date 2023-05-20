# Sky is the limit

exec { 'fix--for-nginx':
  command => 'sed -i "s/worker_connections\s*\(.*\)/worker_connections 2000;/g" /etc/nginx/nginx.conf',
  path    => '/bin:/usr/bin',
} ->

# Restart Nginx
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/bin:/usr/bin',
}

