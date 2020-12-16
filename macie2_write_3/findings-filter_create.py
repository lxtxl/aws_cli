#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/create-findings-filter.html
if __name__ == '__main__':
    """
	delete-findings-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/delete-findings-filter.html
	get-findings-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/get-findings-filter.html
	list-findings-filters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/list-findings-filters.html
	update-findings-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/update-findings-filter.html
    """

    parameter_display_string = """
    # action : The action to perform on findings that meet the filter criteria (findingCriteria). Valid values are: ARCHIVE, suppress (automatically archive) the findings; and, NOOP, donât perform any action on the findings.
Possible values:

ARCHIVE
NOOP
    # finding-criteria : 
    # name : A custom name for the filter. The name must contain at least 3 characters and can contain as many as 64 characters.
We strongly recommend that you avoid including any sensitive data in the name of a filter. Other users of your account might be able to see the filterâs name, depending on the actions that theyâre allowed to perform in Amazon Macie.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("macie2", "create-findings-filter", "action", "finding-criteria", "name", add_option_dict)
