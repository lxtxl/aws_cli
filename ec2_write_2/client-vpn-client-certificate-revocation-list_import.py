#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/import-client-vpn-client-certificate-revocation-list.html
if __name__ == '__main__':
    """
	export-client-vpn-client-certificate-revocation-list : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/export-client-vpn-client-certificate-revocation-list.html
    """

    parameter_display_string = """
    # client-vpn-endpoint-id : The ID of the Client VPN endpoint to which the client certificate revocation list applies.
    # certificate-revocation-list : The client certificate revocation list file. For more information, see Generate a Client Certificate Revocation List in the AWS Client VPN Administrator Guide .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "import-client-vpn-client-certificate-revocation-list", "client-vpn-endpoint-id", "certificate-revocation-list", add_option_dict)
