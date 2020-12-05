#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/delete-monitoring-subscription.html
if __name__ == '__main__':
    """
	create-monitoring-subscription : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-monitoring-subscription.html
	get-monitoring-subscription : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-monitoring-subscription.html
    """

    parameter_display_string = """
    # distribution-id : The ID of the distribution that you are disabling metrics for.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("cloudfront", "delete-monitoring-subscription", "distribution-id", add_option_dict)





