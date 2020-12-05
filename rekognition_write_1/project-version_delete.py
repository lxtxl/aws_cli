#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/delete-project-version.html
if __name__ == '__main__':
    """
	create-project-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/create-project-version.html
	describe-project-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/describe-project-versions.html
	start-project-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/start-project-version.html
	stop-project-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/stop-project-version.html
    """

    parameter_display_string = """
    # project-version-arn : The Amazon Resource Name (ARN) of the model version that you want to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("rekognition", "delete-project-version", "project-version-arn", add_option_dict)





