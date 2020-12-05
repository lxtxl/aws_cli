#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/disable-aws-service-access.html
if __name__ == '__main__':
    """
	enable-aws-service-access : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/enable-aws-service-access.html
    """

    parameter_display_string = """
    # service-principal : The service principal name of the AWS service for which you want to disable integration with your organization. This is typically in the form of a URL, such as `` service-abbreviation .amazonaws.com`` .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("organizations", "disable-aws-service-access", "service-principal", add_option_dict)





