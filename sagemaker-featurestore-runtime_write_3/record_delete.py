#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-featurestore-runtime/delete-record.html
if __name__ == '__main__':
    """
	get-record : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-featurestore-runtime/get-record.html
	put-record : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-featurestore-runtime/put-record.html
    """

    parameter_display_string = """
    # feature-group-name : The name of the feature group to delete the record from.
    # record-identifier-value-as-string : The value for the RecordIdentifier that uniquely identifies the record, in string format.
    # event-time : Timestamp indicating when the deletion event occurred. EventTime can be used to query data at a certain point in time.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("sagemaker-featurestore-runtime", "delete-record", "feature-group-name", "record-identifier-value-as-string", "event-time", add_option_dict)
