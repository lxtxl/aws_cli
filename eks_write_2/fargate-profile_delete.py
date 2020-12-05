#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/delete-fargate-profile.html
if __name__ == '__main__':
    """
	create-fargate-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/create-fargate-profile.html
	describe-fargate-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/describe-fargate-profile.html
	list-fargate-profiles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/list-fargate-profiles.html
    """

    parameter_display_string = """
    # cluster-name : The name of the Amazon EKS cluster associated with the Fargate profile to delete.
    # fargate-profile-name : The name of the Fargate profile to delete.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("eks", "delete-fargate-profile", "cluster-name", "fargate-profile-name", add_option_dict)
