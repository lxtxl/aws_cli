#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/stop-data-collection-by-agent-ids.html
if __name__ == '__main__':
    """
	start-data-collection-by-agent-ids : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/start-data-collection-by-agent-ids.html
    """

    parameter_display_string = """
    # agent-ids : The IDs of the agents or connectors from which to stop collecting data.
(string)
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("discovery", "stop-data-collection-by-agent-ids", "agent-ids", add_option_dict)





