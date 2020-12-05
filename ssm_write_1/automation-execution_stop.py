#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/stop-automation-execution.html
if __name__ == '__main__':
    """
	describe-automation-executions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-automation-executions.html
	get-automation-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-automation-execution.html
	start-automation-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/start-automation-execution.html
    """

    parameter_display_string = """
    # automation-execution-id : The execution ID of the Automation to stop.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ssm", "stop-automation-execution", "automation-execution-id", add_option_dict)





