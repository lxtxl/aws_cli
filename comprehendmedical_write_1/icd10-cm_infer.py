#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/infer-icd10-cm.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # text : The input text used for analysis. The input for InferICD10CM is a string from 1 to 10000 characters.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("comprehendmedical", "infer-icd10-cm", "text", add_option_dict)





