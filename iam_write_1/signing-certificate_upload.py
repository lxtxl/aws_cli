#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/upload-signing-certificate.html
if __name__ == '__main__':
    """
	delete-signing-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-signing-certificate.html
	list-signing-certificates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-signing-certificates.html
	update-signing-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-signing-certificate.html
    """

    parameter_display_string = """
    # certificate-body : The contents of the signing certificate.
The regex pattern used to validate this parameter is a string of characters consisting of the following:

Any printable ASCII character ranging from the space character (\u0020 ) through the end of the ASCII character range
The printable characters in the Basic Latin and Latin-1 Supplement character set (through \u00FF )
The special characters tab (\u0009 ), line feed (\u000A ), and carriage return (\u000D )
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iam", "upload-signing-certificate", "certificate-body", add_option_dict)





