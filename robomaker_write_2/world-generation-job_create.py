#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/create-world-generation-job.html
if __name__ == '__main__':
    """
	cancel-world-generation-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/cancel-world-generation-job.html
	describe-world-generation-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/describe-world-generation-job.html
	list-world-generation-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/list-world-generation-jobs.html
    """

    parameter_display_string = """
    # template : The Amazon Resource Name (arn) of the world template describing the worlds you want to create.
    # world-count : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("robomaker", "create-world-generation-job", "template", "world-count", add_option_dict)
