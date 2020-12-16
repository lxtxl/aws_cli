#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-featurestore-runtime/put-record.html
if __name__ == '__main__':
    """
	delete-record : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-featurestore-runtime/delete-record.html
	get-record : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-featurestore-runtime/get-record.html
    """

    parameter_display_string = """
    # feature-group-name : The name of the feature group that you want to insert the record into.
    # record : List of FeatureValues to be inserted. This will be a full over-write. If you only want to update few of the feature values, do the following:

Use GetRecord to retrieve the latest record.
Update the record returned from GetRecord .
Use PutRecord to update feature values.

(structure)

The value associated with a feature.
FeatureName -> (string)

The name of a feature that a feature value corresponds to.

ValueAsString -> (string)

The value associated with a feature, in string format. Note that features types can be String, Integral, or Fractional. This value represents all three types as a string.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sagemaker-featurestore-runtime", "put-record", "feature-group-name", "record", add_option_dict)
