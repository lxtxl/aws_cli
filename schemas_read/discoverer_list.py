#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/list-discoverers.html
if __name__ == '__main__':
    """
	create-discoverer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/create-discoverer.html
	delete-discoverer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/delete-discoverer.html
	describe-discoverer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/describe-discoverer.html
	start-discoverer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/start-discoverer.html
	stop-discoverer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/stop-discoverer.html
	update-discoverer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/update-discoverer.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("schemas", "list-discoverers", add_option_dict)