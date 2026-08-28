import pplx_sdk, json, concurrent.futures as cf, textwrap
groups = {
"t1_DI": (["https://www.gartner.com/en/information-technology/glossary/decision-intelligence",
 "https://www.gartner.com/en/research/methodologies/gartner-hype-cycle",
 "https://www.gartner.com/en/newsroom/press-releases/2024-08-21-gartner-2024-hype-cycle-for-emerging-technologies-highlights-developer-productivity-total-experience-ai-and-security",
 "https://medium.com/data-science/introduction-to-decision-intelligence-5d147ddab767",
 "https://towardsdatascience.com/decision-intelligence-a-preliminary-summary-2098a9b79b46/",
 "https://www.wired.com/story/google-chief-decision-scientist-cassie-kozyrkov/",
 "https://aisel.aisnet.org/misqe/vol19/iss2/5/",
 "https://sloanreview.mit.edu/article/intelligent-choices-reshape-decision-making-and-productivity/",
 "https://sloanreview.mit.edu/article/the-great-power-shift-how-intelligent-choice-architectures-rewrite-decision-rights/",
 "https://sloanreview.mit.edu/article/genai-tools-and-decision-making-beware-a-new-control-trap/",
 "https://www.tandfonline.com/journals/tjds20/about-this-journal",
 "https://journals.sagepub.com/doi/10.1177/18724981251316079"],
 "Extract exact page/article title, author(s), publisher or journal, publication year, and 1-2 sentences on how it defines or treats decision intelligence / decision-making with analytics and AI, including any boundary vs BI or data science. If the year is not stated say 'year not stated'."),
"t2_TMF": (["https://www.tmforum.org/digital-twin-for-decision-intelligence-dt4di/",
 "https://www.tmforum.org/toolkits/digital-twin-for-decision-intelligence-dt4di-toolkit/",
 "https://www.tmforum.org/resources/introductory-guide/ig1310-digital-twin-for-decision-intelligence-dt4di-aiops-ontology-v3-3-0/",
 "https://www.tmforum.org/resources/introductory-guide/ig1310b-dt4di-maturity-model-v1-0-0/",
 "https://www.tmforum.org/resources/introductory-guide/digital-twin-for-decision-intelligence-dt4di-use-case-repository-v3-0-0-ig1310c/",
 "https://www.tmforum.org/resources/how-to-guide/ig1247-data-governance-tools-panorama-v2-0-0/",
 "https://inform.tmforum.org/features-and-opinion/how-digital-twins-and-ai-are-driving-new-decision-intelligence",
 "https://inform.tmforum.org/research-and-analysis/proofs-of-concept/using-digital-twins-and-agentic-ai-to-enable-level-4-autonomous-network-operations",
 "https://www.tmforum.org/catalysts/projects/C25.0.775/bind-bridging-intelligence-networks-and-digital-twin",
 "https://www.tmforum.org/resources/best-practice/gb1003a-ai-maturity-model-v3-0-0/"],
 "Extract exact title, document/asset ID if any, publisher, version and publication year/date, and 1-2 sentences on content: what the document specifies (architecture, maturity model, use cases, ontology) and any named operators/case studies. If year not stated say 'year not stated'."),
"t3_APQC": (["https://www.apqc.org/process-frameworks",
 "https://www.apqc.org/process-frameworks/pcf-faqs",
 "https://www.apqc.org/process-frameworks/industry-specific-process-frameworks",
 "https://www.apqc.org/resource-library/resource-listing/introduction-apqcs-process-classification-framework-pcf",
 "https://www.apqc.org/resource-library/resource-collection/pcf-version-74-process-definitions-and-key-measures-collection",
 "https://www.apqc.org/resource-library/resource-listing/apqc-process-classification-framework-pcf-automotive-oem-pdf-0",
 "https://www.apqc.org/resource-library/resource-listing/apqc-process-classification-framework-pcf-retail-pdf-version-721",
 "https://www.apqc.org/resource-library/resource-listing/apqc-process-classification-framework-pcf-banking-pcf-pdf-1",
 "https://www.apqc.org/resource-library/resource-listing/analyzing-processes-how-use-process-classification-framework-pcfr",
 "https://www.apqc.org/sites/default/files/files/PCF%20Collateral/Intro%20to%20PCF%20-%20FINAL.pdf"],
 "Extract exact title, publisher, current PCF version number stated, publication/update year, and 1-2 sentences on what the page says about the PCF's structure (levels, numbering/hierarchy), cross-industry vs industry variants, and its use as a common process taxonomy. If year not stated say 'year not stated'."),
"t4_SAP_Activate": (["https://www.sap.com/products/erp/activate-methodology.html",
 "https://learning.sap.com/courses/exploring-sap-cloud-erp/utilizing-the-sap-activate-implementation-methodology-and-sap-cloud-alm_a68867ac-cb61-44de-b358-5114b6ebd68e",
 "https://learning.sap.com/courses/discovering-sap-activate-implementation-tools-and-methodology/understanding-the-sap-integrated-toolchain_ce528715-8830-4aff-94b1-f31ab143421c",
 "https://support.sap.com/en/alm/sap-cloud-alm.html",
 "https://support.sap.com/en/alm/sap-cloud-alm/transition-to-sap-cloud-alm.html",
 "https://help.sap.com/docs/cloud-alm",
 "https://www.sap.com/products/business-transformation-management/signavio-process-manager.html",
 "https://learning.sap.com/courses/sap-signavio-process-management/synchronizing-sap-signavio-with-sap-cloud-alm-3",
 "https://www.signavio.com/products/process-transformation-suite/"],
 "Extract exact title, publisher (SAP entity), publication/update year if shown, and 1-2 sentences on: SAP Activate phases named, and how SAP positions SAP Cloud ALM, SAP Signavio, and SAP Solution Manager relative to the methodology. If year not stated say 'year not stated'."),
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
json.dump(out, open('/home/user/workspace/paper/research/f1.json','w'), indent=1)
for k,rs in out.items():
    print("="*20,k)
    for r in rs:
        print("---", r.get('url'))
        print((r.get('content') or r.get('error') or '')[:1200])
