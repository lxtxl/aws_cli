#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/cancel-world-export-job.html
if __name__ == '__main__':
    """
	create-world-export-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/create-world-export-job.html
	describe-world-export-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/describe-world-export-job.html
	list-world-export-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/list-world-export-jobs.html
    """

    parameter_display_string = """
    # job : The Amazon Resource Name (arn) of the world export job to cancel.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("robomaker", "cancel-world-export-job", "job", add_option_dict)





