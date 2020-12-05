#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/delete-protocols-list.html
if __name__ == '__main__':
    """
	get-protocols-list : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/get-protocols-list.html
	list-protocols-lists : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/list-protocols-lists.html
	put-protocols-list : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/put-protocols-list.html
    """

    parameter_display_string = """
    # list-id : The ID of the protocols list that you want to delete. You can retrieve this ID from PutProtocolsList , ListProtocolsLists , and GetProtocolsLost .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("fms", "delete-protocols-list", "list-id", add_option_dict)





