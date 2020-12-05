#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/describe-cache-clusters.html
if __name__ == '__main__':
    """
	create-cache-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/create-cache-cluster.html
	delete-cache-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/delete-cache-cluster.html
	modify-cache-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/modify-cache-cluster.html
	reboot-cache-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/reboot-cache-cluster.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("elasticache", "describe-cache-clusters", add_option_dict)