#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/describe-stream-processor.html
if __name__ == '__main__':
    """
	create-stream-processor : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/create-stream-processor.html
	delete-stream-processor : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/delete-stream-processor.html
	list-stream-processors : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/list-stream-processors.html
	start-stream-processor : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/start-stream-processor.html
	stop-stream-processor : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/stop-stream-processor.html
    """

    parameter_display_string = """
    # name : Name of the stream processor for which you want information.
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

    execute_one_parameter("rekognition", "describe-stream-processor", "name", add_option_dict)