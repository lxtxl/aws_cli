#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/untag-resource.html
if __name__ == '__main__':
    """
	tag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/tag-resource.html
    """

    parameter_display_string = """
    # resource-arn : The Timestream resource that the tags will be removed from. This value is an Amazon Resource Name (ARN).
    # tag-keys : A list of tags keys. Existing tags of the resource whose keys are members of this list will be removed from the Timestream resource.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("timestream-write", "untag-resource", "resource-arn", "tag-keys", add_option_dict)
