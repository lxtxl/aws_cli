#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/create-cluster.html
if __name__ == '__main__':
    """
	delete-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/delete-cluster.html
	describe-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/describe-cluster.html
	list-clusters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/list-clusters.html
    """

    parameter_display_string = """
    # name : The unique name to give to your cluster.
    # role-arn : The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf. For more information, see Amazon EKS Service IAM Role in the * Amazon EKS User Guide * .
    # resources-vpc-config : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("eks", "create-cluster", "name", "role-arn", "resources-vpc-config", add_option_dict)
