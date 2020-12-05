#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/delete-dataset-group.html
if __name__ == '__main__':
    """
	create-dataset-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/create-dataset-group.html
	describe-dataset-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/describe-dataset-group.html
	list-dataset-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/list-dataset-groups.html
	update-dataset-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/update-dataset-group.html
    """

    parameter_display_string = """
    # dataset-group-arn : The Amazon Resource Name (ARN) of the dataset group to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("forecast", "delete-dataset-group", "dataset-group-arn", add_option_dict)





