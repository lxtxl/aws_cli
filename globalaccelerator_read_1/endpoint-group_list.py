#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/describe-endpoint-group.html
if __name__ == '__main__':
    """
	create-endpoint-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/create-endpoint-group.html
	delete-endpoint-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/delete-endpoint-group.html
	list-endpoint-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/list-endpoint-groups.html
	update-endpoint-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/update-endpoint-group.html
    """

    parameter_display_string = """
    # endpoint-group-arn : The Amazon Resource Name (ARN) of the endpoint group to describe.
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

    execute_one_parameter("globalaccelerator", "describe-endpoint-group", "endpoint-group-arn", add_option_dict)