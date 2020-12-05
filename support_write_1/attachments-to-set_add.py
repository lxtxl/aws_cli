#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/add-attachments-to-set.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # attachments : One or more attachments to add to the set. You can add up to three attachments per set. The size limit is 5 MB per attachment.
In the Attachment object, use the data parameter to specify the contents of the attachment file. In the previous request syntax, the value for data appear as blob , which is represented as a base64-encoded string. The value for fileName is the name of the attachment, such as troubleshoot-screenshot.png .
(structure)

An attachment to a case communication. The attachment consists of the file name and the content of the file.
fileName -> (string)

The name of the attachment file.

data -> (blob)

The content of the attachment file.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("support", "add-attachments-to-set", "attachments", add_option_dict)





