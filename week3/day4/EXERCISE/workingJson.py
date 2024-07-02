#  Exercise 2: Working With JSON
# Instructions

import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""


# Access the nested “salary” key from the JSON-string above.
# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
# Save the dictionary as JSON to a file.

data = json.loads(sampleJson)

print(data['company']['employee']['payable']['salary'])

data['company']['employee']['birth date'] = '2024-06-25'

data['company']['employee']['payable']['discount'] = 2000

with open('D:/Bootcamp_2024/week3/day4/josi.json', 'w') as file_object:
  json.dump(data, file_object, indent=2, sort_keys=True)



