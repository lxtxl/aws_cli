#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/update-contact-attributes.html
if __name__ == '__main__':
    """
	get-contact-attributes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/get-contact-attributes.html
    """

    parameter_display_string = """
    # initial-contact-id : The identifier of the contact. This is the identifier of the contact associated with the first interaction with the contact center.
    # instance-id : The identifier of the Amazon Connect instance.
    # attributes : The Amazon Connect attributes. These attributes can be accessed in contact flows just like any other contact attributes.
You can have up to 32,768 UTF-8 bytes across all attributes for a contact. Attribute keys can include only alphanumeric, dash, and underscore characters.
key -> (string)
value -> (string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("connect", "update-contact-attributes", "initial-contact-id", "instance-id", "attributes", add_option_dict)
