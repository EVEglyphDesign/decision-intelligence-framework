import pplx_sdk, json, concurrent.futures as cf
queries = [
 "Gartner press release decision intelligence emerging technologies 2022",
 "Gartner Magic Quadrant decision intelligence platforms gartner.com document",
 "Standish Group CHAOS report decision latency",
 "who owns AI accelerators client consulting contract intellectual property transformation",
 "Accenture SAP AI accelerators refinery client",
 "Deloitte SAP AI implementation accelerator press release",
 "IDC systems integrator generative AI services client ownership",
 "ERP implementation AI shifting bottleneck to change management 2026",
 "MIT Sloan research AI adoption divide organizational learning 2025",
 "TM Forum AI governance human oversight guide",
]
def go(q):
    try:
        return q, [h.to_dict() for h in pplx_sdk.search.web(q)]
    except Exception as e:
        return q, [{"error":str(e)}]
with cf.ThreadPoolExecutor(10) as ex:
    res = dict(ex.map(go, queries))
json.dump(res, open('/home/user/workspace/paper/research/s5.json','w'), indent=1)
for q,hits in res.items():
    print("##", q)
    for h in hits[:7]:
        print(" -", h.get('title'), "|", h.get('url'), "|", h.get('date'))
