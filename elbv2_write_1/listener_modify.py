#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/modify-listener.html
if __name__ == '__main__':
    """
	create-listener : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/create-listener.html
	delete-listener : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/delete-listener.html
	describe-listeners : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-listeners.html
    """

    parameter_display_string = """
    # listener-arn : The Amazon Resource Name (ARN) of the listener.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("elbv2", "modify-listener", "listener-arn", add_option_dict)





