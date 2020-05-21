# A puppet script that resolves why Apache is returning a 500 error 

exec { 'fix_ext':
    command => '/bin/sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php'
}
