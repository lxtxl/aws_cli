#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr-public/batch-delete-image.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # repository-name : The repository in a public registry that contains the image to delete.
    # image-ids : A list of image ID references that correspond to images to delete. The format of the imageIds reference is imageTag=tag or imageDigest=digest .
(structure)

An object with identifying information for an Amazon ECR image.
imageDigest -> (string)

The sha256 digest of the image manifest.

imageTag -> (string)

The tag used for the image.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ecr-public", "batch-delete-image", "repository-name", "image-ids", add_option_dict)
