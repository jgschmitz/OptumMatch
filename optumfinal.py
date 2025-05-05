from pymongo import MongoClient

# Connect to Atlas
client = MongoClient("mongodb+srv://<username>:<password>@<cluster-url>/?retryWrites=true&w=majority")
db = client["OptumMatch"]
collection = db["Patient-Provider"]

# Use one doc as the query source (can be patient OR provider)
query_doc = collection.find_one({"provider_id": "p001"})
if not query_doc:
    print("❌ No document found with provider_id = 'p001'")
    exit()

query_vector = query_doc["profileEmbedding"]

# 🔍 Simplified vector search pipeline (no match filtering)
pipeline = [
    {
        "$vectorSearch": {
            "index": "united",  # Your Atlas vector index
            "path": "profileEmbedding",
            "queryVector": query_vector,
            "numCandidates": 10,
            "limit": 5
        }
    },
    {
        "$project": {
            "_id": 0,
            "provider_id": 1,
            "specialty": 1,
            "location": 1,
            "profileText": 1,
            "score": { "$meta": "vectorSearchScore" }
        }
    }
]

# Run aggregation
results = list(collection.aggregate(pipeline))

# Output results
for r in results:
    print(f"🩺 {r['provider_id']} ({r.get('specialty', 'N/A')}, {r.get('location', 'N/A')})")
    print(f"   📄 {r.get('profileText', '[No profile text]')}")
    print(f"   ⭐ Similarity Score: {round(r['score'], 3)}\n")
