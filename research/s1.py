import pplx_sdk, json, concurrent.futures as cf
queries = [
 "Gartner decision intelligence definition",
 "Cassie Kozyrkov decision intelligence Google",
 "decision intelligence peer reviewed journal",
 "Journal of Decision Systems decision intelligence",
 "TM Forum IG1247 digital twin decision intelligence",
 "TM Forum decision intelligence maturity model",
 "APQC Process Classification Framework version 7.4",
 "APQC PCF automotive retail banking",
 "SAP Activate methodology phases",
 "SAP Cloud ALM SAP Activate Signavio",
 "SAP Joule Business AI",
 "SAP Cloud ALM AI features 2025",
 "generative AI SAP S/4HANA implementation test scripts research",
]
def go(q):
    try:
        return q, [h.to_dict() for h in pplx_sdk.search.web(q)]
    except Exception as e:
        return q, [{"error":str(e)}]
with cf.ThreadPoolExecutor(13) as ex:
    res = dict(ex.map(go, queries))
json.dump(res, open('/home/user/workspace/paper/research/s1.json','w'), indent=1)
for q,hits in res.items():
    print("##", q)
    for h in hits[:8]:
        print(" -", h.get('title'), "|", h.get('url'), "|", h.get('date'))
