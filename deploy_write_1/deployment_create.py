#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/create-deployment.html
if __name__ == '__main__':
    """
	continue-deployment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/continue-deployment.html
	get-deployment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/get-deployment.html
	list-deployments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/list-deployments.html
	stop-deployment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/stop-deployment.html
    """

    parameter_display_string = """
    # application-name : The name of an AWS CodeDeploy application associated with the IAM user or AWS account.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("deploy", "create-deployment", "application-name", add_option_dict)





