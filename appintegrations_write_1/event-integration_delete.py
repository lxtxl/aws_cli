#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appintegrations/delete-event-integration.html
if __name__ == '__main__':
    """
	create-event-integration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appintegrations/create-event-integration.html
	get-event-integration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appintegrations/get-event-integration.html
	list-event-integrations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appintegrations/list-event-integrations.html
	update-event-integration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appintegrations/update-event-integration.html
    """

    parameter_display_string = """
    # name : The name of the event integration.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("appintegrations", "delete-event-integration", "name", add_option_dict)





