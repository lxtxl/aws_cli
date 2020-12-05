#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/tag-resource.html
if __name__ == '__main__':
    """
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/untag-resource.html
    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Name (ARN) of the Amazon FSx resource that you want to tag.
    # tags : A list of tags for the resource. If a tag with a given key already exists, the value is replaced by the one specified in this parameter.
(structure)

Specifies a key-value pair for a resource tag.
Key -> (string)

A value that specifies the TagKey , the name of the tag. Tag keys must be unique for the resource to which they are attached.

Value -> (string)

A value that specifies the TagValue , the value assigned to the corresponding tag key. Tag values can be null and donât have to be unique in a tag set. For example, you can have a key-value pair in a tag set of finances : April and also of payroll : April .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("fsx", "tag-resource", "resource-arn", "tags", add_option_dict)
