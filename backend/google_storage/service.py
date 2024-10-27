from google.cloud import storage
import asyncio

class StorageService:
    
    async def upload_file_to_gcs(self, bucket_name, source_file_name, destination_blob_name):
        # Use google.cloud.storage directly
        storage_client = storage.Client(project="skilful-rain-418418")
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        result = blob.upload_from_filename(source_file_name)
        
        print(f"{source_file_name} dosyası {destination_blob_name} olarak yüklendi.")

        blob_uri = f"gs://{bucket_name}/{destination_blob_name}"

        return blob_uri

bucket_name = "test_bucket"  # GCS bucket name
source_file_name = "/Users/celalcanaslan/Desktop/Image.jpeg"  # Local file path
destination_blob_name = "uploaded/Image.jpeg"  # Target filename in GCS

if __name__ == "__main__":
    storage_service = StorageService()  # Renamed instance variable
    asyncio.run(storage_service.upload_file_to_gcs(bucket_name, source_file_name, destination_blob_name))
