#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/export-client-vpn-client-certificate-revocation-list.html
if __name__ == '__main__':
    """
	import-client-vpn-client-certificate-revocation-list : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/import-client-vpn-client-certificate-revocation-list.html
    """

    parameter_display_string = """
    # client-vpn-endpoint-id : The ID of the Client VPN endpoint.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "export-client-vpn-client-certificate-revocation-list", "client-vpn-endpoint-id", add_option_dict)





