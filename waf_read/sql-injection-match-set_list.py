#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-sql-injection-match-sets.html
if __name__ == '__main__':
    """
	create-sql-injection-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-sql-injection-match-set.html
	delete-sql-injection-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-sql-injection-match-set.html
	get-sql-injection-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-sql-injection-match-set.html
	update-sql-injection-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-sql-injection-match-set.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("waf", "list-sql-injection-match-sets", add_option_dict)