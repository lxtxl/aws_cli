#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-ip-set.html
if __name__ == '__main__':
    """
	create-ip-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-ip-set.html
	get-ip-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-ip-set.html
	list-ip-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-ip-sets.html
	update-ip-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-ip-set.html
    """

    parameter_display_string = """
    # ip-set-id : The IPSetId of the  IPSet that you want to delete. IPSetId is returned by  CreateIPSet and by  ListIPSets .
    # change-token : The value returned by the most recent call to  GetChangeToken .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("waf", "delete-ip-set", "ip-set-id", "change-token", add_option_dict)
