#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/stop-icd10-cm-inference-job.html
if __name__ == '__main__':
    """
	describe-icd10-cm-inference-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/describe-icd10-cm-inference-job.html
	list-icd10-cm-inference-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/list-icd10-cm-inference-jobs.html
	start-icd10-cm-inference-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/start-icd10-cm-inference-job.html
    """

    parameter_display_string = """
    # job-id : The identifier of the job.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("comprehendmedical", "stop-icd10-cm-inference-job", "job-id", add_option_dict)





