#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/create-agent.html
if __name__ == '__main__':
    """
	delete-agent : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/delete-agent.html
	describe-agent : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/describe-agent.html
	list-agents : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/list-agents.html
	update-agent : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/update-agent.html
    """

    parameter_display_string = """
    # activation-key : Your agent activation key. You can get the activation key either by sending an HTTP GET request with redirects that enable you to get the agent IP address (port 80). Alternatively, you can get it from the AWS DataSync console.
The redirect URL returned in the response provides you the activation key for your agent in the query string parameter activationKey . It might also include other activation-related parameters; however, these are merely defaults. The arguments you pass to this API call determine the actual configuration of your agent.
For more information, see Activating an Agent in the AWS DataSync User Guide.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("datasync", "create-agent", "activation-key", add_option_dict)





