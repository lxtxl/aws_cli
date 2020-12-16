#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/create-certificate-authority-audit-report.html
if __name__ == '__main__':
    """
	describe-certificate-authority-audit-report : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/describe-certificate-authority-audit-report.html
    """

    parameter_display_string = """
    # certificate-authority-arn : The Amazon Resource Name (ARN) of the CA to be audited. This is of the form:

``arn:aws:acm-pca:region :account :certificate-authority/12345678-1234-1234-1234-123456789012 `` .
    # s3-bucket-name : The name of the S3 bucket that will contain the audit report.
    # audit-report-response-format : The format in which to create the report. This can be either JSON or CSV .
Possible values:

JSON
CSV
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("acm-pca", "create-certificate-authority-audit-report", "certificate-authority-arn", "s3-bucket-name", "audit-report-response-format", add_option_dict)
