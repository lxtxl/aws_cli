#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/create-location-object-storage.html
if __name__ == '__main__':
    """
	describe-location-object-storage : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/describe-location-object-storage.html
    """

    parameter_display_string = """
    # server-hostname : The name of the self-managed object storage server. This value is the IP address or Domain Name Service (DNS) name of the object storage server. An agent uses this host name to mount the object storage server in a network.
    # bucket-name : The bucket on the self-managed object storage server that is used to read data from.
    # agent-arns : The Amazon Resource Name (ARN) of the agents associated with the self-managed object storage server location.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("datasync", "create-location-object-storage", "server-hostname", "bucket-name", "agent-arns", add_option_dict)
