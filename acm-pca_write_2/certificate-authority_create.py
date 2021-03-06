#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/create-certificate-authority.html
if __name__ == '__main__':
    """
	delete-certificate-authority : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/delete-certificate-authority.html
	describe-certificate-authority : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/describe-certificate-authority.html
	list-certificate-authorities : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/list-certificate-authorities.html
	restore-certificate-authority : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/restore-certificate-authority.html
	tag-certificate-authority : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/tag-certificate-authority.html
	untag-certificate-authority : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/untag-certificate-authority.html
	update-certificate-authority : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/update-certificate-authority.html
    """

    parameter_display_string = """
    # certificate-authority-configuration : 
    # certificate-authority-type : The type of the certificate authority.
Possible values:

ROOT
SUBORDINATE
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("acm-pca", "create-certificate-authority", "certificate-authority-configuration", "certificate-authority-type", add_option_dict)
