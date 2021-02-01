import time

new_table_name = "coursecatalog"
connect_str = "<Insert your full connection string here>"

# using cosmos db table api
from azure.cosmosdb.table.tableservice import TableService

# Cosmos DB supports multiple models; we can use the Entity class to simplify the addition of table data (entities)
from azure.cosmosdb.table.models import Entity 

# Connect to the Table service
table_service = TableService(connection_string=connect_str)
print("\nConnected to Table service")

# Create a new Table
table_service.create_table(new_table_name)
print("\nCreated table: " + new_table_name)

# Give some time for the table to be created
time.sleep(5)

# Add some data (ENTITIES) to the table - we use objects to represent our data
print("\nCreating entity...")

course_details = Entity()
course_details.PartitionKey = 'Azure'
course_details.RowKey = '280'
course_details.name = 'AZ-300'
course_details.author = 'James Lee'
course_details.description = 'Certification course for MS AZ-300'

# Insert data
print("\nAdding entity to table, '" + new_table_name + "'...")
table_service.insert_entity(new_table_name, course_details)

# Add some data (ENTITIES) to the table - we use objects to represent our data
print("\nCreating entity...")

course_details = Entity()
course_details.PartitionKey = 'Azure'
course_details.RowKey = '381'
course_details.name = 'AZ-301'
course_details.author = 'James Lee'
course_details.description = 'Certification course for MS AZ-301'

# Insert data
print("\nAdding entity to table, '" + new_table_name + "'...")
table_service.insert_entity(new_table_name, course_details)


# Add some data (ENTITIES) to the table - we use objects to represent our data
print("\nCreating entity...")

course_details = Entity()
course_details.PartitionKey = 'Azure'
course_details.RowKey = '441'
course_details.name = 'Azure Storage Deep Dive'
course_details.author = 'James Lee'
course_details.description = 'Deep dive in to the Azure Storage services'

# Insert data
print("\nAdding entity to table, '" + new_table_name + "'...")
table_service.insert_entity(new_table_name, course_details)

# Add some data (ENTITIES) to the table - we use objects to represent our data
print("\nCreating entity...")

course_details = Entity()
course_details.PartitionKey = 'Azure'
course_details.RowKey = '378'
course_details.name = 'DP-200'
course_details.author = 'Brian Roehm'
course_details.description = 'Microsoft Azure Exam DP-200 - Implementing an Azure Data Solution'

# Insert data
print("\nAdding entity to table, '" + new_table_name + "'...")
table_service.insert_entity(new_table_name, course_details)

# Add some data (ENTITIES) to the table - we use objects to represent our data
print("\nCreating entity...")

course_details = Entity()
course_details.PartitionKey = 'Azure'
course_details.RowKey = '367'
course_details.name = 'AZ-500'
course_details.author = 'Shawn Johnson'
course_details.description = 'AZ-500: Microsoft Azure Security Technologies'

# Insert data
print("\nAdding entity to table, '" + new_table_name + "'...")
table_service.insert_entity(new_table_name, course_details)

# Add some data (ENTITIES) to the table - we use objects to represent our data
print("\nCreating entity...")

course_details = Entity()
course_details.PartitionKey = 'DevOps'
course_details.RowKey = '367'
course_details.name = 'DCA'
course_details.author = 'Will Boyd'
course_details.description = 'Docker Certified Associate (DCA)'

# Insert data
print("\nAdding entity to table, '" + new_table_name + "'...")
table_service.insert_entity(new_table_name, course_details)

# Add some data (ENTITIES) to the table - we use objects to represent our data
print("\nCreating entity...")

course_details = Entity()
course_details.PartitionKey = 'DevOps'
course_details.RowKey = '305'
course_details.name = 'CKAD'
course_details.author = 'Will Boyd'
course_details.description = 'Certified Kubernetes Applicatino Developer (CKAD)'

# Insert data
print("\nAdding entity to table, '" + new_table_name + "'...")
table_service.insert_entity(new_table_name, course_details)

print("\n===== DONE =====")