#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-code-repository.html
if __name__ == '__main__':
    """
	delete-code-repository : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-code-repository.html
	describe-code-repository : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-code-repository.html
	list-code-repositories : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-code-repositories.html
	update-code-repository : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-code-repository.html
    """

    parameter_display_string = """
    # code-repository-name : The name of the Git repository. The name must have 1 to 63 characters. Valid characters are a-z, A-Z, 0-9, and - (hyphen).
    # git-config : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sagemaker", "create-code-repository", "code-repository-name", "git-config", add_option_dict)
