#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr-public/delete-repository-policy.html
if __name__ == '__main__':
    """
	get-repository-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr-public/get-repository-policy.html
	set-repository-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr-public/set-repository-policy.html
    """

    parameter_display_string = """
    # repository-name : The name of the repository that is associated with the repository policy to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ecr-public", "delete-repository-policy", "repository-name", add_option_dict)





