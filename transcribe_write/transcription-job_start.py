#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-transcription-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/delete-transcription-job.html
	get-transcription-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/get-transcription-job.html
	list-transcription-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/list-transcription-jobs.html
    """

    write_parameter("transcribe", "start-transcription-job")