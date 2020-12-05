#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/list-agents.html
if __name__ == '__main__':
    """
	create-agent : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/create-agent.html
	delete-agent : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/delete-agent.html
	describe-agent : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/describe-agent.html
	update-agent : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/update-agent.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("datasync", "list-agents", add_option_dict)