#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/update-cluster.html
if __name__ == '__main__':
    """
	create-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/create-cluster.html
	delete-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/delete-cluster.html
	describe-clusters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/describe-clusters.html
    """

    parameter_display_string = """
    # cluster-name : The name of the DAX cluster to be modified.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("dax", "update-cluster", "cluster-name", add_option_dict)





