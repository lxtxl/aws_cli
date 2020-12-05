#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie/disassociate-s3-resources.html
if __name__ == '__main__':
    """
	associate-s3-resources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie/associate-s3-resources.html
	list-s3-resources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie/list-s3-resources.html
	update-s3-resources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie/update-s3-resources.html
    """

    parameter_display_string = """
    # associated-s3-resources : The S3 resources (buckets or prefixes) that you want to remove from being monitored and classified by Amazon Macie Classic.
(structure)

Contains information about the S3 resource. This data type is used as a request parameter in the DisassociateS3Resources action and can be used as a response parameter in the AssociateS3Resources and UpdateS3Resources actions.
bucketName -> (string)

The name of the S3 bucket.

prefix -> (string)

The prefix of the S3 bucket.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("macie", "disassociate-s3-resources", "associated-s3-resources", add_option_dict)





