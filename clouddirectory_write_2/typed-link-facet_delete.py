#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/delete-typed-link-facet.html
if __name__ == '__main__':
    """
	create-typed-link-facet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/create-typed-link-facet.html
	update-typed-link-facet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/update-typed-link-facet.html
    """

    parameter_display_string = """
    # schema-arn : The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .
    # name : The unique name of the typed link facet.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("clouddirectory", "delete-typed-link-facet", "schema-arn", "name", add_option_dict)
