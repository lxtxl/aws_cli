#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/untag-resource.html
if __name__ == '__main__':
    """
	tag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/tag-resource.html
    """

    parameter_display_string = """
    # resource-arn : An ARN that uniquely identifies a resource. The format of the ARN depends on the type of the tagged resource.
    # tag-key-list : A list of keys to identify which key-value tags to remove from a resource.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("backup", "untag-resource", "resource-arn", "tag-key-list", add_option_dict)
