#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis-video-archived-media/get-media-for-fragment-list.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # stream-name : The name of the stream from which to retrieve fragment media.
    # fragments : A list of the numbers of fragments for which to retrieve media. You retrieve these values with  ListFragments .
(string)
    """

    execute_two_parameter("kinesis-video-archived-media", "get-media-for-fragment-list", "stream-name", "fragments", parameter_display_string)