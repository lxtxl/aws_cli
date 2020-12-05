#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/disassociate-membership.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # graph-arn : The ARN of the behavior graph to remove the member account from.
The member accountâs member status in the behavior graph must be ENABLED .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("detective", "disassociate-membership", "graph-arn", add_option_dict)





