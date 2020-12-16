#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/upload-server-certificate.html
if __name__ == '__main__':
    """
	delete-server-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-server-certificate.html
	get-server-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-server-certificate.html
	list-server-certificates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-server-certificates.html
	update-server-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-server-certificate.html
    """

    parameter_display_string = """
    # server-certificate-name : The name for the server certificate. Do not include the path in this value. The name of the certificate cannot contain any spaces.
This parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
    # certificate-body : The contents of the public key certificate in PEM-encoded format.
The regex pattern used to validate this parameter is a string of characters consisting of the following:

Any printable ASCII character ranging from the space character (\u0020 ) through the end of the ASCII character range
The printable characters in the Basic Latin and Latin-1 Supplement character set (through \u00FF )
The special characters tab (\u0009 ), line feed (\u000A ), and carriage return (\u000D )
    # private-key : The contents of the private key in PEM-encoded format.
The regex pattern used to validate this parameter is a string of characters consisting of the following:

Any printable ASCII character ranging from the space character (\u0020 ) through the end of the ASCII character range
The printable characters in the Basic Latin and Latin-1 Supplement character set (through \u00FF )
The special characters tab (\u0009 ), line feed (\u000A ), and carriage return (\u000D )
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("iam", "upload-server-certificate", "server-certificate-name", "certificate-body", "private-key", add_option_dict)
