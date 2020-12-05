#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/get-exclusions-preview.html
if __name__ == '__main__':
    """
	create-exclusions-preview : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/create-exclusions-preview.html
    """

    parameter_display_string = """
    # assessment-template-arn : The ARN that specifies the assessment template for which the exclusions preview was requested.
    # preview-token : The unique identifier associated of the exclusions preview.
    """

    execute_two_parameter("inspector", "get-exclusions-preview", "assessment-template-arn", "preview-token", parameter_display_string)