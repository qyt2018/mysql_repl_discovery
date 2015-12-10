# mysql_repl_discovery

A simple tool for discover MySQL replication topology.

##  DEPENDENCIES
```
DBI
DBD::mysql
```

## How to use

Read more with ```perldoc repl_discovery``` or ```perl repl_discovery --help```

  `repl_discovery` can get the master, slave status,  common info(server_id, binlog, filter ...) 
and check repl health.

## Todo

 1. Multi master check
 2. hierarchical level check
