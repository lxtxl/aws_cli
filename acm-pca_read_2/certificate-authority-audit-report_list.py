#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/describe-certificate-authority-audit-report.html
if __name__ == '__main__':
    """
	create-certificate-authority-audit-report : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/create-certificate-authority-audit-report.html
    """

    parameter_display_string = """
    # certificate-authority-arn : The Amazon Resource Name (ARN) of the private CA. This must be of the form:

``arn:aws:acm-pca:region :account :certificate-authority/12345678-1234-1234-1234-123456789012 `` .
    # audit-report-id : The report ID returned by calling the CreateCertificateAuthorityAuditReport action.
    """

    execute_two_parameter("acm-pca", "describe-certificate-authority-audit-report", "certificate-authority-arn", "audit-report-id", parameter_display_string)