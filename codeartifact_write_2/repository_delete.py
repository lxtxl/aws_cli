#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/delete-repository.html
if __name__ == '__main__':
    """
	create-repository : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/create-repository.html
	describe-repository : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/describe-repository.html
	list-repositories : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/list-repositories.html
	update-repository : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/update-repository.html
    """

    parameter_display_string = """
    # domain : The name of the domain that contains the repository to delete.
    # repository : The name of the repository to delete.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("codeartifact", "delete-repository", "domain", "repository", add_option_dict)
