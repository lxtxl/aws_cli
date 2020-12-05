#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/stop-pii-entities-detection-job.html
if __name__ == '__main__':
    """
	describe-pii-entities-detection-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/describe-pii-entities-detection-job.html
	list-pii-entities-detection-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/list-pii-entities-detection-jobs.html
	start-pii-entities-detection-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/start-pii-entities-detection-job.html
    """

    parameter_display_string = """
    # job-id : The identifier of the PII entities detection job to stop.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("comprehend", "stop-pii-entities-detection-job", "job-id", add_option_dict)





