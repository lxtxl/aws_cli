#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/delete-medical-transcription-job.html
if __name__ == '__main__':
    """
	get-medical-transcription-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/get-medical-transcription-job.html
	list-medical-transcription-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/list-medical-transcription-jobs.html
	start-medical-transcription-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/start-medical-transcription-job.html
    """

    parameter_display_string = """
    # medical-transcription-job-name : The name you provide to the DeleteMedicalTranscriptionJob object to delete a transcription job.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("transcribe", "delete-medical-transcription-job", "medical-transcription-job-name", add_option_dict)





