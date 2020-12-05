#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/list-dataset-contents.html
if __name__ == '__main__':
    """
	create-dataset-content : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/create-dataset-content.html
	delete-dataset-content : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/delete-dataset-content.html
	get-dataset-content : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/get-dataset-content.html
    """

    parameter_display_string = """
    # dataset-name : The name of the data set whose contents information you want to list.
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

    execute_one_parameter("iotanalytics", "list-dataset-contents", "dataset-name", add_option_dict)