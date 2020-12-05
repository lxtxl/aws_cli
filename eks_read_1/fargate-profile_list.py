#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/list-fargate-profiles.html
if __name__ == '__main__':
    """
	create-fargate-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/create-fargate-profile.html
	delete-fargate-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/delete-fargate-profile.html
	describe-fargate-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/describe-fargate-profile.html
    """

    parameter_display_string = """
    # cluster-name : The name of the Amazon EKS cluster that you would like to listFargate profiles in.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("eks", "list-fargate-profiles", "cluster-name", add_option_dict)