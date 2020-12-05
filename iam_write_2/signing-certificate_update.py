#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-signing-certificate.html
if __name__ == '__main__':
    """
	delete-signing-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-signing-certificate.html
	list-signing-certificates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-signing-certificates.html
	upload-signing-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/upload-signing-certificate.html
    """

    parameter_display_string = """
    # certificate-id : The ID of the signing certificate you want to update.
This parameter allows (through its regex pattern ) a string of characters that can consist of any upper or lowercased letter or digit.
    # status : The status you want to assign to the certificate. Active means that the certificate can be used for API calls to AWS Inactive means that the certificate cannot be used.
Possible values:

Active
Inactive
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iam", "update-signing-certificate", "certificate-id", "status", add_option_dict)
