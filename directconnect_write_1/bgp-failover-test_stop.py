#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/stop-bgp-failover-test.html
if __name__ == '__main__':
    """
	start-bgp-failover-test : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/start-bgp-failover-test.html
    """

    parameter_display_string = """
    # virtual-interface-id : The ID of the virtual interface you no longer want to test.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("directconnect", "stop-bgp-failover-test", "virtual-interface-id", add_option_dict)





