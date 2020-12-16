#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-a2i-runtime/start-human-loop.html
if __name__ == '__main__':
    """
	delete-human-loop : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-a2i-runtime/delete-human-loop.html
	describe-human-loop : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-a2i-runtime/describe-human-loop.html
	list-human-loops : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-a2i-runtime/list-human-loops.html
	stop-human-loop : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-a2i-runtime/stop-human-loop.html
    """

    parameter_display_string = """
    # human-loop-name : The name of the human loop.
    # flow-definition-arn : The Amazon Resource Name (ARN) of the flow definition associated with this human loop.
    # human-loop-input : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("sagemaker-a2i-runtime", "start-human-loop", "human-loop-name", "flow-definition-arn", "human-loop-input", add_option_dict)
