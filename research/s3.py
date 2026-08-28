import pplx_sdk, json, concurrent.futures as cf
queries = [
 "decision intelligence MIT Sloan Management Review",
 "MIS Quarterly Executive decision making analytics article",
 "decision intelligence systematic literature review academic",
 "IG1247 TM Forum",
 "TM Forum digital twin decision intelligence catalyst case study operator",
 "APQC process classification framework overview definition seven categories",
 "APQC PCF used as process taxonomy transformation",
 "SAP Activate roadmap viewer discover prepare explore realize deploy run",
 "SAP Solution Manager vs Cloud ALM SAP recommendation",
 "SAP Signavio process transformation SAP page",
 "Joule agents SAP release 2026",
 "AI cutover hypercare SAP research paper",
 "IKEA business transformation Ingka annual report digital investment FY24",
 "IKEA IT transformation SAP program",
 "Standish Group official CHAOS 2020 report",
 "knowledge retention consultants offboarding research paper IT outsourcing",
 "training first sequencing AI ERP adoption 2026",
 "Prosci research change management effectiveness AI 2025",
 "ISACA journal AI governance article",
 "MIS Quarterly Executive submission guidelines",
]
def go(q):
    try:
        return q, [h.to_dict() for h in pplx_sdk.search.web(q)]
    except Exception as e:
        return q, [{"error":str(e)}]
with cf.ThreadPoolExecutor(20) as ex:
    res = dict(ex.map(go, queries))
json.dump(res, open('/home/user/workspace/paper/research/s3.json','w'), indent=1)
for q,hits in res.items():
    print("##", q)
    for h in hits[:8]:
        print(" -", h.get('title'), "|", h.get('url'), "|", h.get('date'))
