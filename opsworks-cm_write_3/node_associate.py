#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks-cm/associate-node.html
if __name__ == '__main__':
    """
	disassociate-node : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks-cm/disassociate-node.html
    """

    parameter_display_string = """
    # server-name : The name of the server with which to associate the node.
    # node-name : The name of the node.
    # engine-attributes : Engine attributes used for associating the node.

Attributes accepted in a AssociateNode request for Chef


CHEF_ORGANIZATION : The Chef organization with which the node is associated. By default only one organization named default can exist.
CHEF_NODE_PUBLIC_KEY : A PEM-formatted public key. This key is required for the chef-client agent to access the Chef API.


Attributes accepted in a AssociateNode request for Puppet


PUPPET_NODE_CSR : A PEM-formatted certificate-signing request (CSR) that is created by the node.

(structure)

A name and value pair that is specific to the engine of the server.
Name -> (string)

The name of the engine attribute.

Value -> (string)

The value of the engine attribute.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("opsworks-cm", "associate-node", "server-name", "node-name", "engine-attributes", add_option_dict)
