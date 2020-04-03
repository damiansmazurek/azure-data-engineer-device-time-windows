import uuid
import time
from azure.eventhub import EventHubProducerClient, EventDataBatch, EventData
import json

class DeviceEmulator:
    def __init__(self, connectionstring, eventhub_name):
        self.client = EventHubProducerClient.from_connection_string(connectionstring, eventhub_name=eventhub_name )
        # Create Event Hubs client
        self.deviceId = uuid.uuid4()

    def send_data(self, data):
        # Send message to eventhub
        self.send_batch_data([data])

    def send_batch_data(self, dataBatch):
        # Send batch data to eventhub
        batchData = EventDataBatch()
        for item in dataBatch:
            message = {"deviceid": self.deviceId, "timestamp": time.time(), "data": item}
            batchData.add(EventData(json.dumps(message)))
        self.client.send_batch(batchData)
        
