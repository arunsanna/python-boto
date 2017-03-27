import boto3
import sys

#Need to iterate over regions
def get_regions():
    client = boto3.client('ec2')
    region_response = client.describe_regions()
    regions = [region['RegionName'] for region in region_response['Regions']]
    return regions

for region in get_regions():
    print region

#calling the functions

#sg_id = str(sys.argv[1])
#
#  client = boto3.client('ec2', region_name=n)
#  reg_con = boto.ec2.connect_to_region(us-east-1)
#  print reg_con
#sec_conn = boto.connect_ec2()
#grp = sec_conn.get_all_security_groups()
#if grp:
#    for g in grp:
#        if g.id == sg_id:
#          print 'you are about to update the security group', g.name
#          g.revoke('tcp',80,80,'68.255.14.150/32')

#for sec in sec_all:
#    print sec.name

#sg = sec_all[1]
#print sg.group_name
#print sg.rules

