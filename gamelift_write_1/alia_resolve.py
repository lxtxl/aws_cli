#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/resolve-alias.html
if __name__ == '__main__':
    """
	create-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-alias.html
	delete-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/delete-alias.html
	describe-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-alias.html
	update-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-alias.html
    """

    parameter_display_string = """
    # alias-id : The unique identifier of the alias that you want to retrieve a fleet ID for. You can use either the alias ID or ARN value.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("gamelift", "resolve-alias", "alias-id", add_option_dict)





