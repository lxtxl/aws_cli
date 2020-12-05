#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/send-message-batch.html
if __name__ == '__main__':
    """
	delete-message-batch : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/delete-message-batch.html
    """

    parameter_display_string = """
    # queue-url : The URL of the Amazon SQS queue to which batched messages are sent.
Queue URLs and names are case-sensitive.
    # entries : A list of ``  SendMessageBatchRequestEntry `` items.
(structure)

Contains the details of a single Amazon SQS message along with an Id .
Id -> (string)

An identifier for a message in this batch used to communicate the result.

Note
The Id s of a batch request need to be unique within a request.
This identifier can have up to 80 characters. The following characters are accepted: alphanumeric characters, hyphens(-), and underscores (_).


MessageBody -> (string)

The body of the message.

DelaySeconds -> (integer)

The length of time, in seconds, for which a specific message is delayed. Valid values: 0 to 900. Maximum: 15 minutes. Messages with a positive DelaySeconds value become available for processing after the delay period is finished. If you donât specify a value, the default value for the queue is applied.

Note
When you set FifoQueue , you canât set DelaySeconds per message. You can set this parameter only on a queue level.


MessageAttributes -> (map)

Each message attribute consists of a Name , Type , and Value . For more information, see Amazon SQS Message Attributes in the Amazon Simple Queue Service Developer Guide .
Name -> (string)
Value -> (structure)

The user-specified message attribute value. For string data types, the Value attribute has the same restrictions on the content as the message body. For more information, see ``  SendMessage .``

Name , type , value and the message body must not be empty or null. All parts of the message attribute, including Name , Type , and Value , are part of the message size restriction (256 KB or 262,144 bytes).

StringValue -> (string)

Strings are Unicode with UTF-8 binary encoding. For a list of code values, see ASCII Printable Characters .

BinaryValue -> (blob)

Binary type attributes can store any binary data, such as compressed data, encrypted data, or images.

StringListValues -> (list)

Not implemented. Reserved for future use.
(string)

BinaryListValues -> (list)

Not implemented. Reserved for future use.
(blob)

DataType -> (string)

Amazon SQS supports the following logical data types: String , Number , and Binary . For the Number data type, you must use StringValue .
You can also append custom labels. For more information, see Amazon SQS Message Attributes in the Amazon Simple Queue Service Developer Guide .



MessageSystemAttributes -> (map)

The message system attribute to send Each message system attribute consists of a Name , Type , and Value .

Warning

Currently, the only supported message system attribute is AWSTraceHeader . Its type must be String and its value must be a correctly formatted AWS X-Ray trace header string.
The size of a message system attribute doesnât count towards the total size of a message.


Name -> (string)
Value -> (structure)

The user-specified message system attribute value. For string data types, the Value attribute has the same restrictions on the content as the message body. For more information, see ``  SendMessage .``

Name , type , value and the message body must not be empty or null.

StringValue -> (string)

Strings are Unicode with UTF-8 binary encoding. For a list of code values, see ASCII Printable Characters .

BinaryValue -> (blob)

Binary type attributes can store any binary data, such as compressed data, encrypted data, or images.

StringListValues -> (list)

Not implemented. Reserved for future use.
(string)

BinaryListValues -> (list)

Not implemented. Reserved for future use.
(blob)

DataType -> (string)

Amazon SQS supports the following logical data types: String , Number , and Binary . For the Number data type, you must use StringValue .
You can also append custom labels. For more information, see Amazon SQS Message Attributes in the Amazon Simple Queue Service Developer Guide .



MessageDeduplicationId -> (string)

This parameter applies only to FIFO (first-in-first-out) queues.
The token used for deduplication of messages within a 5-minute minimum deduplication interval. If a message with a particular MessageDeduplicationId is sent successfully, subsequent messages with the same MessageDeduplicationId are accepted successfully but arenât delivered. For more information, see Exactly-Once Processing in the Amazon Simple Queue Service Developer Guide .

Every message must have a unique MessageDeduplicationId ,

You may provide a MessageDeduplicationId explicitly.
If you arenât able to provide a MessageDeduplicationId and you enable ContentBasedDeduplication for your queue, Amazon SQS uses a SHA-256 hash to generate the MessageDeduplicationId using the body of the message (but not the attributes of the message).
If you donât provide a MessageDeduplicationId and the queue doesnât have ContentBasedDeduplication set, the action fails with an error.
If the queue has ContentBasedDeduplication set, your MessageDeduplicationId overrides the generated one.


When ContentBasedDeduplication is in effect, messages with identical content sent within the deduplication interval are treated as duplicates and only one copy of the message is delivered.
If you send one message with ContentBasedDeduplication enabled and then another message with a MessageDeduplicationId that is the same as the one generated for the first MessageDeduplicationId , the two messages are treated as duplicates and only one copy of the message is delivered.


Note
The MessageDeduplicationId is available to the consumer of the message (this can be useful for troubleshooting delivery issues).
If a message is sent successfully but the acknowledgement is lost and the message is resent with the same MessageDeduplicationId after the deduplication interval, Amazon SQS canât detect duplicate messages.
Amazon SQS continues to keep track of the message deduplication ID even after the message is received and deleted.

The length of MessageDeduplicationId is 128 characters. MessageDeduplicationId can contain alphanumeric characters (a-z , A-Z , 0-9 ) and punctuation (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ ).
For best practices of using MessageDeduplicationId , see Using the MessageDeduplicationId Property in the Amazon Simple Queue Service Developer Guide .

MessageGroupId -> (string)

This parameter applies only to FIFO (first-in-first-out) queues.
The tag that specifies that a message belongs to a specific message group. Messages that belong to the same message group are processed in a FIFO manner (however, messages in different message groups might be processed out of order). To interleave multiple ordered streams within a single queue, use MessageGroupId values (for example, session data for multiple users). In this scenario, multiple consumers can process the queue, but the session data of each user is processed in a FIFO fashion.

You must associate a non-empty MessageGroupId with a message. If you donât provide a MessageGroupId , the action fails.
ReceiveMessage might return messages with multiple MessageGroupId values. For each MessageGroupId , the messages are sorted by time sent. The caller canât specify a MessageGroupId .

The length of MessageGroupId is 128 characters. Valid values: alphanumeric characters and punctuation (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~) .
For best practices of using MessageGroupId , see Using the MessageGroupId Property in the Amazon Simple Queue Service Developer Guide .

Warning
MessageGroupId is required for FIFO queues. You canât use it for Standard queues.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sqs", "send-message-batch", "queue-url", "entries", add_option_dict)
