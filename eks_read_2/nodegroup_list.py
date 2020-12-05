#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/describe-nodegroup.html
if __name__ == '__main__':
    """
	create-nodegroup : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/create-nodegroup.html
	delete-nodegroup : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/delete-nodegroup.html
	list-nodegroups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/list-nodegroups.html
    """

    parameter_display_string = """
    # cluster-name : The name of the Amazon EKS cluster associated with the node group.
    # nodegroup-name : The name of the node group to describe.
    """

    execute_two_parameter("eks", "describe-nodegroup", "cluster-name", "nodegroup-name", parameter_display_string)