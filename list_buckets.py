import boto
s3_conn = boto.connect_s3()
rs = s3_conn.get_all_buckets()
for b in rs:
    print b.name