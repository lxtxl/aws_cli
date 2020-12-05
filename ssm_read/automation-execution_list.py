#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-automation-executions.html
if __name__ == '__main__':
    """
	get-automation-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-automation-execution.html
	start-automation-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/start-automation-execution.html
	stop-automation-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/stop-automation-execution.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("ssm", "describe-automation-executions", add_option_dict)