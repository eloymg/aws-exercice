import time
import boto3
import sys

s3 = boto3.client("s3")


def stillCPU():
    a = True
    t = time.time()
    while a:
        time.sleep(0.00001)
        if (time.time() - t) > 10:
            a = False


if __name__ == "__main__":
    stillCPU()
    s3.put_object(Bucket="aws-exercice-bucket", Key=sys.argv[1])
