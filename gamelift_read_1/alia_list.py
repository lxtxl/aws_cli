#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-alias.html
if __name__ == '__main__':
    """
	create-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-alias.html
	delete-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/delete-alias.html
	resolve-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/resolve-alias.html
	update-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-alias.html
    """

    parameter_display_string = """
    # alias-id : The unique identifier for the fleet alias that you want to retrieve. You can use either the alias ID or ARN value.
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

    execute_one_parameter("gamelift", "describe-alias", "alias-id", add_option_dict)