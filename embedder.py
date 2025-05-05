from pymongo import MongoClient
from sentence_transformers import SentenceTransformer

# Load your embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Connect to MongoDB
client = MongoClient("mongodb+srv://<username>:<password>@<cluster-url>/?retryWrites=true&w=majority")
db = client["OptumMatch"]
collection = db["Patient-Provider"]

# Fetch the specific document for p001
doc = collection.find_one({"provider_id": "p001"})
if not doc:
    print("❌ No document found with provider_id = 'p001'")
    exit()

text = doc.get("profileText", "")
if not text:
    print("⚠️ 'p001' has no profileText — skipping")
    exit()

# Generate new embedding
embedding = model.encode(text).tolist()

# Update in-place
collection.update_one(
    {"provider_id": "p001"},
    {"$set": {"profileEmbedding": embedding}}
)

print(f"✅ Re-embedded p001 with {len(embedding)} dimensions (should be 384)")
