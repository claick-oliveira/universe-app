import uuid
from datetime import datetime


dummy_data = [
    {
      "id": str(uuid.uuid4()),
      "name": "Mercury",
      "description": "",
      "type": "Rocky",
      "mass": "3.3011x10^23 kg",
      "volume": "6.083x10^10 km3",
      "temperature": "67 °C",
      "created_at": datetime.now(),
      "updated_at": datetime.now(),
      "image": ""
    },
    {
      "id": str(uuid.uuid4()),
      "name": "Venus",
      "description": "",
      "type": "Rocky",
      "mass": "4.8675x10^24 kg",
      "volume": "9.2843x10^11 km3",
      "temperature": "464 °C",
      "created_at": datetime.now(),
      "updated_at": datetime.now(),
      "image": ""
    },
    {
      "id": str(uuid.uuid4()),
      "name": "Earth",
      "description": "",
      "type": "Rocky",
      "mass": "5.972168x10^24 kg",
      "volume": "1.08321x10^12 km3",
      "temperature": "14.76 °C",
      "created_at": datetime.now(),
      "updated_at": datetime.now(),
      "image": ""
    },
    {
      "id": str(uuid.uuid4()),
      "name": "Mars",
      "description": "",
      "type": "Rocky",
      "mass": "6.4171x10^23 kg",
      "volume": "1.63118x10^11 km3",
      "temperature": "-60 °C",
      "created_at": datetime.now(),
      "updated_at": datetime.now(),
      "image": ""
    },
    {
      "id": str(uuid.uuid4()),
      "name": "Jupiter",
      "description": "",
      "type": "Gaseous",
      "mass": "1.8982x10^27 kg",
      "volume": "1.4313x10^15 km3",
      "temperature": "-108.15 °C",
      "created_at": datetime.now(),
      "updated_at": datetime.now(),
      "image": ""
    },
    {
      "id": str(uuid.uuid4()),
      "name": "Saturn",
      "description": "",
      "type": "Gaseous",
      "mass": "5.6834x10^26 kg",
      "volume": "8.2713x10^14 km3",
      "temperature": "-139.15 °C",
      "created_at": datetime.now(),
      "updated_at": datetime.now(),
      "image": ""
    },
    {
      "id": str(uuid.uuid4()),
      "name": "Uranus",
      "description": "",
      "type": "Gaseous",
      "mass": "8.6810x10^25 kg",
      "volume": "6.833x10^13 km3",
      "temperature": "-197.2 °C",
      "created_at": datetime.now(),
      "updated_at": datetime.now(),
      "image": ""
    },
    {
      "id": str(uuid.uuid4()),
      "name": "Neptune",
      "description": "",
      "type": "Gaseous",
      "mass": "1.02409x10^26 kg",
      "volume": "6.253x10^13 km3",
      "temperature": "-201 °C",
      "created_at": datetime.now(),
      "updated_at": datetime.now(),
      "image": ""
    }
]
