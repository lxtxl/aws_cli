#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-workforce.html
if __name__ == '__main__':
    """
	delete-workforce : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-workforce.html
	describe-workforce : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-workforce.html
	list-workforces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-workforces.html
	update-workforce : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-workforce.html
    """

    parameter_display_string = """
    # workforce-name : The name of the private workforce.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("sagemaker", "create-workforce", "workforce-name", add_option_dict)





