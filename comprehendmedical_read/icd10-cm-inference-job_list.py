#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/list-icd10-cm-inference-jobs.html
if __name__ == '__main__':
    """
	describe-icd10-cm-inference-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/describe-icd10-cm-inference-job.html
	start-icd10-cm-inference-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/start-icd10-cm-inference-job.html
	stop-icd10-cm-inference-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/stop-icd10-cm-inference-job.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("comprehendmedical", "list-icd10-cm-inference-jobs", add_option_dict)