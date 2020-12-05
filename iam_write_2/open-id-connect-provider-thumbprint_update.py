#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-open-id-connect-provider-thumbprint.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # open-id-connect-provider-arn : The Amazon Resource Name (ARN) of the IAM OIDC provider resource object for which you want to update the thumbprint. You can get a list of OIDC provider ARNs by using the  ListOpenIDConnectProviders operation.
For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
    # thumbprint-list : A list of certificate thumbprints that are associated with the specified IAM OpenID Connect provider. For more information, see  CreateOpenIDConnectProvider .
(string)

Contains a thumbprint for an identity providerâs server certificate.
The identity providerâs server certificate thumbprint is the hex-encoded SHA-1 hash value of the self-signed X.509 certificate. This thumbprint is used by the domain where the OpenID Connect provider makes its keys available. The thumbprint is always a 40-character string.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iam", "update-open-id-connect-provider-thumbprint", "open-id-connect-provider-arn", "thumbprint-list", add_option_dict)
