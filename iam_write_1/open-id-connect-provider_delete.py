#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-open-id-connect-provider.html
if __name__ == '__main__':
    """
	create-open-id-connect-provider : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-open-id-connect-provider.html
	get-open-id-connect-provider : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-open-id-connect-provider.html
	list-open-id-connect-providers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-open-id-connect-providers.html
    """

    parameter_display_string = """
    # open-id-connect-provider-arn : The Amazon Resource Name (ARN) of the IAM OpenID Connect provider resource object to delete. You can get a list of OpenID Connect provider resource ARNs by using the  ListOpenIDConnectProviders operation.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iam", "delete-open-id-connect-provider", "open-id-connect-provider-arn", add_option_dict)





