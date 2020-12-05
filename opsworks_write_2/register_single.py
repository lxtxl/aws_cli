#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/register.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # stack-id : A stack ID. The instance will be registered with the given stack.
    # infrastructure-class : Specifies whether to register an EC2 instance (ec2) or an on-premises instance (on-premises).
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("opsworks", "register", "stack-id", "infrastructure-class", add_option_dict)
