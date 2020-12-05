#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/remove-flow-source.html
if __name__ == '__main__':
    """
	add-flow-sources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/add-flow-sources.html
	update-flow-source : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/update-flow-source.html
    """

    parameter_display_string = """
    # flow-arn : The flow that you want to remove a source from.
    # source-arn : The ARN of the source that you want to remove.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("mediaconnect", "remove-flow-source", "flow-arn", "source-arn", add_option_dict)
