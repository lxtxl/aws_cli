#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/list-multiplexes.html
if __name__ == '__main__':
    """
	create-multiplex : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/create-multiplex.html
	delete-multiplex : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/delete-multiplex.html
	describe-multiplex : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/describe-multiplex.html
	start-multiplex : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/start-multiplex.html
	stop-multiplex : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/stop-multiplex.html
	update-multiplex : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/update-multiplex.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("medialive", "list-multiplexes", add_option_dict)