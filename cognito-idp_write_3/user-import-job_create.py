#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/create-user-import-job.html
if __name__ == '__main__':
    """
	describe-user-import-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/describe-user-import-job.html
	list-user-import-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-user-import-jobs.html
	start-user-import-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/start-user-import-job.html
	stop-user-import-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/stop-user-import-job.html
    """

    parameter_display_string = """
    # job-name : The job name for the user import job.
    # user-pool-id : The user pool ID for the user pool that the users are being imported into.
    # cloud-watch-logs-role-arn : The role ARN for the Amazon CloudWatch Logging role for the user import job.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("cognito-idp", "create-user-import-job", "job-name", "user-pool-id", "cloud-watch-logs-role-arn", add_option_dict)
