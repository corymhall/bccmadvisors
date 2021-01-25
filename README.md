# bccmadvisors Website 

## My Bucket Policy

`{
    "Version": "2012-10-17",
    "Id": "Policy1610741923542",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::cloudfront:user/CloudFront Origin Access Identity E18BP4LIPAR2OD"
            },
            "Action": [
                "s3:GetObject*",
                "s3:GetBucket*",
                "s3:List*"
            ],
            "Resource": [
                "arn:aws:s3:::bccmwebsitebucket",
                "arn:aws:s3:::bccmwebsitebucket/*"
            ]
        },
        {
            "Sid": "Stmt1610741920838",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::111111111111:role/aws-elasticbeanstalk-ec2-role"
            },
            "Action": [
                "s3:DeleteObject",
                "s3:GetObject",
                "s3:PutObject"
            ],
            "Resource": "arn:aws:s3:::bccmwebsitebucket/*"
        },
        {
            "Sid": "Stmt1610741920838",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::111111111111:role/aws-elasticbeanstalk-ec2-role"
            },
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::bccmwebsitebucket"
        }
    ]
}`
