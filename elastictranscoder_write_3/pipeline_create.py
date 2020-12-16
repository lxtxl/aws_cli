#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elastictranscoder/create-pipeline.html
if __name__ == '__main__':
    """
	delete-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elastictranscoder/delete-pipeline.html
	list-pipelines : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elastictranscoder/list-pipelines.html
	read-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elastictranscoder/read-pipeline.html
	update-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elastictranscoder/update-pipeline.html
    """

    parameter_display_string = """
    # name : The name of the pipeline. We recommend that the name be unique within the AWS account, but uniqueness is not enforced.
Constraints: Maximum 40 characters.
    # input-bucket : The Amazon S3 bucket in which you saved the media files that you want to transcode.
    # role : The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to create the pipeline.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("elastictranscoder", "create-pipeline", "name", "input-bucket", "role", add_option_dict)
