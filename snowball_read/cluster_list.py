#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/snowball/list-clusters.html
if __name__ == '__main__':
    """
	cancel-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/snowball/cancel-cluster.html
	create-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/snowball/create-cluster.html
	describe-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/snowball/describe-cluster.html
	update-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/snowball/update-cluster.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("snowball", "list-clusters", add_option_dict)