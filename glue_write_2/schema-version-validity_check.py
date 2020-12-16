#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/check-schema-version-validity.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # data-format : The data format of the schema definition. Currently only AVRO is supported.
Possible values:

AVRO
    # schema-definition : The definition of the schema that has to be validated.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("glue", "check-schema-version-validity", "data-format", "schema-definition", add_option_dict)
