#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/delete-apps-list.html
if __name__ == '__main__':
    """
	get-apps-list : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/get-apps-list.html
	list-apps-lists : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/list-apps-lists.html
	put-apps-list : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/put-apps-list.html
    """

    parameter_display_string = """
    # list-id : The ID of the applications list that you want to delete. You can retrieve this ID from PutAppsList , ListAppsLists , and GetAppsList .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("fms", "delete-apps-list", "list-id", add_option_dict)





