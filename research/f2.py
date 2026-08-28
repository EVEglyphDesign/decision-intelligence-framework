import pplx_sdk, json, concurrent.futures as cf
groups = {
"t5_AI_SAP": (["https://www.sap.com/products/artificial-intelligence.html",
 "https://www.sap.com/products/artificial-intelligence/ai-agents.html",
 "https://news.sap.com/2025/02/joule-sap-uniquely-delivers-ai-agents/",
 "https://news.sap.com/2026/01/sap-business-ai-release-highlights-q4-2025/",
 "https://news.sap.com/2026/04/sap-business-ai-release-highlights-q1-2026/",
 "https://news.sap.com/2026/02/process-conversation-joule-sap-signavio-solutions-generally-available/",
 "https://community.sap.com/t5/technology-blog-posts-by-sap/ai-in-sap-cloud-alm-takes-monitoring-to-another-level/ba-p/14152014",
 "https://help.sap.com/docs/joule/serviceguide/what-is-joule",
 "https://eajournals.org/ejcsit/vol13-issue32-2025/ai-powered-hyperautomation-in-sap-s-4hana-migration-transforming-erp-transitions/",
 "https://ijcesen.com/index.php/ijcesen/article/view/4016",
 "http://www.ijlemr.com/papers/volume9-issue10/6-IJLEMR-89005.pdf",
 "https://www.ijcttjournal.org/archives/ijctt-v72i8p131"],
 "Extract exact title, author(s), publisher/journal, publication year, and 1-2 sentences on what it claims about AI/generative AI in SAP programs (Joule, Cloud ALM, functional specs, test scripts, cutover, hypercare). If year not stated say 'year not stated'."),
"t6_sovereign": (["https://resources.nvidia.com/en-us-telco-ai-factories-mc/en-us-telco-ai-factories/what-is-sovereign-ai",
 "https://blogs.nvidia.com/blog/sovereign-ai-agents-factories/",
 "https://www.nvidia.com/en-us/lp/industries/global-public-sector/sovereign-ai-technical-overview/",
 "https://www.reuters.com/business/media-telecom/nvidias-pitch-sovereign-ai-resonates-with-eu-leaders-2025-06-16/",
 "https://developer.nvidia.com/blog/how-to-govern-autonomous-agents-in-enterprise-ai-factories/",
 "https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng",
 "https://www.europarl.europa.eu/RegData/etudes/BRIE/2025/779251/EPRS_BRI(2025)779251_EN.pdf",
 "https://arxiv.org/html/2509.18101v1",
 "https://www.innoq.com/en/articles/2025/09/on-premise-llms-strategischer-hebel/"],
 "Extract exact title, author/organization, publisher, publication year, and 1-2 sentences on the sovereign AI / data residency / on-premise or in-boundary model hosting claim made. If year not stated say 'year not stated'."),
"t7_memory": (["https://www.standishgroup.com/",
 "https://www.pmi.org/learning/library/knowledge-transfer-project-management-offices-1468",
 "https://www.pmi.org/-/media/pmi/documents/public/pdf/learning/thought-leadership/pulse/capture-value-knowledge-transfer.pdf",
 "https://www.sciencedirect.com/science/article/abs/pii/S0268401208001606",
 "https://dl.acm.org/doi/abs/10.4018/irmj.2005040101",
 "https://www.diva-portal.org/smash/get/diva2:829255/FULLTEXT01.pdf",
 "http://www.diva-portal.org/smash/get/diva2:4611/FULLTEXT01.pdf",
 "https://www.ingka.com/static/ingkagroup_annualsummaryandsustainabilityreport_fy24.pdf",
 "https://www.ingka.com/newsroom/creating-a-simpler-more-resilient-ikea-for-the-future/",
 "https://www.ingka.com/newsroom/ingka-group-takes-next-steps-to-become-even-more-resilient-for-the-future/",
 "https://tech.ingka.com/newsfeed",
 "https://www.cs.vu.nl/~x/the_rise_and_fall_of_the_chaos_report_figures.pdf"],
 "Extract exact title, author(s)/organization, publisher, publication year, and 1-2 sentences on what it documents about project outcomes/failure rates, knowledge transfer or knowledge loss, or (for IKEA/Ingka pages) about digital/business transformation, technology investment, restructuring and any figures stated. If year not stated say 'year not stated'."),
"t8_HITL": (["https://www.nist.gov/itl/ai-risk-management-framework",
 "https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf",
 "https://www.iso.org/standard/42001",
 "https://www.iso.org/artificial-intelligence/ai-management-systems",
 "https://artificialintelligenceact.eu/article/14/",
 "https://www.tandfonline.com/doi/full/10.1080/17579961.2023.2245683",
 "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5147196",
 "https://www.mdpi.com/1099-4300/28/4/377",
 "http://www.austlii.edu.au/cgi-bin/viewdoc/au/journals/SydLawRw/2021/2.html",
 "https://ideas.repec.org/a/inm/ormnsc/v72y2026i1p242-264.html"],
 "Extract exact title, author(s), publisher/journal/standards body, publication year, and 1-2 sentences on what it requires or finds regarding human oversight / human-in-the-loop in AI systems. If year not stated say 'year not stated'."),
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
json.dump(out, open('/home/user/workspace/paper/research/f2.json','w'), indent=1)
for k,rs in out.items():
    print("="*20,k)
    for r in rs:
        print("---", r.get('url'))
        print((r.get('content') or r.get('error') or '')[:1300])
