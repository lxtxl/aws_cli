#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/untag-resource.html
if __name__ == '__main__':
    """
	tag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/tag-resource.html
    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Name (ARN) of the resource from which to remove the tags.
    # tags-to-remove : Tags to remove from this resource.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("glue", "untag-resource", "resource-arn", "tags-to-remove", add_option_dict)
