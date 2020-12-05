#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/create-solution-version.html
if __name__ == '__main__':
    """
	describe-solution-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/describe-solution-version.html
	list-solution-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/list-solution-versions.html
    """

    parameter_display_string = """
    # solution-arn : The Amazon Resource Name (ARN) of the solution containing the training configuration information.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("personalize", "create-solution-version", "solution-arn", add_option_dict)





