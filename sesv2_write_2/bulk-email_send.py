#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/send-bulk-email.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # default-content : 
    # bulk-email-entries : The list of bulk email entry objects.
(structure)

Destination -> (structure)

Represents the destination of the message, consisting of To:, CC:, and BCC: fields.

Note
Amazon SES does not support the SMTPUTF8 extension, as described in RFC6531 . For this reason, the local part of a destination email address (the part of the email address that precedes the @ sign) may only contain 7-bit ASCII characters . If the domain part of an address (the part after the @ sign) contains non-ASCII characters, they must be encoded using Punycode, as described in RFC3492 .

ToAddresses -> (list)

An array that contains the email addresses of the âToâ recipients for the email.
(string)

CcAddresses -> (list)

An array that contains the email addresses of the âCCâ (carbon copy) recipients for the email.
(string)

BccAddresses -> (list)

An array that contains the email addresses of the âBCCâ (blind carbon copy) recipients for the email.
(string)


ReplacementTags -> (list)

A list of tags, in the form of name/value pairs, to apply to an email that you send using the SendBulkTemplatedEmail operation. Tags correspond to characteristics of the email that you define, so that you can publish email sending events.
(structure)

Contains the name and value of a tag that you apply to an email. You can use message tags when you publish email sending events.
Name -> (string)

The name of the message tag. The message tag name has to meet the following criteria:

It can only contain ASCII letters (aâz, AâZ), numbers (0â9), underscores (_), or dashes (-).
It can contain no more than 256 characters.


Value -> (string)

The value of the message tag. The message tag value has to meet the following criteria:

It can only contain ASCII letters (aâz, AâZ), numbers (0â9), underscores (_), or dashes (-).
It can contain no more than 256 characters.




ReplacementEmailContent -> (structure)

The ReplacementEmailContent associated with a BulkEmailEntry .
ReplacementTemplate -> (structure)

The ReplacementTemplate associated with ReplacementEmailContent .
ReplacementTemplateData -> (string)

A list of replacement values to apply to the template. This parameter is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sesv2", "send-bulk-email", "default-content", "bulk-email-entries", add_option_dict)
