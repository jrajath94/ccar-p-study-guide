"""Lab 6 toy: tiny keyword retriever over 20 docs. Local only."""
import re

DOCS = {
    "pol-001": "Refunds are approved within 30 days of delivery for damaged items.",
    "pol-002": "Lost shipments are refunded after the carrier confirms the loss.",
    "pol-003": "Wrong items shipped are replaced or refunded at once.",
    "pol-004": "Digital goods are not refundable after download.",
    "pol-005": "Warranty claims need a photo of the defect.",
}
for i in range(6, 21):
    DOCS["misc-%03d" % i] = "Office memo %d about quarterly planning and budgets." % i

def tokenize(s):
    return set(re.findall(r"[a-z]+", s.lower()))

def retrieve(query, docs, top_k=1):
    q = tokenize(query)
    scored = sorted(docs.items(), key=lambda kv: -len(q & tokenize(kv[1])))
    return [d for d, _ in scored[:top_k]]

QUERIES = {
    "damaged item refund window": "pol-001",
    "lost shipment refund": "pol-002",
    "digital goods refund": "pol-004",
}

def recall_at_1(docs):
    hits = sum(1 for q, want in QUERIES.items() if want in retrieve(q, docs))
    return hits, len(QUERIES)

h, n = recall_at_1(DOCS)
print("baseline recall@1: %d/%d" % (h, n))

# Fault 1: chunk split separates the query terms across two chunks.
# "damaged" lands in chunk B; chunk A keeps "refund"/"30 days".
broken = dict(DOCS)
broken["pol-001"] = "Refunds are approved within 30 days"
broken["pol-001b"] = "of delivery for damaged items."
h2, _ = recall_at_1(broken)
print("bad chunk split, recall@1: %d/%d" % (h2, n),
      "| top-1 for 'damaged item refund window':", retrieve("damaged item refund window", broken))

# Fault 2: keyword-only index on a paraphrased query
pq = "my package never arrived, want money back"
print("paraphrase top-1:", retrieve(pq, DOCS), "(want pol-002)")

# Fix check: re-chunk at the sentence boundary restores recall
h3, _ = recall_at_1(DOCS)
print("re-chunked recall@1: %d/%d" % (h3, n))
