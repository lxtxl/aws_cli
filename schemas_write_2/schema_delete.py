#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/delete-schema.html
if __name__ == '__main__':
    """
	create-schema : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/create-schema.html
	describe-schema : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/describe-schema.html
	export-schema : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/export-schema.html
	list-schemas : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/list-schemas.html
	search-schemas : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/search-schemas.html
	update-schema : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/update-schema.html
    """

    parameter_display_string = """
    # registry-name : The name of the registry.
    # schema-name : The name of the schema.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("schemas", "delete-schema", "registry-name", "schema-name", add_option_dict)
