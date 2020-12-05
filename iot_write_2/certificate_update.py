#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-certificate.html
if __name__ == '__main__':
    """
	delete-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-certificate.html
	describe-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-certificate.html
	list-certificates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-certificates.html
	register-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/register-certificate.html
	transfer-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/transfer-certificate.html
    """

    parameter_display_string = """
    # certificate-id : The ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)
    # new-status : The new status.

Note: Setting the status to PENDING_TRANSFER or PENDING_ACTIVATION will result in an exception being thrown. PENDING_TRANSFER and PENDING_ACTIVATION are statuses used internally by AWS IoT. They are not intended for developer use.
Note: The status value REGISTER_INACTIVE is deprecated and should not be used.

Possible values:

ACTIVE
INACTIVE
REVOKED
PENDING_TRANSFER
REGISTER_INACTIVE
PENDING_ACTIVATION
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iot", "update-certificate", "certificate-id", "new-status", add_option_dict)
