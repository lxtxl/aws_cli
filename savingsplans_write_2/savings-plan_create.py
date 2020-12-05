#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/savingsplans/create-savings-plan.html
if __name__ == '__main__':
    """
	describe-savings-plans : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/savingsplans/describe-savings-plans.html
    """

    parameter_display_string = """
    # savings-plan-offering-id : The ID of the offering.
    # commitment : The hourly commitment, in USD. This is a value between 0.001 and 1 million. You cannot specify more than three digits after the decimal point.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("savingsplans", "create-savings-plan", "savings-plan-offering-id", "commitment", add_option_dict)
