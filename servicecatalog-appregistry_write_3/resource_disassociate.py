#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog-appregistry/disassociate-resource.html
if __name__ == '__main__':
    """
	associate-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog-appregistry/associate-resource.html
    """

    parameter_display_string = """
    # application : The name or ID of the application.
    # resource-type : The type of the resource that is being disassociated.
Possible values:

CFN_STACK
    # resource : The name or ID of the resource.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("servicecatalog-appregistry", "disassociate-resource", "application", "resource-type", "resource", add_option_dict)
