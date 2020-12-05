#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie/update-s3-resources.html
if __name__ == '__main__':
    """
	associate-s3-resources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie/associate-s3-resources.html
	disassociate-s3-resources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie/disassociate-s3-resources.html
	list-s3-resources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie/list-s3-resources.html
    """

    parameter_display_string = """
    # s3-resources-update : The S3 resources whose classification types you want to update.
(structure)

The S3 resources whose classification types you want to update. This data type is used as a request parameter in the UpdateS3Resources action.
bucketName -> (string)

The name of the S3 bucket whose classification types you want to update.

prefix -> (string)

The prefix of the S3 bucket whose classification types you want to update.

classificationTypeUpdate -> (structure)

The classification type that you want to update for the resource associated with Amazon Macie Classic.
oneTime -> (string)

A one-time classification of all of the existing objects in a specified S3 bucket.

continuous -> (string)

A continuous classification of the objects that are added to a specified S3 bucket. Amazon Macie Classic begins performing continuous classification after a bucket is successfully associated with Amazon Macie Classic.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("macie", "update-s3-resources", "s3-resources-update", add_option_dict)





