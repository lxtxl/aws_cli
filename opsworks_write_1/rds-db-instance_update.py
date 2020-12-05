#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/update-rds-db-instance.html
if __name__ == '__main__':
    """
	deregister-rds-db-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/deregister-rds-db-instance.html
	describe-rds-db-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-rds-db-instances.html
	register-rds-db-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/register-rds-db-instance.html
    """

    parameter_display_string = """
    # rds-db-instance-arn : The Amazon RDS instanceâs ARN.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("opsworks", "update-rds-db-instance", "rds-db-instance-arn", add_option_dict)





