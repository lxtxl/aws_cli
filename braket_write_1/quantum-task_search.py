#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/braket/search-quantum-tasks.html
if __name__ == '__main__':
    """
	cancel-quantum-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/braket/cancel-quantum-task.html
	create-quantum-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/braket/create-quantum-task.html
	get-quantum-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/braket/get-quantum-task.html
    """

    parameter_display_string = """
    # filters : Array of SearchQuantumTasksFilter objects.
(structure)

A filter to use to search for tasks.
name -> (string)

The name of the device used for the task.

operator -> (string)

An operator to use in the filter.

values -> (list)

The values to use for the filter.
(string)
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("braket", "search-quantum-tasks", "filters", add_option_dict)





