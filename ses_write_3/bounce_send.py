#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/send-bounce.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # original-message-id : The message ID of the message to be bounced.
    # bounce-sender : The address to use in the âFromâ header of the bounce message. This must be an identity that you have verified with Amazon SES.
    # bounced-recipient-info-list : A list of recipients of the bounced message, including the information required to create the Delivery Status Notifications (DSNs) for the recipients. You must specify at least one BouncedRecipientInfo in the list.
(structure)

Recipient-related information to include in the Delivery Status Notification (DSN) when an email that Amazon SES receives on your behalf bounces.
For information about receiving email through Amazon SES, see the Amazon SES Developer Guide .
Recipient -> (string)

The email address of the recipient of the bounced email.

RecipientArn -> (string)

This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to receive email for the recipient of the bounced email. For more information about sending authorization, see the Amazon SES Developer Guide .

BounceType -> (string)

The reason for the bounce. You must provide either this parameter or RecipientDsnFields .

RecipientDsnFields -> (structure)

Recipient-related DSN fields, most of which would normally be filled in automatically when provided with a BounceType . You must provide either this parameter or BounceType .
FinalRecipient -> (string)

The email address that the message was ultimately delivered to. This corresponds to the Final-Recipient in the DSN. If not specified, FinalRecipient will be set to the Recipient specified in the BouncedRecipientInfo structure. Either FinalRecipient or the recipient in BouncedRecipientInfo must be a recipient of the original bounced message.

Note
Do not prepend the FinalRecipient email address with rfc 822; , as described in RFC 3798 .


Action -> (string)

The action performed by the reporting mail transfer agent (MTA) as a result of its attempt to deliver the message to the recipient address. This is required by RFC 3464 .

RemoteMta -> (string)

The MTA to which the remote MTA attempted to deliver the message, formatted as specified in RFC 3464 (mta-name-type; mta-name ). This parameter typically applies only to propagating synchronous bounces.

Status -> (string)

The status code that indicates what went wrong. This is required by RFC 3464 .

DiagnosticCode -> (string)

An extended explanation of what went wrong; this is usually an SMTP response. See RFC 3463 for the correct formatting of this parameter.

LastAttemptDate -> (timestamp)

The time the final delivery attempt was made, in RFC 822 date-time format.

ExtensionFields -> (list)

Additional X-headers to include in the DSN.
(structure)

Additional X-headers to include in the Delivery Status Notification (DSN) when an email that Amazon SES receives on your behalf bounces.
For information about receiving email through Amazon SES, see the Amazon SES Developer Guide .
Name -> (string)

The name of the header to add. Must be between 1 and 50 characters, inclusive, and consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.

Value -> (string)

The value of the header to add. Must be less than 2048 characters, and must not contain newline characters (ârâ or ânâ).
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("ses", "send-bounce", "original-message-id", "bounce-sender", "bounced-recipient-info-list", add_option_dict)
