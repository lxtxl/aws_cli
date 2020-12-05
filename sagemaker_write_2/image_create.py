#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-image.html
if __name__ == '__main__':
    """
	delete-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-image.html
	describe-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-image.html
	list-images : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-images.html
	update-image : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-image.html
    """

    parameter_display_string = """
    # image-name : The name of the image. Must be unique to your account.
    # role-arn : The Amazon Resource Name (ARN) of an IAM role that enables Amazon SageMaker to perform tasks on your behalf.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sagemaker", "create-image", "image-name", "role-arn", add_option_dict)
