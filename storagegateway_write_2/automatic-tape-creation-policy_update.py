#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/update-automatic-tape-creation-policy.html
if __name__ == '__main__':
    """
	delete-automatic-tape-creation-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/delete-automatic-tape-creation-policy.html
	list-automatic-tape-creation-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/list-automatic-tape-creation-policies.html
    """

    parameter_display_string = """
    # automatic-tape-creation-rules : An automatic tape creation policy consists of a list of automatic tape creation rules. The rules determine when and how to automatically create new tapes.
(structure)

An automatic tape creation policy consists of automatic tape creation rules where each rule defines when and how to create new tapes. For more information about automatic tape creation, see Creating Tapes Automatically .
TapeBarcodePrefix -> (string)

A prefix that you append to the barcode of the virtual tape that you are creating. This prefix makes the barcode unique.

Note
The prefix must be 1-4 characters in length and must be one of the uppercase letters from A to Z.


PoolId -> (string)

The ID of the pool that you want to add your tape to for archiving. The tape in this pool is archived in the Amazon S3 storage class that is associated with the pool. When you use your backup application to eject the tape, the tape is archived directly into the storage class (S3 Glacier or S3 Glacier Deep Archive) that corresponds to the pool.
Valid Values: GLACIER | DEEP_ARCHIVE

TapeSizeInBytes -> (long)

The size, in bytes, of the virtual tape capacity.

MinimumNumTapes -> (integer)

The minimum number of available virtual tapes that the gateway maintains at all times. If the number of tapes on the gateway goes below this value, the gateway creates as many new tapes as are needed to have MinimumNumTapes on the gateway. For more information about automatic tape creation, see Creating Tapes Automatically .

Worm -> (boolean)

Set to true to indicate that tapes are to be archived as write-once-read-many (WORM). Set to false when WORM is not enabled for tapes.
    # gateway-arn : The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("storagegateway", "update-automatic-tape-creation-policy", "automatic-tape-creation-rules", "gateway-arn", add_option_dict)
