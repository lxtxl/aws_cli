#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/start-signing-job.html
if __name__ == '__main__':
    """
	describe-signing-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/describe-signing-job.html
	list-signing-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/list-signing-jobs.html
    """

    parameter_display_string = """
    # source : The email address that is sending the email. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. For information about verifying identities, see the Amazon SES Developer Guide .
If you are sending on behalf of another user and have been permitted to do so by a sending authorization policy, then you must also specify the SourceArn parameter. For more information about sending authorization, see the Amazon SES Developer Guide .

Note
Amazon SES does not support the SMTPUTF8 extension, as described in RFC6531 . For this reason, the local part of a source email address (the part of the email address that precedes the @ sign) may only contain 7-bit ASCII characters . If the domain part of an address (the part after the @ sign) contains non-ASCII characters, they must be encoded using Punycode, as described in RFC3492 . The sender name (also known as the friendly name ) may contain non-ASCII characters. These characters must be encoded using MIME encoded-word syntax, as described in`RFC 2047 <https://tools.ietf.org/html/rfc2047>`__ . MIME encoded-word syntax uses the following form: =?charset?encoding?encoded-text?= .
    # destination : 
    # profile-name : The name of the signing profile.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("signer", "start-signing-job", "source", "destination", "profile-name", add_option_dict)
