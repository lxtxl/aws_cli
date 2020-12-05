#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/disassociate-budget-from-resource.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # budget-name : The name of the budget you want to disassociate.
    # resource-id : The resource identifier you want to disassociate from. Either a portfolio-id or a product-id.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("servicecatalog", "disassociate-budget-from-resource", "budget-name", "resource-id", add_option_dict)
