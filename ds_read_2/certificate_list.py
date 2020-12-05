#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/describe-certificate.html
if __name__ == '__main__':
    """
	deregister-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/deregister-certificate.html
	list-certificates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/list-certificates.html
	register-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/register-certificate.html
    """

    parameter_display_string = """
    # directory-id : The identifier of the directory.
    # certificate-id : The identifier of the certificate.
    """

    execute_two_parameter("ds", "describe-certificate", "directory-id", "certificate-id", parameter_display_string)