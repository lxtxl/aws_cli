#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-gateway-capability-configuration.html
if __name__ == '__main__':
    """
	update-gateway-capability-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/update-gateway-capability-configuration.html
    """

    parameter_display_string = """
    # gateway-id : The ID of the gateway that defines the capability configuration.
    # capability-namespace : The namespace of the capability configuration. For example, if you configure OPC-UA sources from the AWS IoT SiteWise console, your OPC-UA capability configuration has the namespace iotsitewise:opcuacollector:version , where version is a number such as 1 .
    """

    execute_two_parameter("iotsitewise", "describe-gateway-capability-configuration", "gateway-id", "capability-namespace", parameter_display_string)