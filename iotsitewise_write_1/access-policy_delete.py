#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/delete-access-policy.html
if __name__ == '__main__':
    """
	create-access-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/create-access-policy.html
	describe-access-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-access-policy.html
	list-access-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/list-access-policies.html
	update-access-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/update-access-policy.html
    """

    parameter_display_string = """
    # access-policy-id : The ID of the access policy to be deleted.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iotsitewise", "delete-access-policy", "access-policy-id", add_option_dict)





