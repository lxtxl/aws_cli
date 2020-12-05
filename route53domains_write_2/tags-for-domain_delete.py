#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/delete-tags-for-domain.html
if __name__ == '__main__':
    """
	list-tags-for-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/list-tags-for-domain.html
	update-tags-for-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/update-tags-for-domain.html
    """

    parameter_display_string = """
    # domain-name : The domain for which you want to delete one or more tags.
    # tags-to-delete : A list of tag keys to delete.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("route53domains", "delete-tags-for-domain", "domain-name", "tags-to-delete", add_option_dict)
