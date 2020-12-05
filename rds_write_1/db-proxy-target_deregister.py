#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/deregister-db-proxy-targets.html
if __name__ == '__main__':
    """
	describe-db-proxy-targets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-proxy-targets.html
	register-db-proxy-targets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/register-db-proxy-targets.html
    """

    parameter_display_string = """
    # db-proxy-name : The identifier of the DBProxy that is associated with the DBProxyTargetGroup .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("rds", "deregister-db-proxy-targets", "db-proxy-name", add_option_dict)





