#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-image-version.html
if __name__ == '__main__':
    """
	delete-image-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-image-version.html
	describe-image-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-image-version.html
	list-image-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-image-versions.html
    """

    parameter_display_string = """
    # base-image : The registry path of the container image to use as the starting point for this version. The path is an Amazon Container Registry (ECR) URI in the following format:

<acct-id>.dkr.ecr.<region>.amazonaws.com/<repo-name[:tag] or [@digest]>
    # image-name : The ImageName of the Image to create a version of.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sagemaker", "create-image-version", "base-image", "image-name", add_option_dict)
