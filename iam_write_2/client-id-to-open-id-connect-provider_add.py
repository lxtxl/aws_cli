#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/add-client-id-to-open-id-connect-provider.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # open-id-connect-provider-arn : The Amazon Resource Name (ARN) of the IAM OpenID Connect (OIDC) provider resource to add the client ID to. You can get a list of OIDC provider ARNs by using the  ListOpenIDConnectProviders operation.
    # client-id : The client ID (also known as audience) to add to the IAM OpenID Connect provider resource.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iam", "add-client-id-to-open-id-connect-provider", "open-id-connect-provider-arn", "client-id", add_option_dict)
