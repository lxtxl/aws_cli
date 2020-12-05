#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/batch-put-asset-property-value.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # entries : The list of asset property value entries for the batch put request. You can specify up to 10 entries per request.
(structure)

Contains a list of value updates for an asset property in the list of asset entries consumed by the BatchPutAssetPropertyValue API operation.
entryId -> (string)

The user specified ID for the entry. You can use this ID to identify which entries failed.

assetId -> (string)

The ID of the asset to update.

propertyId -> (string)

The ID of the asset property for this entry.

propertyAlias -> (string)

The property alias that identifies the property, such as an OPC-UA server data stream path (for example, /company/windfarm/3/turbine/7/temperature ). For more information, see Mapping industrial data streams to asset properties in the AWS IoT SiteWise User Guide .

propertyValues -> (list)

The list of property values to upload. You can specify up to 10 propertyValues array elements.
(structure)

Contains asset property value information.
value -> (structure)

The value of the asset property (see Variant ).
stringValue -> (string)

Asset property data of type string (sequence of characters).

integerValue -> (integer)

Asset property data of type integer (whole number).

doubleValue -> (double)

Asset property data of type double (floating point number).

booleanValue -> (boolean)

Asset property data of type Boolean (true or false).


timestamp -> (structure)

The timestamp of the asset property value.
timeInSeconds -> (long)

The timestamp date, in seconds, in the Unix epoch format. Fractional nanosecond data is provided by offsetInNanos .

offsetInNanos -> (integer)

The nanosecond offset from timeInSeconds .


quality -> (string)

The quality of the asset property value.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iotsitewise", "batch-put-asset-property-value", "entries", add_option_dict)





