#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/get-run.html
if __name__ == '__main__':
    """
	delete-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/delete-run.html
	list-runs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/list-runs.html
	schedule-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/schedule-run.html
	stop-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/stop-run.html
    """

    parameter_display_string = """
    # arn : The runâs ARN.
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

    execute_one_parameter("devicefarm", "get-run", "arn", add_option_dict)