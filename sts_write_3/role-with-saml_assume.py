#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/assume-role-with-saml.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # role-arn : The Amazon Resource Name (ARN) of the role that the caller is assuming.
    # principal-arn : The Amazon Resource Name (ARN) of the SAML provider in IAM that describes the IdP.
    # saml-assertion : The base-64 encoded SAML authentication response provided by the IdP.
For more information, see Configuring a Relying Party and Adding Claims in the IAM User Guide .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("sts", "assume-role-with-saml", "role-arn", "principal-arn", "saml-assertion", add_option_dict)
