#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/create-organization.html
if __name__ == '__main__':
    """
	delete-organization : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-organization.html
	describe-organization : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/describe-organization.html
	list-organizations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-organizations.html
    """

    parameter_display_string = """
    # alias : The organization alias.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("workmail", "create-organization", "alias", add_option_dict)





