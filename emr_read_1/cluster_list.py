#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/describe-cluster.html
if __name__ == '__main__':
    """
	create-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/create-cluster.html
	list-clusters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/list-clusters.html
	modify-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/modify-cluster.html
	terminate-clusters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/terminate-clusters.html
    """

    parameter_display_string = """
    # cluster-id : A unique string that identifies a cluster. The create-cluster command returns this identifier. You can use the list-clusters command to get cluster IDs.
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

    execute_one_parameter("emr", "describe-cluster", "cluster-id", add_option_dict)