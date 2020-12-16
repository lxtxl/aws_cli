#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/send-bulk-templated-email.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # source : The email address that is sending the email. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. For information about verifying identities, see the Amazon SES Developer Guide .
If you are sending on behalf of another user and have been permitted to do so by a sending authorization policy, then you must also specify the SourceArn parameter. For more information about sending authorization, see the Amazon SES Developer Guide .

Note
Amazon SES does not support the SMTPUTF8 extension, as described in RFC6531 . For this reason, the local part of a source email address (the part of the email address that precedes the @ sign) may only contain 7-bit ASCII characters . If the domain part of an address (the part after the @ sign) contains non-ASCII characters, they must be encoded using Punycode, as described in RFC3492 . The sender name (also known as the friendly name ) may contain non-ASCII characters. These characters must be encoded using MIME encoded-word syntax, as described in RFC 2047 . MIME encoded-word syntax uses the following form: =?charset?encoding?encoded-text?= .
    # template : The template to use when sending this email.
    # destinations : One or more Destination objects. All of the recipients in a Destination will receive the same version of the email. You can specify up to 50 Destination objects within a Destinations array.
(structure)

An array that contains one or more Destinations, as well as the tags and replacement data associated with each of those Destinations.
Destination -> (structure)

Represents the destination of the message, consisting of To:, CC:, and BCC: fields.

Note
Amazon SES does not support the SMTPUTF8 extension, as described in RFC6531 . For this reason, the local part of a destination email address (the part of the email address that precedes the @ sign) may only contain 7-bit ASCII characters . If the domain part of an address (the part after the @ sign) contains non-ASCII characters, they must be encoded using Punycode, as described in RFC3492 .

ToAddresses -> (list)

The recipients to place on the To: line of the message.
(string)

CcAddresses -> (list)

The recipients to place on the CC: line of the message.
(string)

BccAddresses -> (list)

The recipients to place on the BCC: line of the message.
(string)


ReplacementTags -> (list)

A list of tags, in the form of name/value pairs, to apply to an email that you send using SendBulkTemplatedEmail . Tags correspond to characteristics of the email that you define, so that you can publish email sending events.
(structure)

Contains the name and value of a tag that you can provide to SendEmail or SendRawEmail to apply to an email.
Message tags, which you use with configuration sets, enable you to publish email sending events. For information about using configuration sets, see the Amazon SES Developer Guide .
Name -> (string)

The name of the tag. The name must:

This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
Contain less than 256 characters.


Value -> (string)

The value of the tag. The value must:

This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
Contain less than 256 characters.




ReplacementTemplateData -> (string)

A list of replacement values to apply to the template. This parameter is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("ses", "send-bulk-templated-email", "source", "template", "destinations", add_option_dict)
