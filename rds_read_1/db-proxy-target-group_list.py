#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-proxy-target-groups.html
if __name__ == '__main__':
    """
	modify-db-proxy-target-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-proxy-target-group.html
    """

    parameter_display_string = """
    # db-proxy-name : The identifier of the DBProxy associated with the target group.
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

    execute_one_parameter("rds", "describe-db-proxy-target-groups", "db-proxy-name", add_option_dict)