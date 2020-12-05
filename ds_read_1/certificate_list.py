#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/list-certificates.html
if __name__ == '__main__':
    """
	deregister-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/deregister-certificate.html
	describe-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/describe-certificate.html
	register-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/register-certificate.html
    """

    parameter_display_string = """
    # directory-id : The identifier of the directory.
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

    execute_one_parameter("ds", "list-certificates", "directory-id", add_option_dict)