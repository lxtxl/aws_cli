#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-service-linked-role.html
if __name__ == '__main__':
    """
	create-service-linked-role : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-service-linked-role.html
    """

    parameter_display_string = """
    # role-name : The name of the service-linked role to be deleted.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iam", "delete-service-linked-role", "role-name", add_option_dict)





