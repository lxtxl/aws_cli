#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/create-index.html
if __name__ == '__main__':
    """
	list-index : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/list-index.html
    """

    parameter_display_string = """
    # directory-arn : The ARN of the directory where the index should be created.
    # ordered-indexed-attribute-list : Specifies the attributes that should be indexed on. Currently only a single attribute is supported.
(structure)

A unique identifier for an attribute.
SchemaArn -> (string)

The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

FacetName -> (string)

The name of the facet that the attribute exists within.

Name -> (string)

The name of the attribute.
    # is-unique | --no-is-unique : Indicates whether the attribute that is being indexed has unique values or not.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("clouddirectory", "create-index", "directory-arn", "ordered-indexed-attribute-list", "is-unique | --no-is-unique", add_option_dict)
