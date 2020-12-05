#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/snowball/describe-cluster.html
if __name__ == '__main__':
    """
	cancel-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/snowball/cancel-cluster.html
	create-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/snowball/create-cluster.html
	list-clusters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/snowball/list-clusters.html
	update-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/snowball/update-cluster.html
    """

    parameter_display_string = """
    # cluster-id : The automatically generated ID for a cluster.
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

    execute_one_parameter("snowball", "describe-cluster", "cluster-id", add_option_dict)