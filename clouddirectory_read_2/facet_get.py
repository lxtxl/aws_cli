#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/get-facet.html
if __name__ == '__main__':
    """
	create-facet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/create-facet.html
	delete-facet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/delete-facet.html
	update-facet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/update-facet.html
    """

    parameter_display_string = """
    # schema-arn : The Amazon Resource Name (ARN) that is associated with the  Facet . For more information, see  arns .
    # name : The name of the facet to retrieve.
    """

    execute_two_parameter("clouddirectory", "get-facet", "schema-arn", "name", parameter_display_string)