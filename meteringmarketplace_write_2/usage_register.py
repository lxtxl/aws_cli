#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/meteringmarketplace/register-usage.html
if __name__ == '__main__':
    """
	meter-usage : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/meteringmarketplace/meter-usage.html
    """

    parameter_display_string = """
    # product-code : Product code is used to uniquely identify a product in AWS Marketplace. The product code should be the same as the one used during the publishing of a new product.
    # public-key-version : Public Key Version provided by AWS Marketplace
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("meteringmarketplace", "register-usage", "product-code", "public-key-version", add_option_dict)
