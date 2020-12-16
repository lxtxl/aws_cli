#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr-public/complete-layer-upload.html
if __name__ == '__main__':
    """
	initiate-layer-upload : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr-public/initiate-layer-upload.html
    """

    parameter_display_string = """
    # repository-name : The name of the repository in a public registry to associate with the image layer.
    # upload-id : The upload ID from a previous  InitiateLayerUpload operation to associate with the image layer.
    # layer-digests : The sha256 digest of the image layer.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("ecr-public", "complete-layer-upload", "repository-name", "upload-id", "layer-digests", add_option_dict)
