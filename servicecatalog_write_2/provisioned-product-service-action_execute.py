#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/execute-provisioned-product-service-action.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # provisioned-product-id : The identifier of the provisioned product.
    # service-action-id : The self-service action identifier. For example, act-fs7abcd89wxyz .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("servicecatalog", "execute-provisioned-product-service-action", "provisioned-product-id", "service-action-id", add_option_dict)
