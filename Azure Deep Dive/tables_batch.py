import time

table_name = "coursecatalog"
connect_str = "MAGIC"

from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity 

# Let's import the batch library
from azure.cosmosdb.table.tablebatch import TableBatch

# Connect to the Table service
table_service = TableService(connection_string=connect_str)
print("\nConnected to Table service")

# Let's perform a batch transaction, and add two course expiry dates
batch = TableBatch()
task001 = {'PartitionKey': 'Azure', 'RowKey': '280',
    'expiryDate': '1 July 2020'}
task002 = {'PartitionKey': 'Azure', 'RowKey': '381',
    'expiryDate': '1 July 2020'}

# Perform batch transaction using MERGE (could be update, insert, etc)
batch.merge_entity(task001)
batch.merge_entity(task002)
table_service.commit_batch(table_name, batch)

print("\nBatch transaction complete")
print("=======================")