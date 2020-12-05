#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/tag-resource.html
if __name__ == '__main__':
    """
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/untag-resource.html
    """

    parameter_display_string = """
    # arn : The Amazon Resource Name (ARN) of the notification rule to tag.
    # tags : The list of tags to associate with the resource. Tag key names cannot start with âawsâ.
key -> (string)
value -> (string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("codestar-notifications", "tag-resource", "arn", "tags", add_option_dict)
