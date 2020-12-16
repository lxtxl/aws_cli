#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ebs/get-snapshot-block.html
if __name__ == '__main__':
    """
	list-snapshot-blocks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ebs/list-snapshot-blocks.html
	put-snapshot-block : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ebs/put-snapshot-block.html
    """

    parameter_display_string = """
    # snapshot-id : The ID of the snapshot containing the block from which to get data.
    # block-index : The block index of the block from which to get data.
Obtain the BlockIndex by running the ListChangedBlocks or ListSnapshotBlocks operations.
    """

    execute_two_parameter("ebs", "get-snapshot-block", "snapshot-id", "block-index", parameter_display_string)