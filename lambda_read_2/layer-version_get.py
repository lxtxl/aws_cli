#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-layer-version.html
if __name__ == '__main__':
    """
	delete-layer-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-layer-version.html
	list-layer-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-layer-versions.html
	publish-layer-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/publish-layer-version.html
    """

    parameter_display_string = """
    # layer-name : The name or Amazon Resource Name (ARN) of the layer.
    # version-number : 
    """

    execute_two_parameter("lambda", "get-layer-version", "layer-name", "version-number", parameter_display_string)