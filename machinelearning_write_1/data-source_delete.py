#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/delete-data-source.html
if __name__ == '__main__':
    """
	describe-data-sources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/describe-data-sources.html
	get-data-source : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/get-data-source.html
	update-data-source : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/update-data-source.html
    """

    parameter_display_string = """
    # data-source-id : A user-supplied ID that uniquely identifies the DataSource .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("machinelearning", "delete-data-source", "data-source-id", add_option_dict)





