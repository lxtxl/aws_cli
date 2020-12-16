#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-provisioned-product.html
if __name__ == '__main__':
    """
	scan-provisioned-products : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/scan-provisioned-products.html
	search-provisioned-products : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/search-provisioned-products.html
	terminate-provisioned-product : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/terminate-provisioned-product.html
	update-provisioned-product : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/update-provisioned-product.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("servicecatalog", "describe-provisioned-product", add_option_dict)