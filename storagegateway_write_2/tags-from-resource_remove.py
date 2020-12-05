#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/remove-tags-from-resource.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Name (ARN) of the resource you want to remove the tags from.
    # tag-keys : The keys of the tags you want to remove from the specified resource. A tag is composed of a key-value pair.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("storagegateway", "remove-tags-from-resource", "resource-arn", "tag-keys", add_option_dict)
