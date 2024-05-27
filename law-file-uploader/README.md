# LAW File Uploader

## Description
Simple script to upload data to a Log Analytics Workspace DCR based custom table using the Log Ingestion API.

The <b>Azure Monitor HTTP Data Collector API</b> has been deprecated and will no longer be functional as of 9/14/2026. It's been replaced by the <b>Logs ingestion API</b>.

## Prerequisites
<ol>
    <li>Create a Data Collection Endpoint from Azure Monitor.</li>
    <li>Create a DCR based table using the sample squema definition.</li>
    <li>Create a service principal with <b>Monitoring Metrics Publisher</b> role in the DCR.</li>
</ol>

- Detailed instructions: https://learn.microsoft.com/en-us/azure/azure-monitor/logs/tutorial-logs-ingestion-api

## Instructions
<ol>
    <li>Assign values to the environment variables in .env file.</li>
    <li>Assign values to the variables in main.py file.</li>
    <li>Run main.py file in order to upload the data.</li>
</ol>

## Reference
- Log Ingestion API overview: https://learn.microsoft.com/en-us/azure/azure-monitor/logs/logs-ingestion-api-overview