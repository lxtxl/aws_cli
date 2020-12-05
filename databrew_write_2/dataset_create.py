#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/create-dataset.html
if __name__ == '__main__':
    """
	delete-dataset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/delete-dataset.html
	describe-dataset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/describe-dataset.html
	list-datasets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/list-datasets.html
	update-dataset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/update-dataset.html
    """

    parameter_display_string = """
    # name : The name of the dataset to be created.
    # input : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("databrew", "create-dataset", "name", "input", add_option_dict)
