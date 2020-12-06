#!/bin/bash

if [ "$#" != 2 ];then
  echo "Usage: ./get_s3api_1.sh [innotree] [bucket_name]"
  exit 1;
fi

PROFILE_NAME=$1
BUCKET_NAME=$2

python s3api_read_1/bucket-accelerate-configuration_get.py $PROFILE_NAME $BUCKET_NAME
python s3api_read_1/bucket-acl_get.py $PROFILE_NAME $BUCKET_NAME
python s3api_read_1/bucket-analytics-configuration_list.py $PROFILE_NAME $BUCKET_NAME
python s3api_read_1/bucket-cor_get.py $PROFILE_NAME $BUCKET_NAME
python s3api_read_1/bucket-encryption_get.py $PROFILE_NAME $BUCKET_NAME
python s3api_read_1/bucket-intelligent-tiering-configuration_list.py $PROFILE_NAME $BUCKET_NAME
python s3api_read_1/bucket-inventory-configuration_list.py $PROFILE_NAME $BUCKET_NAME
python s3api_read_1/bucket-lifecycle-configuration_get.py $PROFILE_NAME $BUCKET_NAME
python s3api_read_1/bucket-location_get.py $PROFILE_NAME $BUCKET_NAME
python s3api_read_1/bucket-logging_get.py $PROFILE_NAME $BUCKET_NAME
python s3api_read_1/bucket-metrics-configuration_list.py $PROFILE_NAME $BUCKET_NAME
python s3api_read_1/bucket-notification-configuration_get.py $PROFILE_NAME $BUCKET_NAME
python s3api_read_1/bucket-ownership-control_get.py $PROFILE_NAME $BUCKET_NAME
python s3api_read_1/bucket-policy-status_get.py $PROFILE_NAME $BUCKET_NAME
python s3api_read_1/bucket-policy_get.py $PROFILE_NAME $BUCKET_NAME
python s3api_read_1/bucket-replication_get.py $PROFILE_NAME $BUCKET_NAME
python s3api_read_1/bucket-request-payment_get.py $PROFILE_NAME $BUCKET_NAME
python s3api_read_1/bucket-tagging_get.py $PROFILE_NAME $BUCKET_NAME
python s3api_read_1/bucket-versioning_get.py $PROFILE_NAME $BUCKET_NAME
python s3api_read_1/bucket-website_get.py $PROFILE_NAME $BUCKET_NAME
python s3api_read_1/multipart-upload_list.py $PROFILE_NAME $BUCKET_NAME
python s3api_read_1/object-lock-configuration_get.py $PROFILE_NAME $BUCKET_NAME
python s3api_read_1/object-version_list.py $PROFILE_NAME $BUCKET_NAME
python s3api_read_1/object_list.py $PROFILE_NAME $BUCKET_NAME
python s3api_read_1/objects-v2_list.py $PROFILE_NAME $BUCKET_NAME
python s3api_read_1/public-access-block_get.py $PROFILE_NAME $BUCKET_NAME
