# PythonHttpResponseAsCSV
Repo shows how a Python function app both read and write to blob storage and return a csv file in the HttpResponse

Note: When deployed make sure to check that the Function App -> Configuration shows a Key named: AZURE_STORAGE_CONNECTION_STRING with the value of the blob storage accounts connection string.

Additionally, it shows how to use CSV reader and writer. Azure restricts write operations on the host, so it is recommended to use blob storage or other storage methods
