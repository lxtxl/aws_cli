#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-open-id-connect-provider.html
if __name__ == '__main__':
    """
	delete-open-id-connect-provider : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-open-id-connect-provider.html
	get-open-id-connect-provider : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-open-id-connect-provider.html
	list-open-id-connect-providers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-open-id-connect-providers.html
    """

    parameter_display_string = """
    # url : The URL of the identity provider. The URL must begin with https:// and should correspond to the iss claim in the providerâs OpenID Connect ID tokens. Per the OIDC standard, path components are allowed but query parameters are not. Typically the URL consists of only a hostname, like https://server.example.org or https://example.com .
You cannot register the same provider multiple times in a single AWS account. If you try to submit a URL that has already been used for an OpenID Connect provider in the AWS account, you will get an error.
    # thumbprint-list : A list of server certificate thumbprints for the OpenID Connect (OIDC) identity providerâs server certificates. Typically this list includes only one entry. However, IAM lets you have up to five thumbprints for an OIDC provider. This lets you maintain multiple thumbprints if the identity provider is rotating certificates.
The server certificate thumbprint is the hex-encoded SHA-1 hash value of the X.509 certificate used by the domain where the OpenID Connect provider makes its keys available. It is always a 40-character string.
You must provide at least one thumbprint when creating an IAM OIDC provider. For example, assume that the OIDC provider is server.example.com and the provider stores its keys at https://keys.server.example.com/openid-connect. In that case, the thumbprint string would be the hex-encoded SHA-1 hash value of the certificate used by https://keys.server.example.com.
For more information about obtaining the OIDC providerâs thumbprint, see Obtaining the Thumbprint for an OpenID Connect Provider in the IAM User Guide .
(string)

Contains a thumbprint for an identity providerâs server certificate.
The identity providerâs server certificate thumbprint is the hex-encoded SHA-1 hash value of the self-signed X.509 certificate. This thumbprint is used by the domain where the OpenID Connect provider makes its keys available. The thumbprint is always a 40-character string.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iam", "create-open-id-connect-provider", "url", "thumbprint-list", add_option_dict)
