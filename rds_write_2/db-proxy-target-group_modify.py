#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-proxy-target-group.html
if __name__ == '__main__':
    """
	describe-db-proxy-target-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-proxy-target-groups.html
    """

    parameter_display_string = """
    # target-group-name : The name of the new target group to assign to the proxy.
    # db-proxy-name : The name of the new proxy to which to assign the target group.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("rds", "modify-db-proxy-target-group", "target-group-name", "db-proxy-name", add_option_dict)
