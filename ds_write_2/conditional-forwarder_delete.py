#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/delete-conditional-forwarder.html
if __name__ == '__main__':
    """
	create-conditional-forwarder : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/create-conditional-forwarder.html
	describe-conditional-forwarders : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/describe-conditional-forwarders.html
	update-conditional-forwarder : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/update-conditional-forwarder.html
    """

    parameter_display_string = """
    # directory-id : The directory ID for which you are deleting the conditional forwarder.
    # remote-domain-name : The fully qualified domain name (FQDN) of the remote domain with which you are deleting the conditional forwarder.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ds", "delete-conditional-forwarder", "directory-id", "remote-domain-name", add_option_dict)
