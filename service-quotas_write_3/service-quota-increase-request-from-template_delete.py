#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/service-quotas/delete-service-quota-increase-request-from-template.html
if __name__ == '__main__':
    """
	get-service-quota-increase-request-from-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/service-quotas/get-service-quota-increase-request-from-template.html
    """

    parameter_display_string = """
    # service-code : Specifies the code for the service that you want to delete.
    # quota-code : Specifies the code for the quota that you want to delete.
    # aws-region : Specifies the AWS Region for the quota that you want to delete.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("service-quotas", "delete-service-quota-increase-request-from-template", "service-code", "quota-code", "aws-region", add_option_dict)
