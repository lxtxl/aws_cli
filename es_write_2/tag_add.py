#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/add-tags.html
if __name__ == '__main__':
    """
	list-tags : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/list-tags.html
	remove-tags : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/remove-tags.html
    """

    parameter_display_string = """
    # arn : Specify the ARN for which you want to add the tags.
    # tag-list : List of Tag that need to be added for the Elasticsearch domain.
(structure)

Specifies a key value pair for a resource tag.
Key -> (string)

Specifies the TagKey , the name of the tag. Tag keys must be unique for the Elasticsearch domain to which they are attached.

Value -> (string)

Specifies the TagValue , the value assigned to the corresponding tag key. Tag values can be null and do not have to be unique in a tag set. For example, you can have a key value pair in a tag set of project : Trinity and cost-center : Trinity
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("es", "add-tags", "arn", "tag-list", add_option_dict)
