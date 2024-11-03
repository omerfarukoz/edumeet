from google.cloud import storage


class StorageService:


        # This function uploads a file to a bucket in GCS for meeting recordings and materials
        # It returns the blob uri of the uploaded file

    async def upload_file_to_gcs(self, bucket_name, source_file_name, destination_blob_name, project_id:str):

        # Use google.cloud.storage directly

        storage_client = storage.Client(project=project_id)
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        result = blob.upload_from_filename(source_file_name)
        
        print(f"{source_file_name} dosyası {destination_blob_name} olarak yüklendi.")

        blob_uri = f"gs://{bucket_name}/{destination_blob_name}"

        return blob_uri

