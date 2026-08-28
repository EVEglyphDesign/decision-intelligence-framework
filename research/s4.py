import pplx_sdk, json, concurrent.futures as cf
queries = [
 "Kozyrkov introduction to decision intelligence Towards Data Science",
 "Google Cloud decision intelligence Kozyrkov blog",
 "APQC PCF banking version",
 "SAP Cloud ALM product page sap.com",
 "Ingka Group digital transformation technology investment newsroom",
 "IKEA annual report technology digital transformation billion euro",
 "client owned AI models consulting clients bring your own AI transformation",
 "HICSS submission call for papers",
 "IEEE Software author information submission",
 "Communications of the ACM submission practice",
 "Journal of Enterprise Information Management author guidelines Emerald",
 "MIT Sloan Management Review submit article guidelines",
 "ISACA Journal author guidelines call for articles",
 "TM Forum contribute member collaboration program",
 "EU AI Act high risk obligations regulation text official journal",
 "SAP Business AI page sap.com artificial intelligence",
]
def go(q):
    try:
        return q, [h.to_dict() for h in pplx_sdk.search.web(q)]
    except Exception as e:
        return q, [{"error":str(e)}]
with cf.ThreadPoolExecutor(16) as ex:
    res = dict(ex.map(go, queries))
json.dump(res, open('/home/user/workspace/paper/research/s4.json','w'), indent=1)
for q,hits in res.items():
    print("##", q)
    for h in hits[:7]:
        print(" -", h.get('title'), "|", h.get('url'), "|", h.get('date'))
