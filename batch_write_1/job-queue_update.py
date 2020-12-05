#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/update-job-queue.html
if __name__ == '__main__':
    """
	create-job-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/create-job-queue.html
	delete-job-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/delete-job-queue.html
	describe-job-queues : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/describe-job-queues.html
    """

    parameter_display_string = """
    # job-queue : The name or the Amazon Resource Name (ARN) of the job queue.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("batch", "update-job-queue", "job-queue", add_option_dict)





