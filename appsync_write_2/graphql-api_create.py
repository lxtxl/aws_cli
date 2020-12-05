#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/create-graphql-api.html
if __name__ == '__main__':
    """
	delete-graphql-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/delete-graphql-api.html
	get-graphql-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/get-graphql-api.html
	list-graphql-apis : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/list-graphql-apis.html
	update-graphql-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/update-graphql-api.html
    """

    parameter_display_string = """
    # name : A user-supplied name for the GraphqlApi .
    # authentication-type : The authentication type: API key, AWS IAM, OIDC, or Amazon Cognito user pools.
Possible values:

API_KEY
AWS_IAM
AMAZON_COGNITO_USER_POOLS
OPENID_CONNECT
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("appsync", "create-graphql-api", "name", "authentication-type", add_option_dict)
