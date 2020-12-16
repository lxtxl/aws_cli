#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/attach-volume.html
if __name__ == '__main__':
    """
	delete-volume : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/delete-volume.html
	detach-volume : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/detach-volume.html
	list-volumes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/list-volumes.html
    """

    parameter_display_string = """
    # gateway-arn : The Amazon Resource Name (ARN) of the gateway that you want to attach the volume to.
    # volume-arn : The Amazon Resource Name (ARN) of the volume to attach to the specified gateway.
    # network-interface-id : The network interface of the gateway on which to expose the iSCSI target. Only IPv4 addresses are accepted. Use  DescribeGatewayInformation to get a list of the network interfaces available on a gateway.
Valid Values: A valid IP address.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("storagegateway", "attach-volume", "gateway-arn", "volume-arn", "network-interface-id", add_option_dict)
