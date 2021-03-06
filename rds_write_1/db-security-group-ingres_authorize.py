#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/authorize-db-security-group-ingress.html
if __name__ == '__main__':
    """
	revoke-db-security-group-ingress : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/revoke-db-security-group-ingress.html
    """

    parameter_display_string = """
    # db-security-group-name : The name of the DB security group to add authorization to.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("rds", "authorize-db-security-group-ingress", "db-security-group-name", add_option_dict)





