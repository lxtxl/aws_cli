#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-pipeline.html
if __name__ == '__main__':
    """
	delete-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-pipeline.html
	describe-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-pipeline.html
	list-pipelines : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-pipelines.html
	update-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-pipeline.html
    """

    parameter_display_string = """
    # pipeline-name : The name of the pipeline.
    # pipeline-definition : The JSON pipeline definition of the pipeline.
    # role-arn : The Amazon Resource Name (ARN) of the role used by the pipeline to access and create resources.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("sagemaker", "create-pipeline", "pipeline-name", "pipeline-definition", "role-arn", add_option_dict)
