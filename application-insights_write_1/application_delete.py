#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/delete-application.html
if __name__ == '__main__':
    """
	create-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/create-application.html
	describe-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/describe-application.html
	list-applications : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/list-applications.html
	update-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/update-application.html
    """

    parameter_display_string = """
    # resource-group-name : The name of the resource group.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("application-insights", "delete-application", "resource-group-name", add_option_dict)





