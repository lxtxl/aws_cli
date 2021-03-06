#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-tags.html
if __name__ == '__main__':
    """
	create-tags : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-tags.html
	describe-tags : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-tags.html
    """

    parameter_display_string = """
    # resources : The IDs of the resources, separated by spaces.
Constraints: Up to 1000 resource IDs. We recommend breaking up this request into smaller batches.
(string)
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "delete-tags", "resources", add_option_dict)





