#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/untag-resource.html
if __name__ == '__main__':
    """
	tag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/tag-resource.html
    """

    parameter_display_string = """
    # resource-arn : An DataBrew resource from which you want to remove a tag or tags. The value for this parameter is an Amazon Resource Name (ARN).
    # tag-keys : The tag keys (names) of one or more tags to be removed.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("databrew", "untag-resource", "resource-arn", "tag-keys", add_option_dict)
