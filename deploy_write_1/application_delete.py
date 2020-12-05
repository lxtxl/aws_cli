#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/delete-application.html
if __name__ == '__main__':
    """
	create-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/create-application.html
	get-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/get-application.html
	list-applications : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/list-applications.html
	update-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/update-application.html
    """

    parameter_display_string = """
    # application-name : The name of an AWS CodeDeploy application associated with the IAM user or AWS account.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("deploy", "delete-application", "application-name", add_option_dict)





