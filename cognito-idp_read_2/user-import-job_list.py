#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/describe-user-import-job.html
if __name__ == '__main__':
    """
	create-user-import-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/create-user-import-job.html
	list-user-import-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-user-import-jobs.html
	start-user-import-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/start-user-import-job.html
	stop-user-import-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/stop-user-import-job.html
    """

    parameter_display_string = """
    # user-pool-id : The user pool ID for the user pool that the users are being imported into.
    # job-id : The job ID for the user import job.
    """

    execute_two_parameter("cognito-idp", "describe-user-import-job", "user-pool-id", "job-id", parameter_display_string)