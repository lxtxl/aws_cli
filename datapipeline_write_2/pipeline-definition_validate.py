#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/validate-pipeline-definition.html
if __name__ == '__main__':
    """
	get-pipeline-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/get-pipeline-definition.html
	put-pipeline-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/put-pipeline-definition.html
    """

    parameter_display_string = """
    # pipeline-id : The ID of the pipeline.
    # pipeline-objects : The objects that define the pipeline changes to validate against the pipeline.
(structure)

Contains information about a pipeline object. This can be a logical, physical, or physical attempt pipeline object. The complete set of components of a pipeline defines the pipeline.
id -> (string)

The ID of the object.

name -> (string)

The name of the object.

fields -> (list)

Key-value pairs that define the properties of the object.
(structure)

A key-value pair that describes a property of a pipeline object. The value is specified as either a string value (StringValue ) or a reference to another object (RefValue ) but not as both.
key -> (string)

The field identifier.

stringValue -> (string)

The field value, expressed as a String.

refValue -> (string)

The field value, expressed as the identifier of another object.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("datapipeline", "validate-pipeline-definition", "pipeline-id", "pipeline-objects", add_option_dict)
