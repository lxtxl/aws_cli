#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/remove-role-from-db-instance.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # db-instance-identifier : The name of the DB instance to disassociate the IAM role from.
    # role-arn : The Amazon Resource Name (ARN) of the IAM role to disassociate from the DB instance, for example, arn:aws:iam::123456789012:role/AccessRole .
    # feature-name : The name of the feature for the DB instance that the IAM role is to be disassociated from. For the list of supported feature names, see DBEngineVersion .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("rds", "remove-role-from-db-instance", "db-instance-identifier", "role-arn", "feature-name", add_option_dict)
