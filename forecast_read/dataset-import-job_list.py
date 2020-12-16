#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/list-dataset-import-jobs.html
if __name__ == '__main__':
    """
	create-dataset-import-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/create-dataset-import-job.html
	delete-dataset-import-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/delete-dataset-import-job.html
	describe-dataset-import-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/describe-dataset-import-job.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("forecast", "list-dataset-import-jobs", add_option_dict)