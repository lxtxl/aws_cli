#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/set-repository-policy.html
if __name__ == '__main__':
    """
	delete-repository-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/delete-repository-policy.html
	get-repository-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/get-repository-policy.html
    """

    parameter_display_string = """
    # repository-name : The name of the repository to receive the policy.
    # policy-text : The JSON repository policy text to apply to the repository. For more information, see Amazon ECR Repository Policies in the Amazon Elastic Container Registry User Guide .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ecr", "set-repository-policy", "repository-name", "policy-text", add_option_dict)
