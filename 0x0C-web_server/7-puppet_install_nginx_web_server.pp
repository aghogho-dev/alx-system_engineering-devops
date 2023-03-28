class nginx {
  package { 'nginx':
    ensure => 'installed',
  }

  service { 'nginx':
    ensure => 'running',
    enable => true,
  }

  file { '/etc/nginx/html/index.html':
    content => "Hello World!\n",
    mode    => '0744',
    owner   => 'root',
    group   => 'root',
  }

  file { '/etc/nginx/sites-available/default':
    content => "server {
                  listen 80;
                  root /etc/nginx/html;
                  index index.html;
                  location /redirect_me {
                    return 301 https://www.google.com/;
                  }
                }",
    mode    => '0744',
    owner   => 'root',
    group   => 'root',
    notify  => Service['nginx'],
  }

  file { '/etc/nginx/sites-enabled/000-default':
    ensure  => 'link',
    target  => '/etc/nginx/sites-available/default',
    require => File['/etc/nginx/sites-available/default'],
  }
}

include nginx

