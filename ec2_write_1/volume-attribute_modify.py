#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-volume-attribute.html
if __name__ == '__main__':
    """
	describe-volume-attribute : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-volume-attribute.html
    """

    parameter_display_string = """
    # volume-id : The ID of the volume.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "modify-volume-attribute", "volume-id", add_option_dict)





