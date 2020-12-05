#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-image-attribute.html
if __name__ == '__main__':
    """
	describe-image-attribute : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-image-attribute.html
	reset-image-attribute : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reset-image-attribute.html
    """

    parameter_display_string = """
    # image-id : The ID of the AMI.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "modify-image-attribute", "image-id", add_option_dict)





