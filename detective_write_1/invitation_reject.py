#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/reject-invitation.html
if __name__ == '__main__':
    """
	accept-invitation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/accept-invitation.html
	list-invitations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/list-invitations.html
    """

    parameter_display_string = """
    # graph-arn : The ARN of the behavior graph to reject the invitation to.
The member accountâs current member status in the behavior graph must be INVITED .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("detective", "reject-invitation", "graph-arn", add_option_dict)





