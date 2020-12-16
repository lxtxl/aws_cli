#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-container-service.html
if __name__ == '__main__':
    """
	delete-container-service : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-container-service.html
	get-container-services : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-container-services.html
	update-container-service : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/update-container-service.html
    """

    parameter_display_string = """
    # service-name : The name for the container service.
The name that you specify for your container service will make up part of its default domain. The default domain of a container service is typically https://<ServiceName>.<RandomGUID>.<AWSRegion>.cs.amazonlightsail.com . If the name of your container service is container-service-1 , and itâs located in the US East (Ohio) AWS region (us-east-2 ), then the domain for your container service will be like the following example: https://container-service-1.ur4EXAMPLE2uq.us-east-2.cs.amazonlightsail.com
The following are the requirements for container service names:

Must be unique within each AWS Region in your Lightsail account.
Must contain 1 to 63 characters.
Must contain only alphanumeric characters and hyphens.
A hyphen (-) can separate words but cannot be at the start or end of the name.
    # power : The power specification for the container service.
The power specifies the amount of memory, vCPUs, and base monthly cost of each node of the container service. The power and scale of a container service makes up its configured capacity. To determine the monthly price of your container service, multiply the base price of the power with the scale (the number of nodes) of the service.
Use the GetContainerServicePowers action to get a list of power options that you can specify using this parameter, and their base monthly cost.
Possible values:

nano
micro
small
medium
large
xlarge
    # scale : The scale specification for the container service.
The scale specifies the allocated compute nodes of the container service. The power and scale of a container service makes up its configured capacity. To determine the monthly price of your container service, multiply the base price of the power with the scale (the number of nodes) of the service.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("lightsail", "create-container-service", "service-name", "power", "scale", add_option_dict)
