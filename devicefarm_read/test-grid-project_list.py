#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/list-test-grid-projects.html
if __name__ == '__main__':
    """
	create-test-grid-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/create-test-grid-project.html
	delete-test-grid-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/delete-test-grid-project.html
	get-test-grid-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/get-test-grid-project.html
	update-test-grid-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/update-test-grid-project.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("devicefarm", "list-test-grid-projects", add_option_dict)