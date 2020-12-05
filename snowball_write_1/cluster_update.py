#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/snowball/update-cluster.html
if __name__ == '__main__':
    """
	cancel-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/snowball/cancel-cluster.html
	create-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/snowball/create-cluster.html
	describe-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/snowball/describe-cluster.html
	list-clusters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/snowball/list-clusters.html
    """

    parameter_display_string = """
    # cluster-id : The cluster ID of the cluster that you want to update, for example CID123e4567-e89b-12d3-a456-426655440000 .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("snowball", "update-cluster", "cluster-id", add_option_dict)





