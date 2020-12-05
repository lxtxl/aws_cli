#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/delete-nodegroup.html
if __name__ == '__main__':
    """
	create-nodegroup : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/create-nodegroup.html
	describe-nodegroup : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/describe-nodegroup.html
	list-nodegroups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/list-nodegroups.html
    """

    parameter_display_string = """
    # cluster-name : The name of the Amazon EKS cluster that is associated with your node group.
    # nodegroup-name : The name of the node group to delete.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("eks", "delete-nodegroup", "cluster-name", "nodegroup-name", add_option_dict)
