#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/register-job-definition.html
if __name__ == '__main__':
    """
	deregister-job-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/deregister-job-definition.html
	describe-job-definitions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/describe-job-definitions.html
    """

    parameter_display_string = """
    # job-definition-name : The name of the job definition to register. Up to 128 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed.
    # type : The type of job definition.
Possible values:

container
multinode
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("batch", "register-job-definition", "job-definition-name", "type", add_option_dict)
