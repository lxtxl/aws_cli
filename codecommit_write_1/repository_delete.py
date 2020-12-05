#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/delete-repository.html
if __name__ == '__main__':
    """
	create-repository : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/create-repository.html
	get-repository : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-repository.html
	list-repositories : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/list-repositories.html
    """

    parameter_display_string = """
    # repository-name : The name of the repository to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("codecommit", "delete-repository", "repository-name", add_option_dict)





