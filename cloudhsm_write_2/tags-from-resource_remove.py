#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsm/remove-tags-from-resource.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Name (ARN) of the AWS CloudHSM resource.
    # tag-key-list : The tag key or keys to remove.
Specify only the tag key to remove (not the value). To overwrite the value for an existing tag, use  AddTagsToResource .
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cloudhsm", "remove-tags-from-resource", "resource-arn", "tag-key-list", add_option_dict)
