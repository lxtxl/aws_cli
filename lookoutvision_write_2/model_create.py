#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/create-model.html
if __name__ == '__main__':
    """
	delete-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/delete-model.html
	describe-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/describe-model.html
	list-models : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/list-models.html
	start-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/start-model.html
	stop-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/stop-model.html
    """

    parameter_display_string = """
    # project-name : The name of the project in which you want to create a model version.
    # output-config : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("lookoutvision", "create-model", "project-name", "output-config", add_option_dict)
