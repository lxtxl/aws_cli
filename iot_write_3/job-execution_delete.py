#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-job-execution.html
if __name__ == '__main__':
    """
	cancel-job-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/cancel-job-execution.html
	describe-job-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-job-execution.html
    """

    parameter_display_string = """
    # job-id : The ID of the job whose execution on a particular device will be deleted.
    # thing-name : The name of the thing whose job execution will be deleted.
    # execution-number : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("iot", "delete-job-execution", "job-id", "thing-name", "execution-number", add_option_dict)
