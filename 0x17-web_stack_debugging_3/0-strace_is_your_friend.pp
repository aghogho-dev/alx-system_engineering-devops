# Define an exec resource to fix the WordPress issue


exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/',
  onlyif  => '/usr/bin/grep -q "phpp" /var/www/html/wp-settings.php',
  require => File['/var/www/html/wp-settings.php'],
}
