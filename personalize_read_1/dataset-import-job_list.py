#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/describe-dataset-import-job.html
if __name__ == '__main__':
    """
	create-dataset-import-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/create-dataset-import-job.html
	list-dataset-import-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/list-dataset-import-jobs.html
    """

    parameter_display_string = """
    # dataset-import-job-arn : The Amazon Resource Name (ARN) of the dataset import job to describe.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("personalize", "describe-dataset-import-job", "dataset-import-job-arn", add_option_dict)