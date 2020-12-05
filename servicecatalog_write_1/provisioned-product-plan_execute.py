#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/execute-provisioned-product-plan.html
if __name__ == '__main__':
    """
	create-provisioned-product-plan : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/create-provisioned-product-plan.html
	delete-provisioned-product-plan : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/delete-provisioned-product-plan.html
	describe-provisioned-product-plan : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-provisioned-product-plan.html
	list-provisioned-product-plans : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/list-provisioned-product-plans.html
    """

    parameter_display_string = """
    # plan-id : The plan identifier.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("servicecatalog", "execute-provisioned-product-plan", "plan-id", add_option_dict)





