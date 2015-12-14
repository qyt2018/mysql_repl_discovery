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

Notice: Current version don't support different port in master and slaves.

##TODO

1. master and slave have different port.

## changelog:

v0.1.0: init version

v0.1.1: recurion find top master;
        support hierarchical level check;
        support multi master check;

