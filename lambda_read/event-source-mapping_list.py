#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-event-source-mappings.html
if __name__ == '__main__':
    """
	create-event-source-mapping : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-event-source-mapping.html
	delete-event-source-mapping : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-event-source-mapping.html
	get-event-source-mapping : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-event-source-mapping.html
	update-event-source-mapping : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-event-source-mapping.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("lambda", "list-event-source-mappings", add_option_dict)