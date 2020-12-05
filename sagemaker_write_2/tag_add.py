#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/add-tags.html
if __name__ == '__main__':
    """
	delete-tags : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-tags.html
	list-tags : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-tags.html
    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Name (ARN) of the resource that you want to tag.
    # tags : An array of Tag objects. Each tag is a key-value pair. Only the key parameter is required. If you donât specify a value, Amazon SageMaker sets the value to an empty string.
(structure)

Describes a tag.
Key -> (string)

The tag key.

Value -> (string)

The tag value.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sagemaker", "add-tags", "resource-arn", "tags", add_option_dict)
