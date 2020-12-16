#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/delete-job.html
if __name__ == '__main__':
    """
	get-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/get-job.html
	list-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/list-jobs.html
	start-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/start-job.html
	stop-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/stop-job.html
    """

    parameter_display_string = """
    # app-id : The unique ID for an Amplify app.
    # branch-name : The name for the branch, for the job.
    # job-id : The unique ID for the job.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("amplify", "delete-job", "app-id", "branch-name", "job-id", add_option_dict)
