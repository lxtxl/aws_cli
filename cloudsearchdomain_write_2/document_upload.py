#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearchdomain/upload-documents.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # documents : 
    # content-type : The format of the batch you are uploading. Amazon CloudSearch supports two document batch formats:

application/json
application/xml

Possible values:

application/json
application/xml
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cloudsearchdomain", "upload-documents", "documents", "content-type", add_option_dict)
