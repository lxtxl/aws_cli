#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/update-conditional-forwarder.html
if __name__ == '__main__':
    """
	create-conditional-forwarder : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/create-conditional-forwarder.html
	delete-conditional-forwarder : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/delete-conditional-forwarder.html
	describe-conditional-forwarders : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/describe-conditional-forwarders.html
    """

    parameter_display_string = """
    # directory-id : The directory ID of the AWS directory for which to update the conditional forwarder.
    # remote-domain-name : The fully qualified domain name (FQDN) of the remote domain with which you will set up a trust relationship.
    # dns-ip-addrs : The updated IP addresses of the remote DNS server associated with the conditional forwarder.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("ds", "update-conditional-forwarder", "directory-id", "remote-domain-name", "dns-ip-addrs", add_option_dict)
