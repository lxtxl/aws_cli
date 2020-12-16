#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-instance.html
if __name__ == '__main__':
    """
	delete-db-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-instance.html
	describe-db-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-instances.html
	modify-db-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-instance.html
	reboot-db-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/reboot-db-instance.html
	start-db-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/start-db-instance.html
	stop-db-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/stop-db-instance.html
    """

    parameter_display_string = """
    # db-instance-identifier : The DB instance identifier. This parameter is stored as a lowercase string.
Constraints:

Must contain from 1 to 63 letters, numbers, or hyphens.
First character must be a letter.
Canât end with a hyphen or contain two consecutive hyphens.

Example: mydbinstance
    # db-instance-class : The compute and memory capacity of the DB instance, for example, db.m4.large . Not all DB instance classes are available in all AWS Regions, or for all database engines. For the full list of DB instance classes, and availability for your engine, see DB Instance Class in the Amazon RDS User Guide.
    # engine : The name of the database engine to be used for this instance.
Not every database engine is available for every AWS Region.
Valid Values:

aurora (for MySQL 5.6-compatible Aurora)
aurora-mysql (for MySQL 5.7-compatible Aurora)
aurora-postgresql
mariadb
mysql
oracle-ee
oracle-se2
oracle-se1
oracle-se
postgres
sqlserver-ee
sqlserver-se
sqlserver-ex
sqlserver-web
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("rds", "create-db-instance", "db-instance-identifier", "db-instance-class", "engine", add_option_dict)
