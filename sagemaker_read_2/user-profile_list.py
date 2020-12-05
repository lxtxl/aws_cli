#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-user-profile.html
if __name__ == '__main__':
    """
	create-user-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-user-profile.html
	delete-user-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-user-profile.html
	list-user-profiles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-user-profiles.html
	update-user-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-user-profile.html
    """

    parameter_display_string = """
    # domain-id : The domain ID.
    # user-profile-name : The user profile name.
    """

    execute_two_parameter("sagemaker", "describe-user-profile", "domain-id", "user-profile-name", parameter_display_string)