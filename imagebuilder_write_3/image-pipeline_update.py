#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/update-image-pipeline.html
if __name__ == '__main__':
    """
	create-image-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-image-pipeline.html
	delete-image-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/delete-image-pipeline.html
	get-image-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-image-pipeline.html
	list-image-pipelines : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-image-pipelines.html
    """

    parameter_display_string = """
    # image-pipeline-arn : The Amazon Resource Name (ARN) of the image pipeline that you want to update.
    # image-recipe-arn : The Amazon Resource Name (ARN) of the image recipe that will be used to configure images updated by this image pipeline.
    # infrastructure-configuration-arn : The Amazon Resource Name (ARN) of the infrastructure configuration that will be used to build images updated by this image pipeline.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("imagebuilder", "update-image-pipeline", "image-pipeline-arn", "image-recipe-arn", "infrastructure-configuration-arn", add_option_dict)
