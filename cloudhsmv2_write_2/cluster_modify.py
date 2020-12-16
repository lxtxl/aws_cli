#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsmv2/modify-cluster.html
if __name__ == '__main__':
    """
	create-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsmv2/create-cluster.html
	delete-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsmv2/delete-cluster.html
	describe-clusters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsmv2/describe-clusters.html
	initialize-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsmv2/initialize-cluster.html
    """

    parameter_display_string = """
    # backup-retention-policy : 
    # cluster-id : The identifier (ID) of the cluster that you want to modify. To find the cluster ID, use  DescribeClusters .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cloudhsmv2", "modify-cluster", "backup-retention-policy", "cluster-id", add_option_dict)
