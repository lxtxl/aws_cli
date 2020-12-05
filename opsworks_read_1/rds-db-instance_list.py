#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-rds-db-instances.html
if __name__ == '__main__':
    """
	deregister-rds-db-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/deregister-rds-db-instance.html
	register-rds-db-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/register-rds-db-instance.html
	update-rds-db-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/update-rds-db-instance.html
    """

    parameter_display_string = """
    # stack-id : The ID of the stack with which the instances are registered. The operation returns descriptions of all registered Amazon RDS instances.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("opsworks", "describe-rds-db-instances", "stack-id", add_option_dict)