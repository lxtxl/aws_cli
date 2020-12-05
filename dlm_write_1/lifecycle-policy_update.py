#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dlm/update-lifecycle-policy.html
if __name__ == '__main__':
    """
	create-lifecycle-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dlm/create-lifecycle-policy.html
	delete-lifecycle-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dlm/delete-lifecycle-policy.html
	get-lifecycle-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dlm/get-lifecycle-policies.html
	get-lifecycle-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dlm/get-lifecycle-policy.html
    """

    parameter_display_string = """
    # policy-id : The identifier of the lifecycle policy.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("dlm", "update-lifecycle-policy", "policy-id", add_option_dict)





