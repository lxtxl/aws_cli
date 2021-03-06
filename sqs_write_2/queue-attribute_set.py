#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/set-queue-attributes.html
if __name__ == '__main__':
    """
	get-queue-attributes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/get-queue-attributes.html
    """

    parameter_display_string = """
    # queue-url : The URL of the Amazon SQS queue whose attributes are set.
Queue URLs and names are case-sensitive.
    # attributes : A map of attributes to set.
The following lists the names, descriptions, and values of the special request parameters that the SetQueueAttributes action uses:

DelaySeconds â The length of time, in seconds, for which the delivery of all messages in the queue is delayed. Valid values: An integer from 0 to 900 (15 minutes). Default: 0.
MaximumMessageSize â The limit of how many bytes a message can contain before Amazon SQS rejects it. Valid values: An integer from 1,024 bytes (1 KiB) up to 262,144 bytes (256 KiB). Default: 262,144 (256 KiB).
MessageRetentionPeriod â The length of time, in seconds, for which Amazon SQS retains a message. Valid values: An integer representing seconds, from 60 (1 minute) to 1,209,600 (14 days). Default: 345,600 (4 days).
Policy â The queueâs policy. A valid AWS policy. For more information about policy structure, see Overview of AWS IAM Policies in the Amazon IAM User Guide .
ReceiveMessageWaitTimeSeconds â The length of time, in seconds, for which a ``  ReceiveMessage `` action waits for a message to arrive. Valid values: An integer from 0 to 20 (seconds). Default: 0.
RedrivePolicy â The string that includes the parameters for the dead-letter queue functionality of the source queue as a JSON object. For more information about the redrive policy and dead-letter queues, see Using Amazon SQS Dead-Letter Queues in the Amazon Simple Queue Service Developer Guide .

deadLetterTargetArn â The Amazon Resource Name (ARN) of the dead-letter queue to which Amazon SQS moves messages after the value of maxReceiveCount is exceeded.
maxReceiveCount â The number of times a message is delivered to the source queue before being moved to the dead-letter queue. When the ReceiveCount for a message exceeds the maxReceiveCount for a queue, Amazon SQS moves the message to the dead-letter-queue.




Note
The dead-letter queue of a FIFO queue must also be a FIFO queue. Similarly, the dead-letter queue of a standard queue must also be a standard queue.


VisibilityTimeout â The visibility timeout for the queue, in seconds. Valid values: An integer from 0 to 43,200 (12 hours). Default: 30. For more information about the visibility timeout, see Visibility Timeout in the Amazon Simple Queue Service Developer Guide .

The following attributes apply only to server-side-encryption :

KmsMasterKeyId â The ID of an AWS-managed customer master key (CMK) for Amazon SQS or a custom CMK. For more information, see Key Terms . While the alias of the AWS-managed CMK for Amazon SQS is always alias/aws/sqs , the alias of a custom CMK can, for example, be ``alias/MyAlias `` . For more examples, see KeyId in the AWS Key Management Service API Reference .
KmsDataKeyReusePeriodSeconds â The length of time, in seconds, for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again. An integer representing seconds, between 60 seconds (1 minute) and 86,400 seconds (24 hours). Default: 300 (5 minutes). A shorter time period provides better security but results in more calls to KMS which might incur charges after Free Tier. For more information, see How Does the Data Key Reuse Period Work? .

The following attribute applies only to FIFO (first-in-first-out) queues :

ContentBasedDeduplication â Enables content-based deduplication. For more information, see Exactly-Once Processing in the Amazon Simple Queue Service Developer Guide .

Every message must have a unique MessageDeduplicationId ,

You may provide a MessageDeduplicationId explicitly.
If you arenât able to provide a MessageDeduplicationId and you enable ContentBasedDeduplication for your queue, Amazon SQS uses a SHA-256 hash to generate the MessageDeduplicationId using the body of the message (but not the attributes of the message).
If you donât provide a MessageDeduplicationId and the queue doesnât have ContentBasedDeduplication set, the action fails with an error.
If the queue has ContentBasedDeduplication set, your MessageDeduplicationId overrides the generated one.


When ContentBasedDeduplication is in effect, messages with identical content sent within the deduplication interval are treated as duplicates and only one copy of the message is delivered.
If you send one message with ContentBasedDeduplication enabled and then another message with a MessageDeduplicationId that is the same as the one generated for the first MessageDeduplicationId , the two messages are treated as duplicates and only one copy of the message is delivered.



Name -> (string)
Value -> (string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sqs", "set-queue-attributes", "queue-url", "attributes", add_option_dict)
