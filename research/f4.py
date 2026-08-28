import pplx_sdk, json, concurrent.futures as cf
groups = {
"acad_DI": (["https://www.journaldtai.com/index.php/jdtai/article/view/47",
 "https://journals.sagepub.com/doi/full/10.1177/22779752211017386",
 "https://ideas.repec.org/a/das/njaigs/v7y2024i01p304-319id361.html",
 "https://ideas.repec.org/a/for/ijafaa/y2024i74p42-44.html",
 "https://www.gartner.com/en/articles/hype-cycle-for-artificial-intelligence",
 "https://www.gartner.com/en/newsroom/press-releases/2025-08-05-gartner-hype-cycle-identifies-top-ai-innovations-in-2025"],
 "Extract exact title, author(s), journal/publisher, publication year, and 1-2 sentences on how it defines or positions decision intelligence (and, for Gartner pages, any named hype cycle position/innovation). If year not stated say 'year not stated'."),
"tmf_apqc": (["https://www.tmforum.org/resources/introductory-guide-whitepaper/dt4di-from-strategy-to-implementation-v3-0-0-ig1307/",
 "https://www.tmforum.org/resources/introductory-guide/dt4di-top-use-cases-v8-0-0-ig1310c/",
 "https://www.tmforum.org/resources/guidebook/gb1079-dt4di-top-use-cases-v1-0-0/",
 "https://www.signavio.com/reference-models/apqc-framework/",
 "https://help.sap.com/docs/signavio-process-manager/user-guide/import-apqc-framework",
 "https://www.signavio.com/news/press-release-apqc-signavio-pcf/",
 "https://userapps.support.sap.com/sap/support/knowledge/en/3431337"],
 "Extract exact title, document ID/version if any, publisher, publication year/date, and 1-2 sentences on content: for TM Forum, what the guide specifies and named use cases/case studies; for Signavio/SAP pages, how the APQC PCF is provided or used inside the tool. If year not stated say 'year not stated'."),
"sap_ai_sov": (["https://www.sap.com/products/technology-platform/cloud-alm-requirement-generation.html",
 "https://community.sap.com/t5/technology-blog-posts-by-sap/ai-goes-calm-ai-assisted-requirement-generation/ba-p/14294426",
 "https://www.sap.com/products/security-and-sovereignty.html",
 "https://news.sap.com/2025/11/sap-eu-ai-cloud-unified-vision-europe-sovereign-ai-cloud-future/",
 "https://www.sap.com/products/artificial-intelligence/ai-ethics.html",
 "https://www-api.ibm.com/adobe/assets/urn:aaid:aem:c8af1164-1b81-49f0-bf9d-bb4dc8da1e19/original/as/ibm-guide-to-architecting-secure-enterprise-ai-agents-with-mcp-techxchange-2025.pdf"],
 "Extract exact title, author/organization, publisher, publication year, and 1-2 sentences on the key claim: AI-assisted requirement/spec generation in SAP Cloud ALM, sovereign cloud / data residency / in-boundary AI hosting, human oversight in AI ethics, or secure enterprise agent architecture boundaries. If year not stated say 'year not stated'."),
"ikea": (["https://www.inter.ikea.com/en/newsroom/inter-ikea-group-reports-resilient-fy25-results-amid-global-challenges",
 "https://www.ingka.com/annual-summary-and-sustainability-report/",
 "https://www.ingka.com/newsroom/ingka-ab-takes-next-steps-to-strengthen-the-business-for-the-future/",
 "https://www.inter.ikea.com/-/media/interikea/igi/financial-reports/fy25-financial-reports/inter-ikea-holding-bv-annual-report-fy25-final.pdf?rev=10c81cc96c064789932e13ebf6229492&sc_lang=en"],
 "Extract exact title, organization, publisher, publication year, and 1-2 sentences with any stated figures on multi-year business/digital transformation, technology or transformation investment, and organisational restructuring at IKEA/Ingka/Inter IKEA. If year not stated say 'year not stated'."),
}
def go(item):
    k,(urls,prompt) = item
    try:
        res = [r.to_dict() for r in pplx_sdk.content.fetch(urls, prompt=prompt)]
    except Exception as e:
        res = [{"error":str(e)}]
    return k,res
with cf.ThreadPoolExecutor(4) as ex:
    out = dict(ex.map(go, groups.items()))
json.dump(out, open('/home/user/workspace/paper/research/f4.json','w'), indent=1)
for k,rs in out.items():
    print("="*20,k)
    for r in rs:
        print("---", r.get('url'))
        print((r.get('content') or r.get('error') or '')[:1200])
