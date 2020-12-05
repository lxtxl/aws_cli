#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/get-open-id-token-for-developer-identity.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # identity-pool-id : An identity pool ID in the format REGION:GUID.
    # logins : A set of optional name-value pairs that map provider names to provider tokens. Each name-value pair represents a user from a public provider or developer provider. If the user is from a developer provider, the name-value pair will follow the syntax "developer_provider_name": "developer_user_identifier" . The developer provider is the âdomainâ by which Cognito will refer to your users; you provided this domain while creating/updating the identity pool. The developer user identifier is an identifier from your backend that uniquely identifies a user. When you create an identity pool, you can specify the supported logins.
key -> (string)
value -> (string)
    """

    execute_two_parameter("cognito-identity", "get-open-id-token-for-developer-identity", "identity-pool-id", "logins", parameter_display_string)