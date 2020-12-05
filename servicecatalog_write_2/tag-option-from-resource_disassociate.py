#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/disassociate-tag-option-from-resource.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # resource-id : The resource identifier.
    # tag-option-id : The TagOption identifier.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("servicecatalog", "disassociate-tag-option-from-resource", "resource-id", "tag-option-id", add_option_dict)
