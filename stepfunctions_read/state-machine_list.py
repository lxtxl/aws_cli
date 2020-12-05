#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/list-state-machines.html
if __name__ == '__main__':
    """
	create-state-machine : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/create-state-machine.html
	delete-state-machine : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/delete-state-machine.html
	describe-state-machine : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/describe-state-machine.html
	update-state-machine : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/update-state-machine.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("stepfunctions", "list-state-machines", add_option_dict)