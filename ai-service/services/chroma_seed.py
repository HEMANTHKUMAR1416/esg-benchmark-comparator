import chromadb
from sentence_transformers import SentenceTransformer

# init
client = chromadb.Client()
collection = client.get_or_create_collection(name="esg_knowledge")

model = SentenceTransformer("all-MiniLM-L6-v2")

# 🔟 ESG domain docs (simple but useful)
docs = [
    "High environmental scores indicate low emissions and strong sustainability practices.",
    "Low environmental score suggests high pollution or poor energy management.",
    "Strong governance reflects transparent policies and ethical leadership.",
    "Weak governance may indicate corruption risk or poor compliance.",
    "High social score shows good employee welfare and community impact.",
    "Low social score indicates poor labor practices or social responsibility.",
    "Companies should invest in renewable energy to improve ESG performance.",
    "Reducing carbon footprint improves environmental sustainability.",
    "Board diversity improves governance quality.",
    "Sustainability reporting increases investor trust."
]

# embeddings
embeddings = model.encode(docs).tolist()

# add to DB
collection.add(
    documents=docs,
    embeddings=embeddings,
    ids=[str(i) for i in range(len(docs))]
)

print("✅ ChromaDB seeded with 10 ESG documents")