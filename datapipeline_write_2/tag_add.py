#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/add-tags.html
if __name__ == '__main__':
    """
	remove-tags : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/remove-tags.html
    """

    parameter_display_string = """
    # pipeline-id : The ID of the pipeline.
    # tags : The tags to add, as key/value pairs.
(structure)

Tags are key/value pairs defined by a user and associated with a pipeline to control access. AWS Data Pipeline allows you to associate ten tags per pipeline. For more information, see Controlling User Access to Pipelines in the AWS Data Pipeline Developer Guide .
key -> (string)

The key name of a tag defined by a user. For more information, see Controlling User Access to Pipelines in the AWS Data Pipeline Developer Guide .

value -> (string)

The optional value portion of a tag defined by a user. For more information, see Controlling User Access to Pipelines in the AWS Data Pipeline Developer Guide .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("datapipeline", "add-tags", "pipeline-id", "tags", add_option_dict)
