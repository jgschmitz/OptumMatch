# OptumMatch

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jgschmitz/OptumMatch/blob/main/notebooks/starter.ipynb)


These two scripts do similar jobs (matching patients to providers), but the approach and architecture are quite different. 
Here is how to get started....

🧪 Optum Match Starter Notebook (MongoDB Atlas Vector Search)

# 🧠 Step 1: Imports
```
from pymongo import MongoClient
import pandas as pd
import pprint
```
# 🚀 Step 2: Connect to MongoDB Atlas
```
client = MongoClient("mongodb+srv://<username>:<password>@<cluster-url>/?retryWrites=true&w=majority")
db = client["OptumMatch"]
collection = db["Patient-Provider"]
```
# 🔍 Step 3: Choose a provider or patient as the query source
```
query_doc = collection.find_one({"provider_id": "p001"})

if not query_doc:
    raise ValueError("❌ No provider found with provider_id='p001'")

query_vector = query_doc["profileEmbedding"]
print(f"✅ Loaded vector with {len(query_vector)} dimensions")
```
# 📈 Step 4: Define $vectorSearch pipeline
```
pipeline = [
    {
        "$vectorSearch": {
            "index": "united",  # Update if your index has a different name
            "path": "profileEmbedding",
            "queryVector": query_vector,
            "numCandidates": 100,
            "limit": 5
        }
    },
    {
        "$match": {
            "provider_id": {"$ne": query_doc["provider_id"]}  # avoid matching to self
        }
    },
    {
        "$project": {
            "_id": 0,
            "provider_id": 1,
            "name": 1,
            "specialty": 1,
            "location": 1,
            "profileText": 1,
            "score": {"$meta": "vectorSearchScore"}
        }
    }
]
```
# 🧪 Step 5: Run aggregation and format results
results = list(collection.aggregate(pipeline))
```
# Convert to DataFrame for easier display
df = pd.DataFrame(results)
df["score"] = df["score"].round(3)
df = df.sort_values("score", ascending=False)
```
# 🖼️ Display the top matches
```
df[["provider_id", "name", "specialty", "location", "score", "profileText"]]
```
