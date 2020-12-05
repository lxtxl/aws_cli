#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/import-certificate-authority-certificate.html
if __name__ == '__main__':
    """
	get-certificate-authority-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/get-certificate-authority-certificate.html
    """

    parameter_display_string = """
    # certificate-authority-arn : The Amazon Resource Name (ARN) that was returned when you called CreateCertificateAuthority . This must be of the form:

``arn:aws:acm-pca:region :account :certificate-authority/12345678-1234-1234-1234-123456789012 ``
    # certificate : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("acm-pca", "import-certificate-authority-certificate", "certificate-authority-arn", "certificate", add_option_dict)
