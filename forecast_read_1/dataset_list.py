#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/describe-dataset.html
if __name__ == '__main__':
    """
	create-dataset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/create-dataset.html
	delete-dataset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/delete-dataset.html
	list-datasets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/list-datasets.html
    """

    parameter_display_string = """
    # dataset-arn : The Amazon Resource Name (ARN) of the dataset.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("forecast", "describe-dataset", "dataset-arn", add_option_dict)