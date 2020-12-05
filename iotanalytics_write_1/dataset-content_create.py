#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/create-dataset-content.html
if __name__ == '__main__':
    """
	delete-dataset-content : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/delete-dataset-content.html
	get-dataset-content : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/get-dataset-content.html
	list-dataset-contents : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/list-dataset-contents.html
    """

    parameter_display_string = """
    # dataset-name : The name of the dataset.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iotanalytics", "create-dataset-content", "dataset-name", add_option_dict)





