# Create changes with puppet at ssh_config
file_line {'Turn off passwd auth':
  path   => '/etc/ssh/ssh_config',
  ensure => 'present',
  line   => '    PasswordAuthentication no'
}

file_line {'Declare indentity file':
  path   => '/etc/ssh/ssh_config',
  ensure => 'present',
  line   => '    IdentityFile ~/.ssh/holberton'
}