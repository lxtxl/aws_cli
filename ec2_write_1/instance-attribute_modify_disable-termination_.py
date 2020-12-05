#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-instance-attribute.html
if __name__ == '__main__':
    """
	describe-instance-attribute : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instance-attribute.html
	reset-instance-attribute : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reset-instance-attribute.html
    """

    parameter_display_string = """
    # instance-id : The ID of the instance.
    """
    add_option_dict = []
    add_option_dict["parameter_display_string"] = parameter_display_string
    add_option_dict["no_value_parameter_list"] = "--no-disable-api-termination"
    write_one_parameter("ec2", "modify-instance-attribute", "instance-id", add_option_dict)





