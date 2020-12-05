#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/set-topic-attributes.html
if __name__ == '__main__':
    """
	get-topic-attributes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/get-topic-attributes.html
    """

    parameter_display_string = """
    # topic-arn : The ARN of the topic to modify.
    # attribute-name : A map of attributes with their corresponding values.
The following lists the names, descriptions, and values of the special request parameters that the SetTopicAttributes action uses:

DeliveryPolicy â The policy that defines how Amazon SNS retries failed deliveries to HTTP/S endpoints.
DisplayName â The display name to use for a topic with SMS subscriptions.
Policy â The policy that defines who can access your topic. By default, only the topic owner can publish or subscribe to the topic.

The following attribute applies only to server-side-encryption :

KmsMasterKeyId â The ID of an AWS-managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see Key Terms . For more examples, see KeyId in the AWS Key Management Service API Reference .

The following attribute applies only to FIFO topics :

ContentBasedDeduplication â Enables content-based deduplication for FIFO topics.

By default, ContentBasedDeduplication is set to false . If you create a FIFO topic and this attribute is false , you must specify a value for the MessageDeduplicationId parameter for the Publish action.
When you set ContentBasedDeduplication to true , Amazon SNS uses a SHA-256 hash to generate the MessageDeduplicationId using the body of the message (but not the attributes of the message). (Optional) To override the generated value, you can specify a value for the the MessageDeduplicationId parameter for the Publish action.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sns", "set-topic-attributes", "topic-arn", "attribute-name", add_option_dict)
