#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/cancel-simulation-job-batch.html
if __name__ == '__main__':
    """
	describe-simulation-job-batch : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/describe-simulation-job-batch.html
	list-simulation-job-batches : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/list-simulation-job-batches.html
	start-simulation-job-batch : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/start-simulation-job-batch.html
    """

    parameter_display_string = """
    # batch : The id of the batch to cancel.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("robomaker", "cancel-simulation-job-batch", "batch", add_option_dict)





