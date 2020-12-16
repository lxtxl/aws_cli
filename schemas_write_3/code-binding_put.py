#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/put-code-binding.html
if __name__ == '__main__':
    """
	describe-code-binding : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/describe-code-binding.html
    """

    parameter_display_string = """
    # language : The language of the code binding.
    # registry-name : The name of the registry.
    # schema-name : The name of the schema.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("schemas", "put-code-binding", "language", "registry-name", "schema-name", add_option_dict)
