#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/import-terminology.html
if __name__ == '__main__':
    """
	delete-terminology : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/delete-terminology.html
	get-terminology : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/get-terminology.html
	list-terminologies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/list-terminologies.html
    """

    parameter_display_string = """
    # name : The name of the custom terminology being imported.
    # merge-strategy : The merge strategy of the custom terminology being imported. Currently, only the OVERWRITE merge strategy is supported. In this case, the imported terminology will overwrite an existing terminology of the same name.
Possible values:

OVERWRITE
    # data-file : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("translate", "import-terminology", "name", "merge-strategy", "data-file", add_option_dict)
