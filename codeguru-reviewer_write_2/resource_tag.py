#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/tag-resource.html
if __name__ == '__main__':
    """
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/untag-resource.html
    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Name (ARN) of the ` RepositoryAssociation https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html`__ object. You can retrieve this ARN by calling ` ListRepositoryAssociations https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html`__ .
    # tags : An array of key-value pairs used to tag an associated repository. A tag is a custom attribute label with two parts:

A tag key (for example, CostCenter , Environment , Project , or Secret ). Tag keys are case sensitive.
An optional field known as a tag value (for example, 111122223333 , Production , or a team name). Omitting the tag value is the same as using an empty string. Like tag keys, tag values are case sensitive.

key -> (string)
value -> (string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("codeguru-reviewer", "tag-resource", "resource-arn", "tags", add_option_dict)
