#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/stop-entities-detection-v2-job.html
if __name__ == '__main__':
    """
	describe-entities-detection-v2-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/describe-entities-detection-v2-job.html
	list-entities-detection-v2-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/list-entities-detection-v2-jobs.html
	start-entities-detection-v2-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/start-entities-detection-v2-job.html
    """

    parameter_display_string = """
    # job-id : The identifier of the medical entities job to stop.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("comprehendmedical", "stop-entities-detection-v2-job", "job-id", add_option_dict)





