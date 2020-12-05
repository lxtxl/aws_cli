#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-web-acl.html
if __name__ == '__main__':
    """
	associate-web-acl : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/associate-web-acl.html
	create-web-acl : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/create-web-acl.html
	delete-web-acl : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/delete-web-acl.html
	disassociate-web-acl : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/disassociate-web-acl.html
	list-web-acls : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-web-acls.html
	update-web-acl : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-web-acl.html
    """

    parameter_display_string = """
    # web-acl-id : The WebACLId of the  WebACL that you want to get. WebACLId is returned by  CreateWebACL and by  ListWebACLs .
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

    execute_one_parameter("waf-regional", "get-web-acl", "web-acl-id", add_option_dict)