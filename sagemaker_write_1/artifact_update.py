#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-artifact.html
if __name__ == '__main__':
    """
	create-artifact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-artifact.html
	delete-artifact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-artifact.html
	describe-artifact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-artifact.html
	list-artifacts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-artifacts.html
    """

    parameter_display_string = """
    # artifact-arn : The Amazon Resource Name (ARN) of the artifact to update.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("sagemaker", "update-artifact", "artifact-arn", add_option_dict)





