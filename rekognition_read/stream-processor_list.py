#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/list-stream-processors.html
if __name__ == '__main__':
    """
	create-stream-processor : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/create-stream-processor.html
	delete-stream-processor : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/delete-stream-processor.html
	describe-stream-processor : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/describe-stream-processor.html
	start-stream-processor : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/start-stream-processor.html
	stop-stream-processor : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/stop-stream-processor.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("rekognition", "list-stream-processors", add_option_dict)