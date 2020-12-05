#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/put-lifecycle-policy.html
if __name__ == '__main__':
    """
	delete-lifecycle-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/delete-lifecycle-policy.html
	get-lifecycle-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/get-lifecycle-policy.html
    """

    parameter_display_string = """
    # repository-name : The name of the repository to receive the policy.
    # lifecycle-policy-text : The JSON repository policy text to apply to the repository.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ecr", "put-lifecycle-policy", "repository-name", "lifecycle-policy-text", add_option_dict)
