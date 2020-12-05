#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/create-tag-option.html
if __name__ == '__main__':
    """
	delete-tag-option : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/delete-tag-option.html
	describe-tag-option : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-tag-option.html
	list-tag-options : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/list-tag-options.html
	update-tag-option : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/update-tag-option.html
    """

    parameter_display_string = """
    # key : The TagOption key.
    # value : The TagOption value.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("servicecatalog", "create-tag-option", "key", "value", add_option_dict)
