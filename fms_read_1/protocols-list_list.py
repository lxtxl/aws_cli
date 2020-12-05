#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/list-protocols-lists.html
if __name__ == '__main__':
    """
	delete-protocols-list : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/delete-protocols-list.html
	get-protocols-list : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/get-protocols-list.html
	put-protocols-list : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/put-protocols-list.html
    """

    parameter_display_string = """
    # max-results : The maximum number of objects that you want AWS Firewall Manager to return for this request. If more objects are available, in the response, AWS Firewall Manager provides a NextToken value that you can use in a subsequent call to get the next batch of objects.
If you donât specify this, AWS Firewall Manager returns all available objects.
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

    execute_one_parameter("fms", "list-protocols-lists", "max-results", add_option_dict)