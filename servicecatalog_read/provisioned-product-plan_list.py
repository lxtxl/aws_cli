#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/list-provisioned-product-plans.html
if __name__ == '__main__':
    """
	create-provisioned-product-plan : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/create-provisioned-product-plan.html
	delete-provisioned-product-plan : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/delete-provisioned-product-plan.html
	describe-provisioned-product-plan : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-provisioned-product-plan.html
	execute-provisioned-product-plan : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/execute-provisioned-product-plan.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("servicecatalog", "list-provisioned-product-plans", add_option_dict)