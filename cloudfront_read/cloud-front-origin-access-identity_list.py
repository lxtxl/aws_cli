#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-cloud-front-origin-access-identities.html
if __name__ == '__main__':
    """
	create-cloud-front-origin-access-identity : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-cloud-front-origin-access-identity.html
	delete-cloud-front-origin-access-identity : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/delete-cloud-front-origin-access-identity.html
	get-cloud-front-origin-access-identity : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-cloud-front-origin-access-identity.html
	update-cloud-front-origin-access-identity : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-cloud-front-origin-access-identity.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("cloudfront", "list-cloud-front-origin-access-identities", add_option_dict)