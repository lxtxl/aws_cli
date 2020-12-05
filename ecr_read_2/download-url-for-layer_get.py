#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/get-download-url-for-layer.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # repository-name : The name of the repository that is associated with the image layer to download.
    # layer-digest : The digest of the image layer to download.
    """

    execute_two_parameter("ecr", "get-download-url-for-layer", "repository-name", "layer-digest", parameter_display_string)