#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/service-quotas/request-service-quota-increase.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # service-code : Specifies the service that you want to use.
    # quota-code : Specifies the service quota that you want to use.
    # desired-value : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("service-quotas", "request-service-quota-increase", "service-code", "quota-code", "desired-value", add_option_dict)
