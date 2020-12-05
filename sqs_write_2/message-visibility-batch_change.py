#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/change-message-visibility-batch.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # queue-url : The URL of the Amazon SQS queue whose messagesâ visibility is changed.
Queue URLs and names are case-sensitive.
    # entries : A list of receipt handles of the messages for which the visibility timeout must be changed.
(structure)

Encloses a receipt handle and an entry id for each message in ``  ChangeMessageVisibilityBatch .``

Warning

All of the following list parameters must be prefixed with ChangeMessageVisibilityBatchRequestEntry.n , where n is an integer value starting with 1 . For example, a parameter list for this action might look like this:

&ChangeMessageVisibilityBatchRequestEntry.1.Id=change_visibility_msg_2
&ChangeMessageVisibilityBatchRequestEntry.1.ReceiptHandle=your_receipt_handle
&ChangeMessageVisibilityBatchRequestEntry.1.VisibilityTimeout=45

Id -> (string)

An identifier for this particular receipt handle used to communicate the result.

Note
The Id s of a batch request need to be unique within a request.
This identifier can have up to 80 characters. The following characters are accepted: alphanumeric characters, hyphens(-), and underscores (_).


ReceiptHandle -> (string)

A receipt handle.

VisibilityTimeout -> (integer)

The new value (in seconds) for the messageâs visibility timeout.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sqs", "change-message-visibility-batch", "queue-url", "entries", add_option_dict)
