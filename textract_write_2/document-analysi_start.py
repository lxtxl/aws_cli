#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/textract/start-document-analysis.html
if __name__ == '__main__':
    """
	get-document-analysis : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/textract/get-document-analysis.html
    """

    parameter_display_string = """
    # document-location : 
    # feature-types : A list of the types of analysis to perform. Add TABLES to the list to return information about the tables that are detected in the input document. Add FORMS to return detected form data. To perform both types of analysis, add TABLES and FORMS to FeatureTypes . All lines and words detected in the document are included in the response (including text that isnât related to the value of FeatureTypes ).
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("textract", "start-document-analysis", "document-location", "feature-types", add_option_dict)
