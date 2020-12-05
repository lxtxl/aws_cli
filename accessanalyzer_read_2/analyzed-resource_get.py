#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/get-analyzed-resource.html
if __name__ == '__main__':
    """
	list-analyzed-resources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/list-analyzed-resources.html
    """

    parameter_display_string = """
    # analyzer-arn : The ARN of the analyzer to retrieve information from.
    # resource-arn : The ARN of the resource to retrieve information about.
    """

    execute_two_parameter("accessanalyzer", "get-analyzed-resource", "analyzer-arn", "resource-arn", parameter_display_string)