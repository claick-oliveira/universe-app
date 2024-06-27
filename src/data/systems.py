import uuid
from datetime import datetime


dummy_data = [
    {
      "id": str(uuid.uuid4()),
      "name": "Solar System",
      "created_at": datetime.now(),
      "updated_at": datetime.now()
    }
]
