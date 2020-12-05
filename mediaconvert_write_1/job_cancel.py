#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/cancel-job.html
if __name__ == '__main__':
    """
	create-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/create-job.html
	get-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/get-job.html
	list-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/list-jobs.html
    """

    parameter_display_string = """
    # id : The Job ID of the job to be cancelled.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("mediaconvert", "cancel-job", "id", add_option_dict)





