#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalytics/start-application.html
if __name__ == '__main__':
    """
	create-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalytics/create-application.html
	delete-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalytics/delete-application.html
	describe-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalytics/describe-application.html
	list-applications : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalytics/list-applications.html
	stop-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalytics/stop-application.html
	update-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalytics/update-application.html
    """

    parameter_display_string = """
    # application-name : Name of the application.
    # input-configurations : Identifies the specific input, by ID, that the application starts consuming. Amazon Kinesis Analytics starts reading the streaming source associated with the input. You can also specify where in the streaming source you want Amazon Kinesis Analytics to start reading.
(structure)

When you start your application, you provide this configuration, which identifies the input source and the point in the input source at which you want the application to start processing records.
Id -> (string)

Input source ID. You can get this ID by calling the DescribeApplication operation.

InputStartingPositionConfiguration -> (structure)

Point at which you want the application to start processing records from the streaming source.
InputStartingPosition -> (string)

The starting position on the stream.

NOW - Start reading just after the most recent record in the stream, start at the request time stamp that the customer issued.
TRIM_HORIZON - Start reading at the last untrimmed record in the stream, which is the oldest record available in the stream. This option is not available for an Amazon Kinesis Firehose delivery stream.
LAST_STOPPED_POINT - Resume reading from where the application last stopped reading.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("kinesisanalytics", "start-application", "application-name", "input-configurations", add_option_dict)
