#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/list-transcription-jobs.html
if __name__ == '__main__':
    """
	delete-transcription-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/delete-transcription-job.html
	get-transcription-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/get-transcription-job.html
	start-transcription-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/start-transcription-job.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("transcribe", "list-transcription-jobs", add_option_dict)