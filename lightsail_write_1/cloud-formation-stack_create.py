#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-cloud-formation-stack.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # instances : An array of parameters that will be used to create the new Amazon EC2 instance. You can only pass one instance entry at a time in this array. You will get an invalid parameter error if you pass more than one instance entry in this array.
(structure)

Describes the Amazon Elastic Compute Cloud instance and related resources to be created using the create cloud formation stack operation.
sourceName -> (string)

The name of the export snapshot record, which contains the exported Lightsail instance snapshot that will be used as the source of the new Amazon EC2 instance.
Use the get export snapshot records operation to get a list of export snapshot records that you can use to create a CloudFormation stack.

instanceType -> (string)

The instance type (e.g., t2.micro ) to use for the new Amazon EC2 instance.

portInfoSource -> (string)

The port configuration to use for the new Amazon EC2 instance.
The following configuration options are available:

DEFAULT - Use the default firewall settings from the Lightsail instance blueprint.
INSTANCE - Use the configured firewall settings from the source Lightsail instance.
NONE - Use the default Amazon EC2 security group.
CLOSED - All ports closed.


Note
If you configured lightsail-connect as a cidrListAliases on your instance, or if you chose to allow the Lightsail browser-based SSH or RDP clients to connect to your instance, that configuration is not carried over to your new Amazon EC2 instance.


userData -> (string)

A launch script you can create that configures a server with additional user data. For example, you might want to run apt-get -y update .

Note
Depending on the machine image you choose, the command to get software on your instance varies. Amazon Linux and CentOS use yum , Debian and Ubuntu use apt-get , and FreeBSD uses pkg .


availabilityZone -> (string)

The Availability Zone for the new Amazon EC2 instance.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("lightsail", "create-cloud-formation-stack", "instances", add_option_dict)





