# puppet script that increases nginx request limit

exec { 'ULIMIT':
  command => '/bin/sed -i "s/15/3000/g" /etc/default/nginx && /usr/sbin/service nginx restart'
}
