import pplx_sdk, json, concurrent.futures as cf
groups = {
"t9_adoption": (["https://www.prosci.com/methodology/adkar",
 "https://www.prosci.com/methodology-overview",
 "https://www.prosci.com/blog/ai-in-change-management-early-findings",
 "https://www.prosci.com/blog/why-ai-transformation-fails",
 "https://www.kotterinc.com/methodology/8-steps/",
 "https://econjournals.com/index.php/irmm/article/view/19741",
 "https://www.paradigmpress.org/fms/article/download/938/812",
 "https://ai.wharton.upenn.edu/wp-content/uploads/2025/10/2025-Wharton-GBK-AI-Adoption-Report_Full-Report.pdf",
 "https://www.ey.com/en_gl/newsroom/2025/11/ey-survey-reveals-companies-are-missing-out-on-up-to-40-percent-of-ai-productivity-gains-due-to-gaps-in-talent-strategy",
 "https://sloanreview.mit.edu/article/turbocharging-organizational-learning-with-genai/",
 "https://erp.today/how-ai-is-forcing-erp-vendors-to-rethink-the-human-side-of-transformation/",
 "https://4439340.fs1.hubspotusercontent-na1.net/hubfs/4439340/Reports/ERP%20Report/2026-erp-report-panorama-consulting-group.pdf"],
 "Extract exact title, author(s)/organization, publisher, publication year, and 1-2 sentences on what it says about change management, adoption, training sequencing, or the constraint shifting from technical delivery to people learning in ERP/AI programs, including any figures. If year not stated say 'year not stated'."),
"t10_SI": (["https://upperedge.com/system-integrators/state-of-the-si-market-2025-the-race-to-lead-in-ai-enabled-consulting/",
 "https://www.altmansolon.com/thought-leadership/enterprise-ai-systems-integrators",
 "https://www.accenture.com/us-en/services/ai-data/ai-refinery",
 "https://newsroom.accenture.com/blogs/2026/accenture-launches-forward-deployed-engineering-program-with-sap",
 "https://www.deloitte.com/us/en/about/press-room/deloitte-adopts-sap-joule-for-consultants-solution.html",
 "https://www.morganlewis.com/blogs/sourcingatmorganlewis/2024/09/structuring-rights-to-ai-ml-outputs-insights-and-improvements-when-customer-data-is-foundational",
 "https://www.lathropgpm.com/insights/navigating-ai-ownership-in-commercial-and-ip-license-agreements-key-considerations-for-tech-providers-and-customers/",
 "https://www.idc.com/resource-center/blog/from-labor-arbitrage-to-platform-led-outcomes-how-agentic-ai-is-rewriting-the-it-services-playbook/",
 "https://www.mckinsey.com/capabilities/mckinsey-technology/our-insights/the-end-of-erp-as-we-know-it-five-ways-ai-is-disrupting-erp",
 "https://newsroom.ibm.com/2026-01-19-ibm-launches-enterprise-advantage-service-to-help-businesses-scale-agentic-ai"],
 "Extract exact title, author(s)/organization, publisher, publication year, and 1-2 sentences on what it says about the boundary between systems-integrator-owned and client-owned AI tooling/assets, IP ownership of AI assets, or delivery-model shifts. If year not stated say 'year not stated'."),
"extra": (["https://www.gartner.com/reviews/market/decision-intelligence-platforms",
 "https://www.standishgroup.com/products/project-resolution-benchmark",
 "https://www.globenewswire.com/news-release/2023/01/30/2597645/0/en/Gartner-Research-Predicts-Decision-Intelligence-to-be-Among-Most-Relevant-Technology-Trends-in-the-Next-Decade.html",
 "https://www.tmforum.org/resources/toolkit/ai-governance/",
 "https://www.forbes.com/sites/eriklarson/2022/05/10/gartners-decision-intelligence-trend-is-taking-off-what-took-so-long/",
 "https://inform.tmforum.org/research-and-analysis/reports/optimizing-governance-to-accelerate-genai-deployment",
 "https://www.tmforum.org/toolkits/digital-twin-for-decision-intelligence-dt4di-toolkit/"],
 "Extract exact title, author/organization, publisher, publication year, and 1-2 sentences on the key claim relevant to decision intelligence market definition, Gartner hype cycle or Magic Quadrant placement, project decision latency/failure rates, or AI governance. If year not stated say 'year not stated'."),
"venues": (["https://aisel.aisnet.org/misqe/policies.html",
 "https://hicss.hawaii.edu/authors/",
 "https://www.computer.org/digital-library/magazines/so/cfp-ieee-software",
 "https://cacm.acm.org/practice/communications-practice-section-welcomes-submissions/",
 "https://www.emeraldgrouppublishing.com/journal/jeim",
 "https://sloanreview.mit.edu/authors/",
 "https://www.isaca.org/resources/isaca-journal/submit-an-article",
 "https://www.tmforum.org/member-projects/collaboration",
 "https://www.tandfonline.com/journals/tjds20/about-this-journal",
 "https://authors.acm.org/magazines/cacm"],
 "Extract exact page title, publisher/organization, and 1-2 sentences on the venue's scope and how/what it accepts for submission (article types, review process). Note publication year only if stated."),
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
json.dump(out, open('/home/user/workspace/paper/research/f3.json','w'), indent=1)
for k,rs in out.items():
    print("="*20,k)
    for r in rs:
        print("---", r.get('url'))
        print((r.get('content') or r.get('error') or '')[:1300])
