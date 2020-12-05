#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/update-provisioning-artifact.html
if __name__ == '__main__':
    """
	create-provisioning-artifact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/create-provisioning-artifact.html
	delete-provisioning-artifact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/delete-provisioning-artifact.html
	describe-provisioning-artifact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-provisioning-artifact.html
	list-provisioning-artifacts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/list-provisioning-artifacts.html
    """

    parameter_display_string = """
    # product-id : The product identifier.
    # provisioning-artifact-id : The identifier of the provisioning artifact.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("servicecatalog", "update-provisioning-artifact", "product-id", "provisioning-artifact-id", add_option_dict)
