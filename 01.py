import json
import boto3


def lambda_handler(event, context):
    # Create an S3 client
    s3 = boto3.client('s3')
    
    # Retrieve the email IDs from the file in S3
    bucket_name = '<your_bucket_name>'
    file_name = '<your_file_name>'
    response = s3.get_object(Bucket=bucket_name, Key=file_name)
    email_ids = response['Body'].read().decode('utf-8').split('\n')
    
    # Create an SES client
    ses = boto3.client('ses')
    
    # Send emails to the retrieved email IDs
    for email_id in email_ids:
        if email_id.strip() != '':
            response = ses.send_email(
                Source='<your_verified_email>',
                Destination={
                    'ToAddresses': [
                        email_id.strip()
                    ]
                },
                Message={
                    'Subject': {
                        'Data': '<your_subject>'
                    },
                    'Body': {
                        'Text': {
                            'Data': '<your_email_body>'
                        }
                    }
                }
            )
            
            print(f"Email sent to: {email_id.strip()}")


    return {
        'statusCode': 200,
         'body': json.dumps('Emails sent successfully')
    }