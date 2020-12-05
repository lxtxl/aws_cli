#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/remove-listener-certificates.html
if __name__ == '__main__':
    """
	add-listener-certificates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/add-listener-certificates.html
	describe-listener-certificates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-listener-certificates.html
    """

    parameter_display_string = """
    # listener-arn : The Amazon Resource Name (ARN) of the listener.
    # certificates : The certificate to remove. You can specify one certificate per call. Set CertificateArn to the certificate ARN but do not set IsDefault .
(structure)

Information about an SSL server certificate.
CertificateArn -> (string)

The Amazon Resource Name (ARN) of the certificate.

IsDefault -> (boolean)

Indicates whether the certificate is the default certificate. Do not set this value when specifying a certificate as an input. This value is not included in the output when describing a listener, but is included when describing listener certificates.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("elbv2", "remove-listener-certificates", "listener-arn", "certificates", add_option_dict)
