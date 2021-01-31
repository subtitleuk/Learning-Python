#### SENDER ####

import uuid

# For working at the queue level, within a storage account
from azure.storage.queue import QueueClient

processing_queue_name = "processing-queue-id-" + str(uuid.uuid4())[0:4]
connect_str = "<Your storage account connection string (without authentication) goes here>"

# Authentication library
from azure.identity import ClientSecretCredential

# Information for authenticating using a Service Principal (the identity of our application)
tenant_id = "<Your Azure AD tenant ID goes here"
client_id = "<Your registered application ID goes here>"
client_secret ="<Your registered application secret goes here>"

# Get the application credentials
app_credentials = ClientSecretCredential(tenant_id, client_id, client_secret)

# Create a queue client, using the application Azure AD credentials
queue_client = QueueClient.from_connection_string(connect_str, processing_queue_name, credential=app_credentials)
print("Client connected to Queue")

# Create a new queue
queue_client.create_queue()
print("Created queue: " + processing_queue_name)



#### PROCESSING CLIENT ####

# Send messages to the queue
print("\nLet's add some messages...")
queue_client.send_message(u"Message 1")
queue_client.send_message(u"Message 2")
saved_message = queue_client.send_message(u"Message 3")

print("\nLet's PEEK at the messages in the queue...")

# Peek at messages in the queue
peeked_messages = queue_client.peek_messages(max_messages=5)

for peeked_message in peeked_messages:
    # List the message
    print("Message: " + peeked_message.content)