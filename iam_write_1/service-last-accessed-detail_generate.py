#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/generate-service-last-accessed-details.html
if __name__ == '__main__':
    """
	get-service-last-accessed-details : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-service-last-accessed-details.html
    """

    parameter_display_string = """
    # arn : The ARN of the IAM resource (user, group, role, or managed policy) used to generate information about when the resource was last used in an attempt to access an AWS service.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iam", "generate-service-last-accessed-details", "arn", add_option_dict)





