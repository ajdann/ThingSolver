from minio import Minio
from minio.error import S3Error
from datetime import datetime

def remove(name):


    # Create a client with the MinIO server playground, its access key
    # and secret key.
    print("remove file " + name)
    client = Minio(
        "play.min.io",
        access_key="Q3AM3UQ867SPQQA43P2F",
        secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
    )

   


    removedObject = client.remove_object("ajdin", name)
    return removedObject


if __name__ == "__main__":
    try:
        remove()
    except S3Error as exc:
        print("error occurred.", exc)
        raise exc