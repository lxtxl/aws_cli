#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/delete-policy.html
if __name__ == '__main__':
    """
	get-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/get-policy.html
	put-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/put-policy.html
    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Number (ARN) of the private CA that will have its policy deleted. You can find the CAâs ARN by calling the ListCertificateAuthorities action. The ARN value must have the form arn:aws:acm-pca:region:account:certificate-authority/01234567-89ab-cdef-0123-0123456789ab .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("acm-pca", "delete-policy", "resource-arn", add_option_dict)





