#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/list-facet-attributes.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # schema-arn : The ARN of the schema where the facet resides.
    # name : The name of the facet whose attributes will be retrieved.
    """

    execute_two_parameter("clouddirectory", "list-facet-attributes", "schema-arn", "name", parameter_display_string)