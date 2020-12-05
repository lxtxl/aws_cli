#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/get-managed-scaling-policy.html
if __name__ == '__main__':
    """
	put-managed-scaling-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/put-managed-scaling-policy.html
	remove-managed-scaling-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/remove-managed-scaling-policy.html
    """

    parameter_display_string = """
    # cluster-id : Specifies the ID of the cluster for which the managed scaling policy will be fetched.
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

    execute_one_parameter("emr", "get-managed-scaling-policy", "cluster-id", add_option_dict)