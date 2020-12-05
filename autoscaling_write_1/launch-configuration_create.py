#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-launch-configuration.html
if __name__ == '__main__':
    """
	delete-launch-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/delete-launch-configuration.html
	describe-launch-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-launch-configurations.html
    """

    parameter_display_string = """
    # launch-configuration-name : The name of the launch configuration. This name must be unique per Region per account.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("autoscaling", "create-launch-configuration", "launch-configuration-name", add_option_dict)





