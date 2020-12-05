#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb/describe-ledger.html
if __name__ == '__main__':
    """
	create-ledger : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb/create-ledger.html
	delete-ledger : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb/delete-ledger.html
	list-ledgers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb/list-ledgers.html
	update-ledger : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb/update-ledger.html
    """

    parameter_display_string = """
    # name : The name of the ledger that you want to describe.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("qldb", "describe-ledger", "name", add_option_dict)