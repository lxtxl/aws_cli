#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/create-dataflow-endpoint-group.html
if __name__ == '__main__':
    """
	delete-dataflow-endpoint-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/delete-dataflow-endpoint-group.html
	get-dataflow-endpoint-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/get-dataflow-endpoint-group.html
	list-dataflow-endpoint-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/list-dataflow-endpoint-groups.html
    """

    parameter_display_string = """
    # endpoint-details : Endpoint details of each endpoint in the dataflow endpoint group.
(structure)

Information about the endpoint details.
endpoint -> (structure)

A dataflow endpoint.
address -> (structure)

Socket address of a dataflow endpoint.
name -> (string)

Name of a socket address.

port -> (integer)

Port of a socket address.


mtu -> (integer)

Maximum transmission unit (MTU) size in bytes of a dataflow endpoint.

name -> (string)

Name of a dataflow endpoint.

status -> (string)

Status of a dataflow endpoint.


securityDetails -> (structure)

Endpoint security details.
roleArn -> (string)

ARN to a role needed for connecting streams to your instances.

securityGroupIds -> (list)

The security groups to attach to the elastic network interfaces.
(string)

subnetIds -> (list)

A list of subnets where AWS Ground Station places elastic network interfaces to send streams to your instances.
(string)
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("groundstation", "create-dataflow-endpoint-group", "endpoint-details", add_option_dict)





