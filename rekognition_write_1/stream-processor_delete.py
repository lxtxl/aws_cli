#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/delete-stream-processor.html
if __name__ == '__main__':
    """
	create-stream-processor : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/create-stream-processor.html
	describe-stream-processor : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/describe-stream-processor.html
	list-stream-processors : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/list-stream-processors.html
	start-stream-processor : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/start-stream-processor.html
	stop-stream-processor : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/stop-stream-processor.html
    """

    parameter_display_string = """
    # name : The name of the stream processor you want to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("rekognition", "delete-stream-processor", "name", add_option_dict)





