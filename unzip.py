import zipfile
zip_ref = zipfile.ZipFile('/tmp/627434363107-aws-billing-detailed-line-items-with-resources-and-tags-2016-10.csv.zip', 'r')
zip_ref.extractall('/tmp/')
zip_ref.close()