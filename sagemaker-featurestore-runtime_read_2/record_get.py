#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-featurestore-runtime/get-record.html
if __name__ == '__main__':
    """
	delete-record : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-featurestore-runtime/delete-record.html
	put-record : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-featurestore-runtime/put-record.html
    """

    parameter_display_string = """
    # feature-group-name : The name of the feature group in which you want to put the records.
    # record-identifier-value-as-string : The value that corresponds to RecordIdentifier type and uniquely identifies the record in the FeatureGroup .
    """

    execute_two_parameter("sagemaker-featurestore-runtime", "get-record", "feature-group-name", "record-identifier-value-as-string", parameter_display_string)