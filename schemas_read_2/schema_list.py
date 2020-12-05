#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/describe-schema.html
if __name__ == '__main__':
    """
	create-schema : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/create-schema.html
	delete-schema : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/delete-schema.html
	export-schema : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/export-schema.html
	list-schemas : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/list-schemas.html
	search-schemas : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/search-schemas.html
	update-schema : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/update-schema.html
    """

    parameter_display_string = """
    # registry-name : The name of the registry.
    # schema-name : The name of the schema.
    """

    execute_two_parameter("schemas", "describe-schema", "registry-name", "schema-name", parameter_display_string)