#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/untag-resource.html
if __name__ == '__main__':
    """
	list-resources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/list-resources.html
	tag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/tag-resource.html
    """

    parameter_display_string = """
    # resource-share-arn : The Amazon Resource Name (ARN) of the resource share.
    # tag-keys : The tag keys of the tags to remove.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ram", "untag-resource", "resource-share-arn", "tag-keys", add_option_dict)
