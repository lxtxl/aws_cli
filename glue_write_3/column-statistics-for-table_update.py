#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-column-statistics-for-table.html
if __name__ == '__main__':
    """
	delete-column-statistics-for-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-column-statistics-for-table.html
	get-column-statistics-for-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-column-statistics-for-table.html
    """

    parameter_display_string = """
    # database-name : The name of the catalog database where the partitions reside.
    # table-name : The name of the partitionsâ table.
    # column-statistics-list : A list of the column statistics.
(structure)

Represents the generated column-level statistics for a table or partition.
ColumnName -> (string)

Name of column which statistics belong to.

ColumnType -> (string)

The data type of the column.

AnalyzedTime -> (timestamp)

The timestamp of when column statistics were generated.

StatisticsData -> (structure)

A ColumnStatisticData object that contains the statistics data values.
Type -> (string)

The type of column statistics data.

BooleanColumnStatisticsData -> (structure)

Boolean column statistics data.
NumberOfTrues -> (long)

The number of true values in the column.

NumberOfFalses -> (long)

The number of false values in the column.

NumberOfNulls -> (long)

The number of null values in the column.


DateColumnStatisticsData -> (structure)

Date column statistics data.
MinimumValue -> (timestamp)

The lowest value in the column.

MaximumValue -> (timestamp)

The highest value in the column.

NumberOfNulls -> (long)

The number of null values in the column.

NumberOfDistinctValues -> (long)

The number of distinct values in a column.


DecimalColumnStatisticsData -> (structure)

Decimal column statistics data.
MinimumValue -> (structure)

The lowest value in the column.
UnscaledValue -> (blob)

The unscaled numeric value.

Scale -> (integer)

The scale that determines where the decimal point falls in the unscaled value.


MaximumValue -> (structure)

The highest value in the column.
UnscaledValue -> (blob)

The unscaled numeric value.

Scale -> (integer)

The scale that determines where the decimal point falls in the unscaled value.


NumberOfNulls -> (long)

The number of null values in the column.

NumberOfDistinctValues -> (long)

The number of distinct values in a column.


DoubleColumnStatisticsData -> (structure)

Double column statistics data.
MinimumValue -> (double)

The lowest value in the column.

MaximumValue -> (double)

The highest value in the column.

NumberOfNulls -> (long)

The number of null values in the column.

NumberOfDistinctValues -> (long)

The number of distinct values in a column.


LongColumnStatisticsData -> (structure)

Long column statistics data.
MinimumValue -> (long)

The lowest value in the column.

MaximumValue -> (long)

The highest value in the column.

NumberOfNulls -> (long)

The number of null values in the column.

NumberOfDistinctValues -> (long)

The number of distinct values in a column.


StringColumnStatisticsData -> (structure)

String column statistics data.
MaximumLength -> (long)

The size of the longest string in the column.

AverageLength -> (double)

The average string length in the column.

NumberOfNulls -> (long)

The number of null values in the column.

NumberOfDistinctValues -> (long)

The number of distinct values in a column.


BinaryColumnStatisticsData -> (structure)

Binary column statistics data.
MaximumLength -> (long)

The size of the longest bit sequence in the column.

AverageLength -> (double)

The average bit sequence length in the column.

NumberOfNulls -> (long)

The number of null values in the column.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("glue", "update-column-statistics-for-table", "database-name", "table-name", "column-statistics-list", add_option_dict)
