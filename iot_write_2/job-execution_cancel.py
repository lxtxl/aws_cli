#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/cancel-job-execution.html
if __name__ == '__main__':
    """
	delete-job-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-job-execution.html
	describe-job-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-job-execution.html
    """

    parameter_display_string = """
    # job-id : The ID of the job to be canceled.
    # thing-name : The name of the thing whose execution of the job will be canceled.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iot", "cancel-job-execution", "job-id", "thing-name", add_option_dict)
