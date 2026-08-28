import pplx_sdk, json, concurrent.futures as cf
queries = [
 "NVIDIA sovereign AI",
 "EU AI Act data residency sovereign cloud 2025",
 "sovereign AI enterprise on-premise LLM deployment 2025",
 "client DMZ AI agent deployment enterprise architecture",
 "Standish Group CHAOS report project failure",
 "PMI knowledge transfer project knowledge loss consultants",
 "tacit knowledge loss ERP post implementation research",
 "IKEA Ingka digital transformation multi-year investment",
 "NIST AI Risk Management Framework",
 "ISO/IEC 42001 AI management system",
 "EU AI Act Article 14 human oversight",
 "human-in-the-loop AI enterprise finance peer reviewed",
 "Prosci ADKAR model change management",
 "Kotter 8 step change model",
 "ERP change management adoption training research 2025",
 "AI adoption bottleneck people learning not technology 2025 research",
 "systems integrator AI accelerators client owned AI assets consulting 2025",
 "Gartner hype cycle decision intelligence 2024",
]
def go(q):
    try:
        return q, [h.to_dict() for h in pplx_sdk.search.web(q)]
    except Exception as e:
        return q, [{"error":str(e)}]
with cf.ThreadPoolExecutor(18) as ex:
    res = dict(ex.map(go, queries))
json.dump(res, open('/home/user/workspace/paper/research/s2.json','w'), indent=1)
for q,hits in res.items():
    print("##", q)
    for h in hits[:8]:
        print(" -", h.get('title'), "|", h.get('url'), "|", h.get('date'))
