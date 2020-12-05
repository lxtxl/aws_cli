#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/get-typed-link-facet-information.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # schema-arn : The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .
    # name : The unique name of the typed link facet.
    """

    execute_two_parameter("clouddirectory", "get-typed-link-facet-information", "schema-arn", "name", parameter_display_string)