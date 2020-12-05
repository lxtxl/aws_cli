#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/untag-resource.html
if __name__ == '__main__':
    """
	tag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/tag-resource.html
    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Number (ARN) of an X-Ray group or sampling rule.
    # tag-keys : Keys for one or more tags that you want to remove from an X-Ray group or sampling rule.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("xray", "untag-resource", "resource-arn", "tag-keys", add_option_dict)
