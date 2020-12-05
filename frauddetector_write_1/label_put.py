#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/put-label.html
if __name__ == '__main__':
    """
	delete-label : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-label.html
	get-labels : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-labels.html
    """

    parameter_display_string = """
    # name : The label name.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("frauddetector", "put-label", "name", add_option_dict)





