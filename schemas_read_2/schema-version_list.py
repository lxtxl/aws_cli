#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/list-schema-versions.html
if __name__ == '__main__':
    """
	delete-schema-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/delete-schema-version.html
    """

    parameter_display_string = """
    # registry-name : The name of the registry.
    # schema-name : The name of the schema.
    """

    execute_two_parameter("schemas", "list-schema-versions", "registry-name", "schema-name", parameter_display_string)