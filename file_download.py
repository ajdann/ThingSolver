from minio import Minio
from minio.error import S3Error
from datetime import datetime

def download(name):


    # Create a client with the MinIO server playground, its access key
    # and secret key.
    print("download file " + name)
    client = Minio(
        "play.min.io",
        access_key="Q3AM3UQ867SPQQA43P2F",
        secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
    )

   


    foundObject = client.fget_object(bucket_name='ajdin',object_name=name,file_path="./downloads/" + name)
    return foundObject


if __name__ == "__main__":
    try:
        download()
    except S3Error as exc:
        print("error occurred.", exc)
        raise exc