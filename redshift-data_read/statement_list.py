#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-data/list-statements.html
if __name__ == '__main__':
    """
	cancel-statement : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-data/cancel-statement.html
	describe-statement : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-data/describe-statement.html
	execute-statement : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-data/execute-statement.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("redshift-data", "list-statements", add_option_dict)