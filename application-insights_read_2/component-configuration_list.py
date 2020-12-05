#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/describe-component-configuration.html
if __name__ == '__main__':
    """
	update-component-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/update-component-configuration.html
    """

    parameter_display_string = """
    # resource-group-name : The name of the resource group.
    # component-name : The name of the component.
    """

    execute_two_parameter("application-insights", "describe-component-configuration", "resource-group-name", "component-name", parameter_display_string)