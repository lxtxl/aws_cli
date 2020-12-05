#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-instance-read-replica.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # db-instance-identifier : The DB instance identifier of the read replica. This identifier is the unique key that identifies a DB instance. This parameter is stored as a lowercase string.
    # source-db-instance-identifier : The identifier of the DB instance that will act as the source for the read replica. Each DB instance can have up to five read replicas.
Constraints:

Must be the identifier of an existing MySQL, MariaDB, Oracle, PostgreSQL, or SQL Server DB instance.
Can specify a DB instance that is a MySQL read replica only if the source is running MySQL 5.6 or later.
For the limitations of Oracle read replicas, see Read Replica Limitations with Oracle in the Amazon RDS User Guide .
For the limitations of SQL Server read replicas, see Read Replica Limitations with Microsoft SQL Server in the Amazon RDS User Guide .
Can specify a PostgreSQL DB instance only if the source is running PostgreSQL 9.3.5 or later (9.4.7 and higher for cross-region replication).
The specified DB instance must have automatic backups enabled, that is, its backup retention period must be greater than 0.
If the source DB instance is in the same AWS Region as the read replica, specify a valid DB instance identifier.
If the source DB instance is in a different AWS Region from the read replica, specify a valid DB instance ARN. For more information, see Constructing an ARN for Amazon RDS in the Amazon RDS User Guide . This doesnât apply to SQL Server, which doesnât support cross-region replicas.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("rds", "create-db-instance-read-replica", "db-instance-identifier", "source-db-instance-identifier", add_option_dict)
