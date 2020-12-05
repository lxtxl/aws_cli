#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/delete-dataset-group.html
if __name__ == '__main__':
    """
	create-dataset-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/create-dataset-group.html
	describe-dataset-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/describe-dataset-group.html
	list-dataset-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/list-dataset-groups.html
    """

    parameter_display_string = """
    # dataset-group-arn : The ARN of the dataset group to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("personalize", "delete-dataset-group", "dataset-group-arn", add_option_dict)





