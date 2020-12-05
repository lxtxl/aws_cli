#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-default-credit-specification.html
if __name__ == '__main__':
    """
	get-default-credit-specification : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-default-credit-specification.html
    """

    parameter_display_string = """
    # instance-family : The instance family.
Possible values:

t2
t3
t3a
t4g
    # cpu-credits : The credit option for CPU usage of the instance family.
Valid Values: standard | unlimited
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "modify-default-credit-specification", "instance-family", "cpu-credits", add_option_dict)
