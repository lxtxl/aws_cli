#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/confirm-product-instance.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # instance-id : The ID of the instance.
    # product-code : The product code. This must be a product code that you own.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "confirm-product-instance", "instance-id", "product-code", add_option_dict)
