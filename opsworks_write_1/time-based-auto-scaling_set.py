#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/set-time-based-auto-scaling.html
if __name__ == '__main__':
    """
	describe-time-based-auto-scaling : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-time-based-auto-scaling.html
    """

    parameter_display_string = """
    # instance-id : The instance ID.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("opsworks", "set-time-based-auto-scaling", "instance-id", add_option_dict)





