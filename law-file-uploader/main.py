from azure.identity import DefaultAzureCredential
from azure.monitor.ingestion import LogsIngestionClient
from azure.core.exceptions import HttpResponseError
from dotenv import load_dotenv

DCE_ENDPOINT: str = None # Example:  https://dce-sentinel-test-8jfn.westeurope-1.ingest.monitor.azure.com
DCR_IMMUTABLE_ID: str = None # Example: dcr-e413300f6dac49429ca85dd303d9b021
STREAM_NAME: str = None # Example: Custom-Test_CL, Microsoft-CommonSecurityLog, Microsoft-Syslog

if __name__ == "__main__":
    # Load credential data from .env
    load_dotenv()

    # Log Ingestion API Client definition
    credential: DefaultAzureCredential = DefaultAzureCredential()
    client: LogsIngestionClient | LogsIngestionClient = LogsIngestionClient(endpoint=DCE_ENDPOINT, credential=credential, logging_enable=True)

    # Set the data to be uploaded.
    body: list[dict[str, str]] = [
            {
            "TimeGenerated": "2023-03-12T15:04:48.423211Z",
            "Message": "Test"
            }
        ]

    # Upload data
    try:
        client.upload(rule_id=DCR_IMMUTABLE_ID, stream_name=STREAM_NAME, logs=body)
    except HttpResponseError as e:
        print(f"Upload failed: {e}")
