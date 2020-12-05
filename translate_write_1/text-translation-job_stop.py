#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/stop-text-translation-job.html
if __name__ == '__main__':
    """
	describe-text-translation-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/describe-text-translation-job.html
	list-text-translation-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/list-text-translation-jobs.html
	start-text-translation-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/start-text-translation-job.html
    """

    parameter_display_string = """
    # job-id : The job ID of the job to be stopped.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("translate", "stop-text-translation-job", "job-id", add_option_dict)





