#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/create-facet.html
if __name__ == '__main__':
    """
	delete-facet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/delete-facet.html
	get-facet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/get-facet.html
	update-facet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/update-facet.html
    """

    parameter_display_string = """
    # schema-arn : The schema ARN in which the new  Facet will be created. For more information, see  arns .
    # name : The name of the  Facet , which is unique for a given schema.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("clouddirectory", "create-facet", "schema-arn", "name", add_option_dict)
