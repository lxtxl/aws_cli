#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-saml-providers.html
if __name__ == '__main__':
    """
	create-saml-provider : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-saml-provider.html
	delete-saml-provider : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-saml-provider.html
	get-saml-provider : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-saml-provider.html
	update-saml-provider : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-saml-provider.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("iam", "list-saml-providers", add_option_dict)