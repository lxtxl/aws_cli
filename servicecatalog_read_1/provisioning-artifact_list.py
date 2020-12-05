#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/list-provisioning-artifacts.html
if __name__ == '__main__':
    """
	create-provisioning-artifact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/create-provisioning-artifact.html
	delete-provisioning-artifact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/delete-provisioning-artifact.html
	describe-provisioning-artifact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-provisioning-artifact.html
	update-provisioning-artifact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/update-provisioning-artifact.html
    """

    parameter_display_string = """
    # product-id : The product identifier.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("servicecatalog", "list-provisioning-artifacts", "product-id", add_option_dict)