#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/untag-resource.html
if __name__ == '__main__':
    """
	tag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/tag-resource.html
    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Name (ARN) of the ` RepositoryAssociation https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html`__ object. You can retrieve this ARN by calling ` ListRepositoryAssociations https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html`__ .
    # tag-keys : A list of the keys for each tag you want to remove from an associated repository.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("codeguru-reviewer", "untag-resource", "resource-arn", "tag-keys", add_option_dict)
