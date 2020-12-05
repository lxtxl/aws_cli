#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elastictranscoder/cancel-job.html
if __name__ == '__main__':
    """
	create-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elastictranscoder/create-job.html
	read-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elastictranscoder/read-job.html
    """

    parameter_display_string = """
    # id : The identifier of the job that you want to cancel.
To get a list of the jobs (including their jobId ) that have a status of Submitted , use the  ListJobsByStatus API action.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("elastictranscoder", "cancel-job", "id", add_option_dict)





