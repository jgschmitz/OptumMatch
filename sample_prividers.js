sample_providers = [
    {
        "provider_id": "p002",
        "specialty": "psychiatry",
        "location": "Chicago",
        "profileText": "Dr. Patel specializes in adolescent mental health, focusing on CBT and medication management for anxiety and depression."
    },
    {
        "provider_id": "p003",
        "specialty": "endocrinology",
        "location": "Boston",
        "profileText": "Dr. Lee helps patients manage diabetes and thyroid disorders with compassionate, long-term care plans."
    },
    {
        "provider_id": "p004",
        "specialty": "primary care",
        "location": "San Francisco",
        "profileText": "Dr. Johnson offers preventive and wellness care with attention to diversity, lifestyle, and long-term health outcomes."
    },
    {
        "provider_id": "p005",
        "specialty": "dermatology",
        "location": "Austin",
        "profileText": "Dr. Yang provides comprehensive dermatological care with a focus on acne, eczema, and cosmetic skin procedures."
    },
    {
        "provider_id": "p006",
        "specialty": "pediatrics",
        "location": "Seattle",
        "profileText": "Dr. Ramirez focuses on whole-child pediatric care, emphasizing development, nutrition, and emotional health."
    },
    {
        "provider_id": "p008",
        "specialty": "oncology",
        "location": "Atlanta",
        "profileText": "Dr. Taylor supports patients through cancer treatment with personalized care plans, emotional support, and integrative therapies."
    },
    {
        "provider_id": "p009",
        "specialty": "orthopedics",
        "location": "New York",
        "profileText": "Dr. Singh specializes in sports injuries and joint replacement surgery, with an emphasis on rapid recovery."
    },
    {
        "provider_id": "p010",
        "specialty": "gastroenterology",
        "location": "Phoenix",
        "profileText": "Dr. Chen treats digestive disorders with an emphasis on nutrition, gut health, and evidence-based interventions."
    }
]

# Insert or update documents in the collection
for provider in sample_providers:
    db["Patient-Provider"].update_one(
        {"provider_id": provider["provider_id"]},
        {"$set": provider},
        upsert=True
    )

print("✅ Sample providers inserted or updated.")
