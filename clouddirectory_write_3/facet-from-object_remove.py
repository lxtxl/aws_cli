#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/remove-facet-from-object.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # directory-arn : The ARN of the directory in which the object resides.
    # schema-facet : 
    # object-reference : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("clouddirectory", "remove-facet-from-object", "directory-arn", "schema-facet", "object-reference", add_option_dict)
