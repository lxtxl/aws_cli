#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/list-applications.html
if __name__ == '__main__':
    """
	create-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/create-application.html
	delete-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/delete-application.html
	get-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/get-application.html
	update-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/update-application.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("appconfig", "list-applications", add_option_dict)