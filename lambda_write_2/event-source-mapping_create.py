#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-event-source-mapping.html
if __name__ == '__main__':
    """
	delete-event-source-mapping : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-event-source-mapping.html
	get-event-source-mapping : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-event-source-mapping.html
	list-event-source-mappings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-event-source-mappings.html
	update-event-source-mapping : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-event-source-mapping.html
    """

    parameter_display_string = """
    # event-source-arn : The Amazon Resource Name (ARN) of the event source.

Amazon Kinesis - The ARN of the data stream or a stream consumer.
Amazon DynamoDB Streams - The ARN of the stream.
Amazon Simple Queue Service - The ARN of the queue.
Amazon Managed Streaming for Apache Kafka - The ARN of the cluster.
    # function-name : The name of the Lambda function.

Name formats


Function name - MyFunction .
Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction .
Version or Alias ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction:PROD .
Partial ARN - 123456789012:function:MyFunction .

The length constraint applies only to the full ARN. If you specify only the function name, itâs limited to 64 characters in length.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("lambda", "create-event-source-mapping", "event-source-arn", "function-name", add_option_dict)
