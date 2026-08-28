import pplx_sdk, json, concurrent.futures as cf
queries = [
 "Journal of Business Analytics decision intelligence article",
 "decision intelligence definition academic paper 2024 framework research",
 "TM Forum IG1307 DT4DI from strategy to implementation resource",
 "SAP Signavio APQC process classification framework content",
 "SAP Cloud ALM AI generated requirements fit-to-standard help documentation",
 "SAP Sovereign Cloud data residency",
 "IBM architecting secure enterprise AI agents MCP guide",
 "Inter IKEA annual report FY25 transformation technology",
 "SAP Business AI trust data privacy AI ethics policy page",
 "Gartner hype cycle for artificial intelligence 2025 decision intelligence placement",
]
def go(q):
    try:
        return q, [h.to_dict() for h in pplx_sdk.search.web(q)]
    except Exception as e:
        return q, [{"error":str(e)}]
with cf.ThreadPoolExecutor(10) as ex:
    res = dict(ex.map(go, queries))
json.dump(res, open('/home/user/workspace/paper/research/s6.json','w'), indent=1)
for q,hits in res.items():
    print("##", q)
    for h in hits[:6]:
        print(" -", h.get('title'), "|", h.get('url'), "|", h.get('date'))
