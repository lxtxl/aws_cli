#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/create-component.html
if __name__ == '__main__':
    """
	delete-component : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/delete-component.html
	describe-component : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/describe-component.html
	list-components : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/list-components.html
	update-component : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/update-component.html
    """

    parameter_display_string = """
    # resource-group-name : The name of the resource group.
    # component-name : The name of the component.
    # resource-list : The list of resource ARNs that belong to the component.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("application-insights", "create-component", "resource-group-name", "component-name", "resource-list", add_option_dict)
