#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-default-credit-specification.html
if __name__ == '__main__':
    """
	modify-default-credit-specification : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-default-credit-specification.html
    """

    parameter_display_string = """
    # instance-family : The instance family.
Possible values:

t2
t3
t3a
t4g
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

    execute_one_parameter("ec2", "get-default-credit-specification", "instance-family", add_option_dict)