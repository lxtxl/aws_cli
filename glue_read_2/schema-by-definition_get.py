#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-schema-by-definition.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # schema-id : 
    # schema-definition : The definition of the schema for which schema details are required.
    """

    execute_two_parameter("glue", "get-schema-by-definition", "schema-id", "schema-definition", parameter_display_string)