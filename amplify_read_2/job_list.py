#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/list-jobs.html
if __name__ == '__main__':
    """
	delete-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/delete-job.html
	get-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/get-job.html
	start-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/start-job.html
	stop-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/stop-job.html
    """

    parameter_display_string = """
    # app-id : The unique ID for an Amplify app.
    # branch-name : The name for a branch.
    """

    execute_two_parameter("amplify", "list-jobs", "app-id", "branch-name", parameter_display_string)