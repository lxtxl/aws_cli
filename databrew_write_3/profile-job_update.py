#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/update-profile-job.html
if __name__ == '__main__':
    """
	create-profile-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/create-profile-job.html
    """

    parameter_display_string = """
    # name : The name of the job to be updated.
    # output-location : 
    # role-arn : The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role to be assumed for this request.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("databrew", "update-profile-job", "name", "output-location", "role-arn", add_option_dict)
