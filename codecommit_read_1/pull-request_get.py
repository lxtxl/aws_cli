#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-pull-request.html
if __name__ == '__main__':
    """
	create-pull-request : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/create-pull-request.html
	list-pull-requests : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/list-pull-requests.html
    """

    parameter_display_string = """
    # pull-request-id : The system-generated ID of the pull request. To get this ID, use  ListPullRequests .
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

    execute_one_parameter("codecommit", "get-pull-request", "pull-request-id", add_option_dict)