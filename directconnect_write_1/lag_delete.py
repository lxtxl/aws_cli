#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/delete-lag.html
if __name__ == '__main__':
    """
	create-lag : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-lag.html
	describe-lags : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-lags.html
	update-lag : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/update-lag.html
    """

    parameter_display_string = """
    # lag-id : The ID of the LAG.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("directconnect", "delete-lag", "lag-id", add_option_dict)





