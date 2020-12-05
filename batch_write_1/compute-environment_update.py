#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/update-compute-environment.html
if __name__ == '__main__':
    """
	create-compute-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/create-compute-environment.html
	delete-compute-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/delete-compute-environment.html
	describe-compute-environments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/describe-compute-environments.html
    """

    parameter_display_string = """
    # compute-environment : The name or full Amazon Resource Name (ARN) of the compute environment to update.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("batch", "update-compute-environment", "compute-environment", add_option_dict)





