#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-schema.html
if __name__ == '__main__':
    """
	delete-schema : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-schema.html
	get-schema : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-schema.html
	list-schemas : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/list-schemas.html
	update-schema : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-schema.html
    """

    parameter_display_string = """
    # schema-name : Name of the schema to be created of max length of 255, and may only contain letters, numbers, hyphen, underscore, dollar sign, or hash mark. No whitespace.
    # data-format : The data format of the schema definition. Currently only AVRO is supported.
Possible values:

AVRO
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("glue", "create-schema", "schema-name", "data-format", add_option_dict)
