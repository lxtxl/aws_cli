#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/stop-stack.html
if __name__ == '__main__':
    """
	clone-stack : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/clone-stack.html
	create-stack : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/create-stack.html
	delete-stack : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/delete-stack.html
	describe-stacks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-stacks.html
	start-stack : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/start-stack.html
	update-stack : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/update-stack.html
    """

    parameter_display_string = """
    # stack-id : The stack ID.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("opsworks", "stop-stack", "stack-id", add_option_dict)





