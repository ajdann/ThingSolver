from minio import Minio
from minio.error import S3Error
from datetime import datetime

def download(name):


    # Create a client with the MinIO server playground, its access key
    # and secret key.
    print("upload file " + file.filename)
    client = Minio(
        "play.min.io",
        access_key="Q3AM3UQ867SPQQA43P2F",
        secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
    )

   
    found = client.bucket_exists("ajdin")
    if not found:
        client.make_bucket("ajdin")
    else:
        print("Bucket 'ajdin' already exists")

    client.fput_object(
        "ajdin", "test/"+ now + file.filename, "./" + file.filename,
    )
    client.fget_object(bucket_name='ajdin',)
    print(
        "'./" + file.filename +" is successfully uploaded as "
        "object" + file.filename + " to bucket 'ajdin'."
    )


if __name__ == "__main__":
    try:
        download()
    except S3Error as exc:
        print("error occurred.", exc)