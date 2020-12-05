#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/upgrade-applied-schema.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # published-schema-arn : The revision of the published schema to upgrade the directory to.
    # directory-arn : The ARN for the directory to which the upgraded schema will be applied.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("clouddirectory", "upgrade-applied-schema", "published-schema-arn", "directory-arn", add_option_dict)
