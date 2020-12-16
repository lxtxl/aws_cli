#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/update-recipe-job.html
if __name__ == '__main__':
    """
	create-recipe-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/create-recipe-job.html
    """

    parameter_display_string = """
    # name : The name of the job to update.
    # outputs : One or more artifacts that represent the output from running the job.
(structure)

Represents individual output from a particular job run.
CompressionFormat -> (string)

The compression algorithm used to compress the output text of the job.

Format -> (string)

The data format of the output of the job.

PartitionColumns -> (list)

The names of one or more partition columns for the output of the job.
(string)

Location -> (structure)

The location in Amazon S3 where the job writes its output.
Bucket -> (string)

The S3 bucket name.

Key -> (string)

The unique name of the object in the bucket.


Overwrite -> (boolean)

A value that, if true, means that any data in the location specified for output is overwritten with new output.
    # role-arn : The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role to be assumed for this request.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("databrew", "update-recipe-job", "name", "outputs", "role-arn", add_option_dict)
