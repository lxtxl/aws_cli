#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/delete-solution.html
if __name__ == '__main__':
    """
	create-solution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/create-solution.html
	describe-solution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/describe-solution.html
	list-solutions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/list-solutions.html
    """

    parameter_display_string = """
    # solution-arn : The ARN of the solution to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("personalize", "delete-solution", "solution-arn", add_option_dict)





