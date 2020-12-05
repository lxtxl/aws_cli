#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/update-pipeline.html
if __name__ == '__main__':
    """
	create-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/create-pipeline.html
	delete-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/delete-pipeline.html
	describe-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/describe-pipeline.html
	list-pipelines : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/list-pipelines.html
    """

    parameter_display_string = """
    # pipeline-name : The name of the pipeline to update.
    # pipeline-activities : A list of PipelineActivity objects. Activities perform transformations on your messages, such as removing, renaming or adding message attributes; filtering messages based on attribute values; invoking your Lambda functions on messages for advanced processing; or performing mathematical transformations to normalize device data.
The list can be 2-25 PipelineActivity objects and must contain both a channel and a datastore activity. Each entry in the list must contain only one activity. For example:

pipelineActivities = [ { "channel": { ... } }, { "lambda": { ... } }, ... ]

(structure)

An activity that performs a transformation on a message.
channel -> (structure)

Determines the source of the messages to be processed.
name -> (string)

The name of the channel activity.

channelName -> (string)

The name of the channel from which the messages are processed.

next -> (string)

The next activity in the pipeline.


lambda -> (structure)

Runs a Lambda function to modify the message.
name -> (string)

The name of the lambda activity.

lambdaName -> (string)

The name of the Lambda function that is run on the message.

batchSize -> (integer)

The number of messages passed to the Lambda function for processing.
The Lambda function must be able to process all of these messages within five minutes, which is the maximum timeout duration for Lambda functions.

next -> (string)

The next activity in the pipeline.


datastore -> (structure)

Specifies where to store the processed message data.
name -> (string)

The name of the datastore activity.

datastoreName -> (string)

The name of the data store where processed messages are stored.


addAttributes -> (structure)

Adds other attributes based on existing attributes in the message.
name -> (string)

The name of the addAttributes activity.

attributes -> (map)

A list of 1-50 AttributeNameMapping objects that map an existing attribute to a new attribute.

Note
The existing attributes remain in the message, so if you want to remove the originals, use RemoveAttributeActivity .

key -> (string)
value -> (string)

next -> (string)

The next activity in the pipeline.


removeAttributes -> (structure)

Removes attributes from a message.
name -> (string)

The name of the removeAttributes activity.

attributes -> (list)

A list of 1-50 attributes to remove from the message.
(string)

next -> (string)

The next activity in the pipeline.


selectAttributes -> (structure)

Creates a new message using only the specified attributes from the original message.
name -> (string)

The name of the selectAttributes activity.

attributes -> (list)

A list of the attributes to select from the message.
(string)

next -> (string)

The next activity in the pipeline.


filter -> (structure)

Filters a message based on its attributes.
name -> (string)

The name of the filter activity.

filter -> (string)

An expression that looks like a SQL WHERE clause that must return a Boolean value. Messages that satisfy the condition are passed to the next activity.

next -> (string)

The next activity in the pipeline.


math -> (structure)

Computes an arithmetic expression using the messageâs attributes and adds it to the message.
name -> (string)

The name of the math activity.

attribute -> (string)

The name of the attribute that contains the result of the math operation.

math -> (string)

An expression that uses one or more existing attributes and must return an integer value.

next -> (string)

The next activity in the pipeline.


deviceRegistryEnrich -> (structure)

Adds data from the AWS IoT device registry to your message.
name -> (string)

The name of the deviceRegistryEnrich activity.

attribute -> (string)

The name of the attribute that is added to the message.

thingName -> (string)

The name of the IoT device whose registry information is added to the message.

roleArn -> (string)

The ARN of the role that allows access to the deviceâs registry information.

next -> (string)

The next activity in the pipeline.


deviceShadowEnrich -> (structure)

Adds information from the AWS IoT Device Shadow service to a message.
name -> (string)

The name of the deviceShadowEnrich activity.

attribute -> (string)

The name of the attribute that is added to the message.

thingName -> (string)

The name of the IoT device whose shadow information is added to the message.

roleArn -> (string)

The ARN of the role that allows access to the deviceâs shadow.

next -> (string)

The next activity in the pipeline.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iotanalytics", "update-pipeline", "pipeline-name", "pipeline-activities", add_option_dict)
