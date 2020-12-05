#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/create-test-grid-project.html
if __name__ == '__main__':
    """
	delete-test-grid-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/delete-test-grid-project.html
	get-test-grid-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/get-test-grid-project.html
	list-test-grid-projects : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/list-test-grid-projects.html
	update-test-grid-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/update-test-grid-project.html
    """

    parameter_display_string = """
    # name : Human-readable name of the Selenium testing project.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("devicefarm", "create-test-grid-project", "name", add_option_dict)





