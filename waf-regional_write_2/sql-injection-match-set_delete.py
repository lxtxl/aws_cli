#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/delete-sql-injection-match-set.html
if __name__ == '__main__':
    """
	create-sql-injection-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/create-sql-injection-match-set.html
	get-sql-injection-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-sql-injection-match-set.html
	list-sql-injection-match-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-sql-injection-match-sets.html
	update-sql-injection-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-sql-injection-match-set.html
    """

    parameter_display_string = """
    # sql-injection-match-set-id : The SqlInjectionMatchSetId of the  SqlInjectionMatchSet that you want to delete. SqlInjectionMatchSetId is returned by  CreateSqlInjectionMatchSet and by  ListSqlInjectionMatchSets .
    # change-token : The value returned by the most recent call to  GetChangeToken .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("waf-regional", "delete-sql-injection-match-set", "sql-injection-match-set-id", "change-token", add_option_dict)
