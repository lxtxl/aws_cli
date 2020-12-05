#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/delete-agent.html
if __name__ == '__main__':
    """
	create-agent : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/create-agent.html
	describe-agent : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/describe-agent.html
	list-agents : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/list-agents.html
	update-agent : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/update-agent.html
    """

    parameter_display_string = """
    # agent-arn : The Amazon Resource Name (ARN) of the agent to delete. Use the ListAgents operation to return a list of agents for your account and AWS Region.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("datasync", "delete-agent", "agent-arn", add_option_dict)





