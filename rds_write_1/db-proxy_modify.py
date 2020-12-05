#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-proxy.html
if __name__ == '__main__':
    """
	create-db-proxy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-proxy.html
	delete-db-proxy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-proxy.html
	describe-db-proxies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-proxies.html
    """

    parameter_display_string = """
    # db-proxy-name : The identifier for the DBProxy to modify.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("rds", "modify-db-proxy", "db-proxy-name", add_option_dict)





