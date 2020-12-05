#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/create-case.html
if __name__ == '__main__':
    """
	describe-cases : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/describe-cases.html
	resolve-case : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/resolve-case.html
    """

    parameter_display_string = """
    # subject : The title of the AWS Support case. The title appears in the Subject field on the AWS Support Center Create Case page.
    # communication-body : The communication body text that describes the issue. This text appears in the Description field on the AWS Support Center Create Case page.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("support", "create-case", "subject", "communication-body", add_option_dict)
