#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/describe-fargate-profile.html
if __name__ == '__main__':
    """
	create-fargate-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/create-fargate-profile.html
	delete-fargate-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/delete-fargate-profile.html
	list-fargate-profiles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/list-fargate-profiles.html
    """

    parameter_display_string = """
    # cluster-name : The name of the Amazon EKS cluster associated with the Fargate profile.
    # fargate-profile-name : The name of the Fargate profile to describe.
    """

    execute_two_parameter("eks", "describe-fargate-profile", "cluster-name", "fargate-profile-name", parameter_display_string)