#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/delete-environment.html
if __name__ == '__main__':
    """
	describe-environments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/describe-environments.html
	list-environments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/list-environments.html
	update-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/update-environment.html
    """

    parameter_display_string = """
    # environment-id : The ID of the environment to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("cloud9", "delete-environment", "environment-id", add_option_dict)





