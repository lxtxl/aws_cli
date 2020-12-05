#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/create-object.html
if __name__ == '__main__':
    """
	attach-object : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/attach-object.html
	delete-object : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/delete-object.html
	detach-object : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/detach-object.html
    """

    parameter_display_string = """
    # directory-arn : The Amazon Resource Name (ARN) that is associated with the  Directory in which the object will be created. For more information, see  arns .
    # schema-facets : A list of schema facets to be associated with the object. Do not provide minor version components. See  SchemaFacet for details.
(structure)

A facet.
SchemaArn -> (string)

The ARN of the schema that contains the facet with no minor component. See  arns and In-Place Schema Upgrade for a description of when to provide minor versions.

FacetName -> (string)

The name of the facet.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("clouddirectory", "create-object", "directory-arn", "schema-facets", add_option_dict)
