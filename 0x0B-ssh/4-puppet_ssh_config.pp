# Create changes with puppet
file_line {'Turn off passwd auth':
  path   => '/etc/ssh/ssh_config',
  ensure => 'present',
  line   => '    ForwardAgent yes '
}

file_line {'Declare identity file':
  path   => '/etc/ssh/ssh_config',
  ensure => 'present',
  line   => '    IdentityFile ~/.ssh/holberton'
}


