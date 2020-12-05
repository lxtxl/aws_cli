#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/get-finding-statistics.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # group-by : The finding property to use to group the query results. Valid values are:

classificationDetails.jobId - The unique identifier for the classification job that produced the finding.
resourcesAffected.s3Bucket.name - The name of the S3 bucket that the finding applies to.
severity.description - The severity level of the finding, such as High or Medium.
type - The type of finding, such as Policy:IAMUser/S3BucketPublic and SensitiveData:S3Object/Personal.

Possible values:

resourcesAffected.s3Bucket.name
type
classificationDetails.jobId
severity.description
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("macie2", "get-finding-statistics", "group-by", add_option_dict)