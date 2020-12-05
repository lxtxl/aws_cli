#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-job.html
if __name__ == '__main__':
    """
	create-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-job.html
	get-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-job.html
	get-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-jobs.html
	list-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/list-jobs.html
	update-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-job.html
    """

    parameter_display_string = """
    # job-name : The name of the job definition to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("glue", "delete-job", "job-name", add_option_dict)





