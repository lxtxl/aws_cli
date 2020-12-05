#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/get-transcription-job.html
if __name__ == '__main__':
    """
	delete-transcription-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/delete-transcription-job.html
	list-transcription-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/list-transcription-jobs.html
	start-transcription-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/start-transcription-job.html
    """

    parameter_display_string = """
    # transcription-job-name : The name of the job.
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

    execute_one_parameter("transcribe", "get-transcription-job", "transcription-job-name", add_option_dict)