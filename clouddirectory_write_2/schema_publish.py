#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/publish-schema.html
if __name__ == '__main__':
    """
	apply-schema : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/apply-schema.html
	create-schema : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/create-schema.html
	delete-schema : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/delete-schema.html
	update-schema : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/update-schema.html
    """

    parameter_display_string = """
    # development-schema-arn : The Amazon Resource Name (ARN) that is associated with the development schema. For more information, see  arns .
    # schema-version : The major version under which the schema will be published. Schemas have both a major and minor version associated with them.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("clouddirectory", "publish-schema", "development-schema-arn", "schema-version", add_option_dict)
