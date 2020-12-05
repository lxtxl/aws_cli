#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	get-medical-transcription-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/get-medical-transcription-job.html
	list-medical-transcription-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/list-medical-transcription-jobs.html
	start-medical-transcription-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/start-medical-transcription-job.html
    """

    write_parameter("transcribe", "delete-medical-transcription-job")