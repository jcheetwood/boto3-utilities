"""
HOST ZONE ID and DNS NAME will need to replaced with AWS values.
"""

import boto3

client = boto3.client('route53')

east_states = ["ME", "VT", "NH", "MA", "CT", "RI", "NY", "NJ", "PA", "DE", "MD", "WV", "VA", "NC", "SC", "GA", "FL", "AL", "MS", "TN", "KY", "IL", "IN", "OH", "MI", "WI"]

west_states = ["WA", "OR", "CA", "ID", "NV", "MT", "WY", "UT", "AR", "CO", "NM", "ND", "SD", "NE", "KS", "OK", "TX", "MN", "IA", "MO", "AK", "LA", "AR", "HI"]

#for i in east_states:
#    print(i)


for i in east_states:
    try:
        response = client.change_resource_record_sets(
            HostedZoneId='HOSTED ZONE ID',
            ChangeBatch={
                'Changes': [
                    {
                        'Action': 'CREATE',
                        'ResourceRecordSet': {
                            'Name': 'DNS NAME',
                            'Type': 'A',
                            'SetIdentifier': i,
                            'GeoLocation': {
                                'CountryCode': 'US',
                                'SubdivisionCode': i
                            },
                            'AliasTarget': {
                                'HostedZoneId': 'HOSTED ZONE ID',
                                'DNSName': 'DNS NAME',
                                'EvaluateTargetHealth': False
                            },
                        }
                    },
                ]
            }
        )
    except:
        print("Record Already Exists.")