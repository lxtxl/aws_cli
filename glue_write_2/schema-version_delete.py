#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-schema-versions.html
if __name__ == '__main__':
    """
	get-schema-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-schema-version.html
	list-schema-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/list-schema-versions.html
	register-schema-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/register-schema-version.html
    """

    parameter_display_string = """
    # schema-id : 
    # versions : A version range may be supplied which may be of the format:

a single version number, 5
a range, 5-8 : deletes versions 5, 6, 7, 8
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("glue", "delete-schema-versions", "schema-id", "versions", add_option_dict)
