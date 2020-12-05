#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/stop-execution.html
if __name__ == '__main__':
    """
	describe-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/describe-execution.html
	list-executions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/list-executions.html
	start-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/start-execution.html
    """

    parameter_display_string = """
    # execution-arn : The Amazon Resource Name (ARN) of the execution to stop.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("stepfunctions", "stop-execution", "execution-arn", add_option_dict)





