#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/put-job-failure-result.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # job-id : The unique system-generated ID of the job that failed. This is the same ID returned from PollForJobs .
    # failure-details : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("codepipeline", "put-job-failure-result", "job-id", "failure-details", add_option_dict)
