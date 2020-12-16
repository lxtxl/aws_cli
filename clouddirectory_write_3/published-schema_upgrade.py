#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/upgrade-published-schema.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # development-schema-arn : The ARN of the development schema with the changes used for the upgrade.
    # published-schema-arn : The ARN of the published schema to be upgraded.
    # minor-version : Identifies the minor version of the published schema that will be created. This parameter is NOT optional.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("clouddirectory", "upgrade-published-schema", "development-schema-arn", "published-schema-arn", "minor-version", add_option_dict)
