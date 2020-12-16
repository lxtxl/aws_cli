#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-stream.html
if __name__ == '__main__':
    """
	delete-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-stream.html
	describe-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-stream.html
	list-streams : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-streams.html
	update-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-stream.html
    """

    parameter_display_string = """
    # stream-id : The stream ID.
    # files : The files to stream.
(structure)

Represents a file to stream.
fileId -> (integer)

The file ID.

s3Location -> (structure)

The location of the file in S3.
bucket -> (string)

The S3 bucket.

key -> (string)

The S3 key.

version -> (string)

The S3 bucket version.
    # role-arn : An IAM role that allows the IoT service principal assumes to access your S3 files.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("iot", "create-stream", "stream-id", "files", "role-arn", add_option_dict)
