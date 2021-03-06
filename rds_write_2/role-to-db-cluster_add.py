#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/add-role-to-db-cluster.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # db-cluster-identifier : The name of the DB cluster to associate the IAM role with.
    # role-arn : The Amazon Resource Name (ARN) of the IAM role to associate with the Aurora DB cluster, for example arn:aws:iam::123456789012:role/AuroraAccessRole .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("rds", "add-role-to-db-cluster", "db-cluster-identifier", "role-arn", add_option_dict)
