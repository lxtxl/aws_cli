#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/delete-log-subscription.html
if __name__ == '__main__':
    """
	create-log-subscription : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/create-log-subscription.html
	list-log-subscriptions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/list-log-subscriptions.html
    """

    parameter_display_string = """
    # directory-id : Identifier of the directory whose log subscription you want to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ds", "delete-log-subscription", "directory-id", add_option_dict)





