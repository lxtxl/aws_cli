#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb/create-ledger.html
if __name__ == '__main__':
    """
	delete-ledger : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb/delete-ledger.html
	describe-ledger : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb/describe-ledger.html
	list-ledgers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb/list-ledgers.html
	update-ledger : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb/update-ledger.html
    """

    parameter_display_string = """
    # name : The name of the ledger that you want to create. The name must be unique among all of your ledgers in the current AWS Region.
Naming constraints for ledger names are defined in Quotas in Amazon QLDB in the Amazon QLDB Developer Guide .
    # permissions-mode : The permissions mode to assign to the ledger that you want to create.
Possible values:

ALLOW_ALL
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("qldb", "create-ledger", "name", "permissions-mode", add_option_dict)
