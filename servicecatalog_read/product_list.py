#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-product.html
if __name__ == '__main__':
    """
	copy-product : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/copy-product.html
	create-product : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/create-product.html
	delete-product : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/delete-product.html
	provision-product : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/provision-product.html
	search-products : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/search-products.html
	update-product : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/update-product.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("servicecatalog", "describe-product", add_option_dict)