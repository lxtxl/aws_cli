#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/write-records.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # database-name : The name of the Timestream database.
    # table-name : The name of the Timesream table.
    # records : An array of records containing the unique dimension and measure attributes for each time series data point.
(structure)

Record represents a time series data point being written into Timestream. Each record contains an array of dimensions. Dimensions represent the meta data attributes of a time series data point such as the instance name or availability zone of an EC2 instance. A record also contains the measure name which is the name of the measure being collected for example the CPU utilization of an EC2 instance. A record also contains the measure value and the value type which is the data type of the measure value. In addition, the record contains the timestamp when the measure was collected that the timestamp unit which represents the granularity of the timestamp.
Dimensions -> (list)

Contains the list of dimensions for time series data points.
(structure)

Dimension represents the meta data attributes of the time series. For example, the name and availability zone of an EC2 instance or the name of the manufacturer of a wind turbine are dimensions.
Name -> (string)

Dimension represents the meta data attributes of the time series. For example, the name and availability zone of an EC2 instance or the name of the manufacturer of a wind turbine are dimensions.
For constraints on Dimension names, see Naming Constraints .

Value -> (string)

The value of the dimension.

DimensionValueType -> (string)

The data type of the dimension for the time series data point.



MeasureName -> (string)

Measure represents the data attribute of the time series. For example, the CPU utilization of an EC2 instance or the RPM of a wind turbine are measures.

MeasureValue -> (string)

Contains the measure value for the time series data point.

MeasureValueType -> (string)

Contains the data type of the measure value for the time series data point.

Time -> (string)

Contains the time at which the measure value for the data point was collected. The time value plus the unit provides the time elapsed since the epoch. For example, if the time value is 12345 and the unit is ms , then 12345 ms have elapsed since the epoch.

TimeUnit -> (string)

The granularity of the timestamp unit. It indicates if the time value is in seconds, milliseconds, nanoseconds or other supported values.

Version -> (long)

64-bit attribute used for record updates. Write requests for duplicate data with a higher version number will update the existing measure value and version. In cases where the measure value is the same, Version will still be updated . Default value is to 1.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("timestream-write", "write-records", "database-name", "table-name", "records", add_option_dict)
