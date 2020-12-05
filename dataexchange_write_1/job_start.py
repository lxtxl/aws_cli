#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/start-job.html
if __name__ == '__main__':
    """
	cancel-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/cancel-job.html
	create-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/create-job.html
	get-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/get-job.html
	list-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/list-jobs.html
    """

    parameter_display_string = """
    # job-id : The unique identifier for a job.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("dataexchange", "start-job", "job-id", add_option_dict)





