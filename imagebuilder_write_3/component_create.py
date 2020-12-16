#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-component.html
if __name__ == '__main__':
    """
	delete-component : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/delete-component.html
	get-component : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-component.html
	import-component : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/import-component.html
	list-components : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-components.html
    """

    parameter_display_string = """
    # name : The name of the component.
    # semantic-version : The semantic version of the component. This version follows the semantic version syntax. For example, major.minor.patch. This could be versioned like software (2.0.1) or like a date (2019.12.01).
    # platform : The platform of the component.
Possible values:

Windows
Linux
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("imagebuilder", "create-component", "name", "semantic-version", "platform", add_option_dict)
