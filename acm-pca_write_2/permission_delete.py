#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/delete-permission.html
if __name__ == '__main__':
    """
	create-permission : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/create-permission.html
	list-permissions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/list-permissions.html
    """

    parameter_display_string = """
    # certificate-authority-arn : The Amazon Resource Number (ARN) of the private CA that issued the permissions. You can find the CAâs ARN by calling the ListCertificateAuthorities action. This must have the following form:

``arn:aws:acm-pca:region :account :certificate-authority/12345678-1234-1234-1234-123456789012 `` .
    # principal : The AWS service or identity that will have its CA permissions revoked. At this time, the only valid service principal is acm.amazonaws.com
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("acm-pca", "delete-permission", "certificate-authority-arn", "principal", add_option_dict)
