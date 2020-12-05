#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/get-certificate.html
if __name__ == '__main__':
    """
	issue-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/issue-certificate.html
	revoke-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/revoke-certificate.html
    """

    parameter_display_string = """
    # certificate-authority-arn : The Amazon Resource Name (ARN) that was returned when you called CreateCertificateAuthority . This must be of the form:

``arn:aws:acm-pca:region :account :certificate-authority/12345678-1234-1234-1234-123456789012 `` .
    # certificate-arn : The ARN of the issued certificate. The ARN contains the certificate serial number and must be in the following form:

``arn:aws:acm-pca:region :account :certificate-authority/12345678-1234-1234-1234-123456789012 /certificate/286535153982981100925020015808220737245 ``
    """

    execute_two_parameter("acm-pca", "get-certificate", "certificate-authority-arn", "certificate-arn", parameter_display_string)