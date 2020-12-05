#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/delete-terminology.html
if __name__ == '__main__':
    """
	get-terminology : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/get-terminology.html
	import-terminology : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/import-terminology.html
	list-terminologies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/list-terminologies.html
    """

    parameter_display_string = """
    # name : The name of the custom terminology being deleted.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("translate", "delete-terminology", "name", add_option_dict)





