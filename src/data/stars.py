import uuid
from datetime import datetime


dummy_data = [
    {
      "id": str(uuid.uuid4()),
      "name": "Sun",
      "description": "",
      "mass": "1.9885x10^30 kg",
      "volume": "1.412x10^18 km3",
      "temperature": "15699726,85 °C",
      "created_at": datetime.now(),
      "updated_at": datetime.now(),
      "image": ""
    }
]
