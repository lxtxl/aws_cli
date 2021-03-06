#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/untag-resource.html
if __name__ == '__main__':
    """
	tag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/tag-resource.html
    """

    parameter_display_string = """
    # resource-arn : The ARN of the canary that youâre removing tags from.
The ARN format of a canary is ``arn:aws:synthetics:Region :account-id :canary:canary-name `` .
    # tag-keys : The list of tag keys to remove from the resource.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("synthetics", "untag-resource", "resource-arn", "tag-keys", add_option_dict)
