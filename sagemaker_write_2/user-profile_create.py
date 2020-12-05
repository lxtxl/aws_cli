#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-user-profile.html
if __name__ == '__main__':
    """
	delete-user-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-user-profile.html
	describe-user-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-user-profile.html
	list-user-profiles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-user-profiles.html
	update-user-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-user-profile.html
    """

    parameter_display_string = """
    # domain-id : The ID of the associated Domain.
    # user-profile-name : A name for the UserProfile.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sagemaker", "create-user-profile", "domain-id", "user-profile-name", add_option_dict)