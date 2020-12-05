#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/describe-shared-directories.html
if __name__ == '__main__':
    """
	accept-shared-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/accept-shared-directory.html
	reject-shared-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/reject-shared-directory.html
    """

    parameter_display_string = """
    # owner-directory-id : Returns the identifier of the directory in the directory owner account.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("ds", "describe-shared-directories", "owner-directory-id", add_option_dict)