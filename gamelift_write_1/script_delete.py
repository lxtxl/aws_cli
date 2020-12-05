#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/delete-script.html
if __name__ == '__main__':
    """
	create-script : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-script.html
	describe-script : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-script.html
	list-scripts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/list-scripts.html
	update-script : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-script.html
    """

    parameter_display_string = """
    # script-id : A unique identifier for a Realtime script to delete. You can use either the script ID or ARN value.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("gamelift", "delete-script", "script-id", add_option_dict)





