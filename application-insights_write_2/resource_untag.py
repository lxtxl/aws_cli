#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/untag-resource.html
if __name__ == '__main__':
    """
	tag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/tag-resource.html
    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Name (ARN) of the application that you want to remove one or more tags from.
    # tag-keys : The tags (tag keys) that you want to remove from the resource. When you specify a tag key, the action removes both that key and its associated tag value.
To remove more than one tag from the application, append the TagKeys parameter and argument for each additional tag to remove, separated by an ampersand.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("application-insights", "untag-resource", "resource-arn", "tag-keys", add_option_dict)
