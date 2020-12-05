#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-automation-execution.html
if __name__ == '__main__':
    """
	describe-automation-executions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-automation-executions.html
	start-automation-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/start-automation-execution.html
	stop-automation-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/stop-automation-execution.html
    """

    parameter_display_string = """
    # automation-execution-id : The unique identifier for an existing automation execution to examine. The execution ID is returned by StartAutomationExecution when the execution of an Automation document is initiated.
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

    execute_one_parameter("ssm", "get-automation-execution", "automation-execution-id", add_option_dict)