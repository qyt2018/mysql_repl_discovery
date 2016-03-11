# mysql_repl_discovery

A simple tool for discover MySQL replication topology.

##  DEPENDENCIES
```
DBI
DBD::mysql
perl-TermReadKey (if enable askpass option)
```

## How to use

Read more with ```perldoc repl_discovery``` or ```perl repl_discovery --help```

  `repl_discovery` can get the master, slave status,  common info(server_id, binlog, filter ...) 
and check repl health.

Notice: Current version don't support different port in master and slaves.

# RPM

`repl_discovery.spec`

##TODO

1. master and slave have different port( not support ).

# Usage

### hostname:
`
cz-test2: 10.0.21.7  (slave)
cz-test3: 10.0.21.17 (master)
`
specify master or slave ip address or hostname
```
$ perl repl_discovery --host 10.0.21.17 --port 3303 --user monitor --askpass
Enter password : 
+-10.0.21.17:3303
version             5.5.36-34.1-rel34.1-log
server_id           68839
has_gtid            Not Support
binlog_enable       1
filter              binlog_ignore_db: information_schema,mysql,performance_schema,test; 
binlog_format       ROW
max_packet          32MB
read_only           0
  +-10.0.21.7:3303
  version             5.5.36-34.1-rel34.1-log
  server_id           462055
  has_gtid            Not Support
  binlog_enable       1
  filter              replicate_ignore_db: information_schema,mysql,performance_schema,test; 
  binlog_format       ROW
  max_packet          32MB
  read_only           1
  repl_check          OK
$ perl repl_discovery --host 10.0.21.7 --port 3303 --user monitor --askpass
Enter password : 
+-10.0.21.17:3303
version             5.5.36-34.1-rel34.1-log
server_id           68839
has_gtid            Not Support
binlog_enable       1
filter              binlog_ignore_db: information_schema,mysql,performance_schema,test; 
binlog_format       ROW
max_packet          32MB
read_only           0
  +-10.0.21.7:3303
  version             5.5.36-34.1-rel34.1-log
  server_id           462055
  has_gtid            Not Support
  binlog_enable       1
  filter              replicate_ignore_db: information_schema,mysql,performance_schema,test; 
  binlog_format       ROW
  max_packet          32MB
  read_only           1
  repl_check          OK
```

## changelog:

v0.1.0: init version

v0.1.1: recurion find top master;
        support hierarchical level check;
        support multi master check;

