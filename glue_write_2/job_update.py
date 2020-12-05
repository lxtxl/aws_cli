#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-job.html
if __name__ == '__main__':
    """
	create-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-job.html
	delete-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-job.html
	get-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-job.html
	get-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-jobs.html
	list-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/list-jobs.html
    """

    parameter_display_string = """
    # job-name : The name of the job definition to update.
    # job-update : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("glue", "update-job", "job-name", "job-update", add_option_dict)
