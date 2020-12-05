#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb/update-ledger.html
if __name__ == '__main__':
    """
	create-ledger : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb/create-ledger.html
	delete-ledger : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb/delete-ledger.html
	describe-ledger : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb/describe-ledger.html
	list-ledgers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb/list-ledgers.html
    """

    parameter_display_string = """
    # name : The name of the ledger.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("qldb", "update-ledger", "name", add_option_dict)





