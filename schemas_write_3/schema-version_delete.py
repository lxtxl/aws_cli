#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/delete-schema-version.html
if __name__ == '__main__':
    """
	list-schema-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/list-schema-versions.html
    """

    parameter_display_string = """
    # registry-name : The name of the registry.
    # schema-name : The name of the schema.
    # schema-version : The version number of the schema
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("schemas", "delete-schema-version", "registry-name", "schema-name", "schema-version", add_option_dict)
