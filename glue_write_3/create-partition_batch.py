#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/batch-create-partition.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # database-name : The name of the metadata database in which the partition is to be created.
    # table-name : The name of the metadata table in which the partition is to be created.
    # partition-input-list : A list of PartitionInput structures that define the partitions to be created.
(structure)

The structure used to create and update a partition.
Values -> (list)

The values of the partition. Although this parameter is not required by the SDK, you must specify this parameter for a valid input.
The values for the keys for the new partition must be passed as an array of String objects that must be ordered in the same order as the partition keys appearing in the Amazon S3 prefix. Otherwise AWS Glue will add the values to the wrong keys.
(string)

LastAccessTime -> (timestamp)

The last time at which the partition was accessed.

StorageDescriptor -> (structure)

Provides information about the physical location where the partition is stored.
Columns -> (list)

A list of the Columns in the table.
(structure)

A column in a Table .
Name -> (string)

The name of the Column .

Type -> (string)

The data type of the Column .

Comment -> (string)

A free-form text comment.

Parameters -> (map)

These key-value pairs define properties associated with the column.
key -> (string)
value -> (string)



Location -> (string)

The physical location of the table. By default, this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.

InputFormat -> (string)

The input format: SequenceFileInputFormat (binary), or TextInputFormat , or a custom format.

OutputFormat -> (string)

The output format: SequenceFileOutputFormat (binary), or IgnoreKeyTextOutputFormat , or a custom format.

Compressed -> (boolean)

True if the data in the table is compressed, or False if not.

NumberOfBuckets -> (integer)

Must be specified if the table contains any dimension columns.

SerdeInfo -> (structure)

The serialization/deserialization (SerDe) information.
Name -> (string)

Name of the SerDe.

SerializationLibrary -> (string)

Usually the class that implements the SerDe. An example is org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe .

Parameters -> (map)

These key-value pairs define initialization parameters for the SerDe.
key -> (string)
value -> (string)


BucketColumns -> (list)

A list of reducer grouping columns, clustering columns, and bucketing columns in the table.
(string)

SortColumns -> (list)

A list specifying the sort order of each bucket in the table.
(structure)

Specifies the sort order of a sorted column.
Column -> (string)

The name of the column.

SortOrder -> (integer)

Indicates that the column is sorted in ascending order (== 1 ), or in descending order (==0 ).



Parameters -> (map)

The user-supplied properties in key-value form.
key -> (string)
value -> (string)

SkewedInfo -> (structure)

The information about values that appear frequently in a column (skewed values).
SkewedColumnNames -> (list)

A list of names of columns that contain skewed values.
(string)

SkewedColumnValues -> (list)

A list of values that appear so frequently as to be considered skewed.
(string)

SkewedColumnValueLocationMaps -> (map)

A mapping of skewed values to the columns that contain them.
key -> (string)
value -> (string)


StoredAsSubDirectories -> (boolean)

True if the table data is stored in subdirectories, or False if not.

SchemaReference -> (structure)

An object that references a schema stored in the AWS Glue Schema Registry.
When creating a table, you can pass an empty list of columns for the schema, and instead use a schema reference.
SchemaId -> (structure)

A structure that contains schema identity fields. Either this or the SchemaVersionId has to be provided.
SchemaArn -> (string)
SchemaName -> (string)
RegistryName -> (string)

SchemaVersionId -> (string)

The unique ID assigned to a version of the schema. Either this or the SchemaId has to be provided.

SchemaVersionNumber -> (long)

The version number of the schema.



Parameters -> (map)

These key-value pairs define partition parameters.
key -> (string)
value -> (string)

LastAnalyzedTime -> (timestamp)

The last time at which column statistics were computed for this partition.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("glue", "batch-create-partition", "database-name", "table-name", "partition-input-list", add_option_dict)
