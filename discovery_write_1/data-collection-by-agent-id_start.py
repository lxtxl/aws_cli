#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/start-data-collection-by-agent-ids.html
if __name__ == '__main__':
    """
	stop-data-collection-by-agent-ids : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/stop-data-collection-by-agent-ids.html
    """

    parameter_display_string = """
    # agent-ids : The IDs of the agents or connectors from which to start collecting data. If you send a request to an agent/connector ID that you do not have permission to contact, according to your AWS account, the service does not throw an exception. Instead, it returns the error in the Description field. If you send a request to multiple agents/connectors and you do not have permission to contact some of those agents/connectors, the system does not throw an exception. Instead, the system shows Failed in the Description field.
(string)
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("discovery", "start-data-collection-by-agent-ids", "agent-ids", add_option_dict)





