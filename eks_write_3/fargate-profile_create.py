#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/create-fargate-profile.html
if __name__ == '__main__':
    """
	delete-fargate-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/delete-fargate-profile.html
	describe-fargate-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/describe-fargate-profile.html
	list-fargate-profiles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/list-fargate-profiles.html
    """

    parameter_display_string = """
    # fargate-profile-name : The name of the Fargate profile.
    # cluster-name : The name of the Amazon EKS cluster to apply the Fargate profile to.
    # pod-execution-role-arn : The Amazon Resource Name (ARN) of the pod execution role to use for pods that match the selectors in the Fargate profile. The pod execution role allows Fargate infrastructure to register with your cluster as a node, and it provides read access to Amazon ECR image repositories. For more information, see Pod Execution Role in the Amazon EKS User Guide .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("eks", "create-fargate-profile", "fargate-profile-name", "cluster-name", "pod-execution-role-arn", add_option_dict)
