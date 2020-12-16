#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/revoke-certificate.html
if __name__ == '__main__':
    """
	get-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/get-certificate.html
	issue-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/issue-certificate.html
    """

    parameter_display_string = """
    # certificate-authority-arn : Amazon Resource Name (ARN) of the private CA that issued the certificate to be revoked. This must be of the form:

``arn:aws:acm-pca:region :account :certificate-authority/12345678-1234-1234-1234-123456789012 ``
    # certificate-serial : Serial number of the certificate to be revoked. This must be in hexadecimal format. You can retrieve the serial number by calling GetCertificate with the Amazon Resource Name (ARN) of the certificate you want and the ARN of your private CA. The GetCertificate action retrieves the certificate in the PEM format. You can use the following OpenSSL command to list the certificate in text format and copy the hexadecimal serial number.

openssl x509 -in *file_path* -text -noout

You can also copy the serial number from the console or use the DescribeCertificate action in the AWS Certificate Manager API Reference .
    # revocation-reason : Specifies why you revoked the certificate.
Possible values:

UNSPECIFIED
KEY_COMPROMISE
CERTIFICATE_AUTHORITY_COMPROMISE
AFFILIATION_CHANGED
SUPERSEDED
CESSATION_OF_OPERATION
PRIVILEGE_WITHDRAWN
A_A_COMPROMISE
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("acm-pca", "revoke-certificate", "certificate-authority-arn", "certificate-serial", "revocation-reason", add_option_dict)
