#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/list-certificate-authorities.html
if __name__ == '__main__':
    """
	create-certificate-authority : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/create-certificate-authority.html
	delete-certificate-authority : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/delete-certificate-authority.html
	describe-certificate-authority : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/describe-certificate-authority.html
	restore-certificate-authority : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/restore-certificate-authority.html
	tag-certificate-authority : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/tag-certificate-authority.html
	untag-certificate-authority : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/untag-certificate-authority.html
	update-certificate-authority : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/update-certificate-authority.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("acm-pca", "list-certificate-authorities", add_option_dict)