#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reset-snapshot-attribute.html
if __name__ == '__main__':
    """
	describe-snapshot-attribute : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-snapshot-attribute.html
	modify-snapshot-attribute : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-snapshot-attribute.html
    """

    parameter_display_string = """
    # attribute : The attribute to reset. Currently, only the attribute for permission to create volumes can be reset.
Possible values:

productCodes
createVolumePermission
    # snapshot-id : The ID of the snapshot.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "reset-snapshot-attribute", "attribute", "snapshot-id", add_option_dict)
