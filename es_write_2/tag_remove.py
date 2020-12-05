#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/remove-tags.html
if __name__ == '__main__':
    """
	add-tags : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/add-tags.html
	list-tags : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/list-tags.html
    """

    parameter_display_string = """
    # arn : Specifies the ARN for the Elasticsearch domain from which you want to delete the specified tags.
    # tag-keys : Specifies the TagKey list which you want to remove from the Elasticsearch domain.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("es", "remove-tags", "arn", "tag-keys", add_option_dict)
