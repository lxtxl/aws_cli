#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/remove-client-id-from-open-id-connect-provider.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # open-id-connect-provider-arn : The Amazon Resource Name (ARN) of the IAM OIDC provider resource to remove the client ID from. You can get a list of OIDC provider ARNs by using the  ListOpenIDConnectProviders operation.
For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
    # client-id : The client ID (also known as audience) to remove from the IAM OIDC provider resource. For more information about client IDs, see  CreateOpenIDConnectProvider .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iam", "remove-client-id-from-open-id-connect-provider", "open-id-connect-provider-arn", "client-id", add_option_dict)
