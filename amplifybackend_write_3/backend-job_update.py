#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifybackend/update-backend-job.html
if __name__ == '__main__':
    """
	get-backend-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifybackend/get-backend-job.html
	list-backend-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifybackend/list-backend-jobs.html
    """

    parameter_display_string = """
    # app-id : The app ID.
    # backend-environment-name : The name of the backend environment.
    # job-id : The ID for the job.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("amplifybackend", "update-backend-job", "app-id", "backend-environment-name", "job-id", add_option_dict)
