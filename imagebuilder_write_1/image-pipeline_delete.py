#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/delete-image-pipeline.html
if __name__ == '__main__':
    """
	create-image-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-image-pipeline.html
	get-image-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-image-pipeline.html
	list-image-pipelines : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-image-pipelines.html
	update-image-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/update-image-pipeline.html
    """

    parameter_display_string = """
    # image-pipeline-arn : The Amazon Resource Name (ARN) of the image pipeline to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("imagebuilder", "delete-image-pipeline", "image-pipeline-arn", add_option_dict)





