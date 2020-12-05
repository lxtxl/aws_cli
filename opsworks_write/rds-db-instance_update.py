#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	deregister-rds-db-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/deregister-rds-db-instance.html
	describe-rds-db-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-rds-db-instances.html
	register-rds-db-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/register-rds-db-instance.html
    """

    write_parameter("opsworks", "update-rds-db-instance")