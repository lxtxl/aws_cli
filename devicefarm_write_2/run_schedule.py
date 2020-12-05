#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/schedule-run.html
if __name__ == '__main__':
    """
	delete-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/delete-run.html
	get-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/get-run.html
	list-runs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/list-runs.html
	stop-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/stop-run.html
    """

    parameter_display_string = """
    # project-arn : The ARN of the project for the run to be scheduled.
    # test : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("devicefarm", "schedule-run", "project-arn", "test", add_option_dict)
