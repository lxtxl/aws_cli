#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/get-terminology.html
if __name__ == '__main__':
    """
	delete-terminology : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/delete-terminology.html
	import-terminology : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/import-terminology.html
	list-terminologies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/list-terminologies.html
    """

    parameter_display_string = """
    # name : The name of the custom terminology being retrieved.
    # terminology-data-format : The data format of the custom terminology being retrieved, either CSV or TMX.
Possible values:

CSV
TMX
    """

    execute_two_parameter("translate", "get-terminology", "name", "terminology-data-format", parameter_display_string)