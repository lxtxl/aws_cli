#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appintegrations/list-event-integrations.html
if __name__ == '__main__':
    """
	create-event-integration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appintegrations/create-event-integration.html
	delete-event-integration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appintegrations/delete-event-integration.html
	get-event-integration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appintegrations/get-event-integration.html
	update-event-integration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appintegrations/update-event-integration.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("appintegrations", "list-event-integrations", add_option_dict)