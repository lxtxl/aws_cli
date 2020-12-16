#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/get-grant.html
if __name__ == '__main__':
    """
	accept-grant : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/accept-grant.html
	create-grant : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/create-grant.html
	delete-grant : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/delete-grant.html
	reject-grant : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/reject-grant.html
    """

    parameter_display_string = """
    # grant-arn : Amazon Resource Name (ARN) of the grant.
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

    execute_one_parameter("license-manager", "get-grant", "grant-arn", add_option_dict)