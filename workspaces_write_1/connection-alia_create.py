#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/create-connection-alias.html
if __name__ == '__main__':
    """
	associate-connection-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/associate-connection-alias.html
	delete-connection-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/delete-connection-alias.html
	disassociate-connection-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/disassociate-connection-alias.html
    """

    parameter_display_string = """
    # connection-string : A connection string in the form of a fully qualified domain name (FQDN), such as www.example.com .

Warning
After you create a connection string, it is always associated to your AWS account. You cannot recreate the same connection string with a different account, even if you delete all instances of it from the original account. The connection string is globally reserved for your account.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("workspaces", "create-connection-alias", "connection-string", add_option_dict)





