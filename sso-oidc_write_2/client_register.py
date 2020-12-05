#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-oidc/register-client.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # client-name : The friendly name of the client.
    # client-type : The type of client. The service supports only public as a client type. Anything other than public will be rejected by the service.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sso-oidc", "register-client", "client-name", "client-type", add_option_dict)
