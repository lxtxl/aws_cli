#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object-torrent.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # bucket : The name of the bucket containing the object for which to get the torrent files.
    # key : The object key for which to get the information.
    """

    execute_two_parameter("s3api", "get-object-torrent", "bucket", "key", parameter_display_string)