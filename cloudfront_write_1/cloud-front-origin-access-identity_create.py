#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-cloud-front-origin-access-identity.html
if __name__ == '__main__':
    """
	delete-cloud-front-origin-access-identity : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/delete-cloud-front-origin-access-identity.html
	get-cloud-front-origin-access-identity : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-cloud-front-origin-access-identity.html
	list-cloud-front-origin-access-identities : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-cloud-front-origin-access-identities.html
	update-cloud-front-origin-access-identity : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-cloud-front-origin-access-identity.html
    """

    parameter_display_string = """
    # cloud-front-origin-access-identity-config : 
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("cloudfront", "create-cloud-front-origin-access-identity", "cloud-front-origin-access-identity-config", add_option_dict)





