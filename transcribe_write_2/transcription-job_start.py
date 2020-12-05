#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/start-transcription-job.html
if __name__ == '__main__':
    """
	delete-transcription-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/delete-transcription-job.html
	get-transcription-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/get-transcription-job.html
	list-transcription-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/list-transcription-jobs.html
    """

    parameter_display_string = """
    # transcription-job-name : The name of the job. You canât use the strings â. â or â.. â by themselves as the job name. The name must also be unique within an AWS account. If you try to create a transcription job with the same name as a previous transcription job, you get a ConflictException error.
    # media : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("transcribe", "start-transcription-job", "transcription-job-name", "media", add_option_dict)
