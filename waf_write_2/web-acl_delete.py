#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-web-acl.html
if __name__ == '__main__':
    """
	create-web-acl : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-web-acl.html
	get-web-acl : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-web-acl.html
	list-web-acls : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-web-acls.html
	update-web-acl : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-web-acl.html
    """

    parameter_display_string = """
    # web-acl-id : The WebACLId of the  WebACL that you want to delete. WebACLId is returned by  CreateWebACL and by  ListWebACLs .
    # change-token : The value returned by the most recent call to  GetChangeToken .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("waf", "delete-web-acl", "web-acl-id", "change-token", add_option_dict)
