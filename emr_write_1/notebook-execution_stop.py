#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/stop-notebook-execution.html
if __name__ == '__main__':
    """
	describe-notebook-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/describe-notebook-execution.html
	list-notebook-executions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/list-notebook-executions.html
	start-notebook-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/start-notebook-execution.html
    """

    parameter_display_string = """
    # notebook-execution-id : The unique identifier of the notebook execution.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("emr", "stop-notebook-execution", "notebook-execution-id", add_option_dict)





