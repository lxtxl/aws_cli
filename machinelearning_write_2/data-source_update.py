#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/update-data-source.html
if __name__ == '__main__':
    """
	delete-data-source : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/delete-data-source.html
	describe-data-sources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/describe-data-sources.html
	get-data-source : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/get-data-source.html
    """

    parameter_display_string = """
    # data-source-id : The ID assigned to the DataSource during creation.
    # data-source-name : A new user-supplied name or description of the DataSource that will replace the current description.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("machinelearning", "update-data-source", "data-source-id", "data-source-name", add_option_dict)
