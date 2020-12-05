#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/list-access-points.html
if __name__ == '__main__':
    """
	create-access-point : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/create-access-point.html
	delete-access-point : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/delete-access-point.html
	get-access-point : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-access-point.html
    """

    parameter_display_string = """
    # account-id : The AWS account ID for owner of the bucket whose access points you want to list.
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

    execute_one_parameter("s3control", "list-access-points", "account-id", add_option_dict)