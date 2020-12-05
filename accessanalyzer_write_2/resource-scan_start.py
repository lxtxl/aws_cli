#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/start-resource-scan.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # analyzer-arn : The ARN of the analyzer to use to scan the policies applied to the specified resource.
    # resource-arn : The ARN of the resource to scan.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("accessanalyzer", "start-resource-scan", "analyzer-arn", "resource-arn", add_option_dict)
