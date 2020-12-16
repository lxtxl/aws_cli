#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/update-gateway-capability-configuration.html
if __name__ == '__main__':
    """
	describe-gateway-capability-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-gateway-capability-configuration.html
    """

    parameter_display_string = """
    # gateway-id : The ID of the gateway to be updated.
    # capability-namespace : The namespace of the gateway capability configuration to be updated. For example, if you configure OPC-UA sources from the AWS IoT SiteWise console, your OPC-UA capability configuration has the namespace iotsitewise:opcuacollector:version , where version is a number such as 1 .
    # capability-configuration : The JSON document that defines the configuration for the gateway capability. For more information, see Configuring data sources (CLI) in the AWS IoT SiteWise User Guide .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("iotsitewise", "update-gateway-capability-configuration", "gateway-id", "capability-namespace", "capability-configuration", add_option_dict)
