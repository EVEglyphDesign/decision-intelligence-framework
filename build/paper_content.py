"""Content module for the peer-review paper.

Isolated from the builder so it can be edited without touching layout code.
Every citation URL below appears at least once in
/home/user/workspace/paper/research/literature_pass.md.
"""

from __future__ import annotations

# --- Paper metadata ------------------------------------------------------

TITLE = "A Decision Intelligence Framework for Enterprise Transformation Programs"
SUBTITLE = (
    "Sovereign Context Reasoning, APQC-Spined Traceability, "
    "and Adoption-First Sequencing in the SAP Program Context"
)
AUTHOR = "EVEglyphDesign — practitioner author"
VERSION = "v1.1 — invited peer review draft (capital-asset framing)"
ABSTRACT = (
    "Decision intelligence is now defined as a superset discipline in which "
    "business intelligence is one optional input, yet enterprise "
    "transformation programs continue to treat it either as a synonym for "
    "analytics or as an unbounded aspiration. This paper proposes a "
    "practitioner framework for embedding decision intelligence inside the "
    "SAP program context along three load-bearing choices: an AI "
    "context-reasoning surface hosted wholly inside the client's DMZ and "
    "operated as a durable enterprise capital asset; a program-wide numbering "
    "spine anchored on the APQC Process Classification Framework (v7.4) that "
    "threads blueprint, technical design, technical object, test plan, "
    "dataset, and role and authorisation records through the SAP Activate "
    "phase model; and an adoption-first sequencing that moves learning and "
    "role design forward in the plan on the evidence that people, not "
    "technology, are now the binding constraint on transformation outcomes. "
    "The framework is positioned as additive to the existing SAP toolchain "
    "(Cloud ALM, Signavio, Solution Manager, Joule) and to the emerging "
    "TM Forum DT4DI stack (IG1307, IG1310, IG1310A, IG1310B, IG1310C), and "
    "it makes an explicit break with the systems-integrator-owned platform "
    "pattern by naming the sovereign context-reasoning repository as a "
    "client-held residual. The paper closes with an invitation to peer "
    "review, an evidence register, and a list of open questions the author "
    "does not yet have the data to close."
)

KEYWORDS = [
    "decision intelligence",
    "enterprise transformation",
    "SAP Activate",
    "APQC PCF",
    "sovereign AI",
    "human-authorised decision artifacts",
    "program memory",
    "adoption sequencing",
    "digital twin",
    "TM Forum DT4DI",
]


# --- Helper: markdown-like link tag for reportlab -----------------------

def L(anchor: str, url: str) -> str:
    """Return a reportlab <link> tag with the canon orange underline."""
    return f'<link href="{url}" color="#e87722"><u>{anchor}</u></link>'


# --- Sections -----------------------------------------------------------
# Each section is a list of ("kind", content) tuples:
#   ("h2", text)         -> section heading
#   ("h3", text)         -> subsection heading
#   ("p",  text)         -> paragraph (may contain L() links)
#   ("bul", [text, ...]) -> bulleted list
#   ("tbl", (headers, rows)) -> table
#   ("space", n_points)  -> vertical space

SECTIONS: list[tuple[str, str, list]] = []


def add(kind: str, content):
    SECTIONS.append((kind, "", content) if isinstance(content, (list, tuple, dict)) else (kind, content, None))


# 1. Introduction ---------------------------------------------------------

add("h2", "1. Introduction")

add(
    "p",
    "The single largest information-technology capital asset most enterprises "
    "own is not the package they bought. It is the accumulated business "
    "context they built on top of it — the industry-specific reasoning, the "
    "structured and unstructured decision history, the configuration and "
    "customisation choices, and the tacit institutional judgement that has "
    "been layered onto ERP, CRM, and adjacent platforms for decades. That "
    "asset is almost always larger than the licences that carry it, and it is "
    "almost never treated on the balance sheet, in the transformation plan, "
    "or in the vendor contract as the asset it is. This paper is a framework "
    "for treating it that way — for making the client's own reasoning the "
    "asset that a transformation program compounds, rather than the asset it "
    "quietly leaks to whoever holds the delivery platform.",
)

add(
    "p",
    "The pressure to do this now is structural. Enterprise transformation "
    "programs are being asked to absorb generative and agentic AI at a pace "
    "that is not compatible with how enterprise standards evolve. Standards "
    "bodies operate by consensus at intervals of years; the platforms "
    "currently reshaping delivery methodology reprice, rebrand, and re-scope "
    "their offers at intervals of months. Programs must adopt AI before an "
    "enterprise-grade standard for using it has crystallised. That gap is "
    "where fear, over-buying, and integrator lock-in enter transformation "
    "portfolios — and it is also where the client's capital asset is most "
    "exposed. The framework in this paper is a way to close the gap on the "
    "client's side of the line rather than the vendor's.",
)

add(
    "p",
    "Decision intelligence (DI) is one of the constructs that has arrived to "
    "fill the gap. Gartner defines DI as \"a practical discipline that advances "
    "decision making by explicitly understanding and engineering how decisions "
    "are made and how outcomes are evaluated, managed and improved via "
    "feedback\" (" + L("Gartner IT Glossary", "https://www.gartner.com/en/information-technology/glossary/decision-intelligence") + "), "
    "and the accompanying market definition treats business intelligence as "
    "only one optional input among decision modelling, orchestration, "
    "evaluation, governance, and audit (" + L("Gartner Peer Insights", "https://www.gartner.com/reviews/market/decision-intelligence-platforms") + "). "
    "Cassie Kozyrkov's founding practitioner writing frames DI as a discipline "
    "concerned with \"all aspects of selecting between options\" and fuses "
    "applied data science, social science, and managerial science (" + L("Kozyrkov, 2019", "https://medium.com/data-science/introduction-to-decision-intelligence-5d147ddab767") + "). "
    "Peer-reviewed theory is thinner: the strongest published treatment is a "
    "four-element Decision Context / Framework Proficiency / Intelligence "
    "Access / Decision Proficiency framework (" + L("Moser, Rengarajan and Narayanamurthy, 2021", "https://journals.sagepub.com/doi/full/10.1177/22779752211017386") + "), "
    "with the closest management-side construct being Schrage and Kiron's "
    "\"intelligent choice architectures\" (" + L("MIT Sloan Management Review", "https://sloanreview.mit.edu/article/intelligent-choices-reshape-decision-making-and-productivity/") + ").",
)

add(
    "p",
    "This paper proposes a practitioner framework for using decision "
    "intelligence inside the SAP program context, and stakes three load-bearing "
    "claims — each of which is a claim about the client's capital asset, not "
    "a claim about methodology. First, the AI context-reasoning surface for a "
    "transformation program is a client-side capital asset and must be hosted "
    "wholly inside the client's DMZ; the systems-integrator-owned pattern "
    "currently consolidating in the market moves that asset outside the "
    "client's balance sheet and is not neutral. Second, the SAP program "
    "already has a viable numbering spine in the APQC Process Classification "
    "Framework and its five-digit stable IDs, and using that spine to thread "
    "blueprint, technical design, technical object, test plan, dataset, and "
    "role and authorisation records converts point-in-time deliverables into a "
    "traceable program record that survives the delivery team's departure. "
    "Third, the constraint on transformation success has moved from technical "
    "delivery to human adoption, and the plan must be resequenced so that the "
    "authorised human decisions — the ones that make the reasoning surface "
    "defensible as an asset — are rehearsed early rather than at cutover. The "
    "framework is additive: it does not displace SAP Cloud ALM, SAP Signavio, "
    "SAP Solution Manager, Joule, Jira, or Azure DevOps. It orchestrates work "
    "around them and lands the residual with the client.",
)

add(
    "p",
    "The paper is written as an invited-peer-review draft. Its argument is a "
    "practitioner argument grounded in program-delivery experience and "
    "canonical primary sources; the sections at the end name the places where "
    "the argument has thin literature behind it and invite specific "
    "corrections.",
)


# 2. Background ----------------------------------------------------------

add("h2", "2. Background — what decision intelligence is and is not")

add("h3", "2.1 A superset discipline, not a synonym for business intelligence")

add(
    "p",
    "Gartner's market definition of a decision intelligence platform requires "
    "collaborative decision modelling, execution, and monitoring; BI, machine "
    "learning, optimisation, graph, simulation, and AI agents are named as "
    "optional composable techniques (" + L("Gartner Peer Insights", "https://www.gartner.com/reviews/market/decision-intelligence-platforms") + "). "
    "DI is therefore properly read as the discipline of engineering the "
    "decision itself — inputs, options, weights, feedback, and accountability "
    "— and BI as one instrument that DI orchestrates. That distinction is not "
    "cosmetic. It changes what a transformation program is trying to buy.",
)

add(
    "p",
    "The current placement of \"decision intelligence\" on Gartner's "
    "artificial-intelligence hype cycle is not confirmable from Gartner's own "
    "2025 pages, which name AI agents, AI-ready data, multimodal AI, AI TRiSM, "
    "ModelOps, and AI-native software engineering but do not mention decision "
    "intelligence (" + L("Gartner, 2025", "https://www.gartner.com/en/articles/hype-cycle-for-artificial-intelligence") + "; " + L("Gartner press release, 2025", "https://www.gartner.com/en/newsroom/press-releases/2025-08-05-gartner-hype-cycle-identifies-top-ai-innovations-in-2025") + "). "
    "The paper does not depend on any hype-cycle position; it depends on the "
    "definitional and structural claims above.",
)

add("h3", "2.2 The TM Forum DT4DI stack")

add(
    "p",
    "The most developed industry framing of decision intelligence is TM "
    "Forum's Digital Twin for Decision Intelligence (DT4DI) programme. Its "
    "published stack is IG1307 strategy-to-implementation guide "
    "(" + L("v3.0.0, 2025", "https://www.tmforum.org/resources/introductory-guide-whitepaper/dt4di-from-strategy-to-implementation-v3-0-0-ig1307/") + "), "
    "IG1310 DT4DI and AIOps ontology (" + L("v3.3.0, 2023", "https://www.tmforum.org/resources/introductory-guide/ig1310-digital-twin-for-decision-intelligence-dt4di-aiops-ontology-v3-3-0/") + "), "
    "IG1310A reference architecture (v2.2.0, 2023), IG1310B maturity model "
    "with five levels across five weighted dimensions "
    "(" + L("v1.0.0, 2023", "https://www.tmforum.org/resources/introductory-guide/ig1310b-dt4di-maturity-model-v1-0-0/") + "), "
    "and the IG1310C use-case repository "
    "(" + L("v3.0.0, 2024", "https://www.tmforum.org/resources/introductory-guide/digital-twin-for-decision-intelligence-dt4di-use-case-repository-v3-0-0-ig1310c/") + " and "
    "" + L("v8.0.0, 2025", "https://www.tmforum.org/resources/introductory-guide/dt4di-top-use-cases-v8-0-0-ig1310c/") + "). "
    "DT4DI's own thesis is explicit: DI expands and complements traditional BI "
    "for analysis, processes, and decision-making. The paper adopts DT4DI as "
    "credible vocabulary for governed decision twins and staged capability "
    "development, and reserves the client-owned DMZ deployment and owned "
    "residual as the governing architecture.",
)

add(
    "p",
    "Two limitations of DT4DI as a direct fit for enterprise SAP programs "
    "must be named. First, DT4DI is telco-scoped: its use-case repository "
    "and reference architecture are built around communications service "
    "providers. Second, no named operator case study is published in TM "
    "Forum's own DT4DI assets at time of writing; the nearest proof point is "
    "the BIND Catalyst combining digital twins, agentic AI, and A2A for "
    "level-4 autonomous network operations "
    "(" + L("TM Forum Inform", "https://inform.tmforum.org/research-and-analysis/proofs-of-concept/using-digital-twins-and-agentic-ai-to-enable-level-4-autonomous-network-operations") + "). "
    "The framework proposed here is compatible with DT4DI's vocabulary but is "
    "designed for enterprise transformation programs and does not inherit "
    "DT4DI's telco scope.",
)


# 3. The framework -------------------------------------------------------

add("h2", "3. The framework — three load-bearing choices")

add("h3", "3.1 Sovereign context reasoning inside the client's DMZ")

add(
    "p",
    "A transformation program generates high-value context: workshop "
    "transcripts, requirements clarifications, fit-to-standard decisions, "
    "cutover choices, and hypercare tickets. Once processed by an AI context-"
    "reasoning surface, that context becomes a capital asset. The framework's "
    "first choice is that the surface holding it must run inside the client's "
    "DMZ, and the residual must transfer to the client at engagement end.",
)

add(
    "p",
    "The choice is not vendor-neutral. NVIDIA's canonical treatment of "
    "sovereign AI is national — the capability of a nation or organisation to "
    "develop and control AI within its own borders using its own "
    "infrastructure, data, workforce, and networks "
    "(" + L("NVIDIA", "https://resources.nvidia.com/en-us-telco-ai-factories-mc/en-us-telco-ai-factories/what-is-sovereign-ai") + "), "
    "while the EU AI Act itself imposes no residency mandate but does apply "
    "extraterritorially "
    "(" + L("Reg. (EU) 2024/1689", "https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng") + "); "
    "residency pressure comes instead from adjacent EU regulation "
    "(" + L("Cloud and AI Development Act briefing, 2025", "https://www.europarl.europa.eu/RegData/etudes/BRIE/2025/779251/EPRS_BRI(2025)779251_EN.pdf") + "). "
    "On the economics, on-premises inference for enterprise-scale workloads "
    "breaks even against cloud APIs at approximately fifty million tokens per "
    "month or when residency is mandated "
    "(" + L("Pan and Wang, 2025", "https://arxiv.org/html/2509.18101v1") + "), "
    "which is well below the token volume of a live transformation program's "
    "context-reasoning workload.",
)

add(
    "p",
    "The market is already converging on the client-owned pattern. IBM's "
    "MCP-based reference architecture places the reasoning agents inside "
    "customer-controlled infrastructure "
    "(" + L("IBM, 2025", "https://www-api.ibm.com/adobe/assets/urn:aaid:aem:c8af1164-1b81-49f0-bf9d-bb4dc8da1e19/original/as/ibm-guide-to-architecting-secure-enterprise-ai-agents-with-mcp-techxchange-2025.pdf") + "), "
    "and NVIDIA's Secure Agent Workspace argues for governed autonomous "
    "agents inside enterprise AI factories "
    "(" + L("NVIDIA", "https://developer.nvidia.com/blog/how-to-govern-autonomous-agents-in-enterprise-ai-factories/") + "). "
    "The counter-pattern is IDC's Service Provider Agentic AI Platform — an "
    "SI-owned platform that persists after engagement end and requires "
    "explicit IP and data terms "
    "(" + L("IDC", "https://www.idc.com/resource-center/blog/from-labor-arbitrage-to-platform-led-outcomes-how-agentic-ai-is-rewriting-the-it-services-playbook/") + "). "
    "Legal commentary is beginning to specify the boundary, but the enterprise "
    "contracting language has not caught up "
    "(" + L("Morgan Lewis, 2024", "https://www.morganlewis.com/blogs/sourcingatmorganlewis/2024/09/structuring-rights-to-ai-ml-outputs-insights-and-improvements-when-customer-data-is-foundational") + "). "
    "The framework recommends that clients treat the sovereign context-"
    "reasoning surface as a program deliverable in its own right, on the same "
    "footing as the ERP configuration itself.",
)

add("h3", "3.2 APQC-spined traceability threading the SAP Activate phase model")

add(
    "p",
    "The framework's second choice is a program-wide numbering spine anchored "
    "on the APQC Process Classification Framework (PCF). The cross-industry "
    "PCF is at " + L("version 7.4", "https://www.apqc.org/process-frameworks/pcf-faqs") + " "
    "and decomposes into 13 Categories through Process Group, Process, "
    "Activity, and Task, with each element carrying both a hierarchy number "
    "and a unique five-digit ID that persists across name and definition "
    "changes "
    "(" + L("APQC, 2018", "https://www.apqc.org/sites/default/files/files/PCF%20Collateral/Intro%20to%20PCF%20-%20FINAL.pdf") + "). "
    "That stable-ID property is the one that makes the PCF viable as a program "
    "spine rather than just a taxonomy. Industry variants — Automotive (OEM) "
    "7.2.2, Retail 7.2.1, Banking 7.2.2 — retain the core structure and "
    "reference numbers of the cross-industry PCF so that spine choices survive "
    "sector-specific extension "
    "(" + L("APQC industry PCFs", "https://www.apqc.org/process-frameworks/industry-specific-process-frameworks") + "). "
    "The PCF is already importable as a folder tree of linked value chains, "
    "BPMN diagrams, and activities inside SAP Signavio Process Manager "
    "(" + L("SAP Help Portal", "https://help.sap.com/docs/signavio-process-manager/user-guide/import-apqc-framework") + "), "
    "which gives the spine a concrete tooling landing.",
)

add(
    "p",
    "The spine threads a single ID from the PCF process element through: "
    "(a) the blueprint entry, (b) the technical design record, "
    "(c) the technical object, (d) the test plan and test scripts, "
    "(e) the dataset extract or migration object, and "
    "(f) the role, position, and authorisation record. In the SAP Activate "
    "phase model — Discover, Prepare, Explore, Realize, Deploy, Run "
    "(" + L("SAP Activate", "https://www.sap.com/products/erp/activate-methodology.html") + ") "
    "— the spine gives every fit-to-standard workshop in Explore a "
    "traceable identifier, every configuration decision a traceable owner, "
    "and every cutover in Deploy a traceable dataset lineage. SAP Cloud ALM "
    "already embeds SAP Activate task content, templates, and accelerators "
    "with quality gates per phase "
    "(" + L("SAP Support", "https://support.sap.com/en/alm/sap-cloud-alm/transition-to-sap-cloud-alm.html") + "), "
    "which is the natural landing point for the spine in the phase gates.",
)

add(
    "p",
    "Two clarifications matter for the peer reviewer. The PCF is a taxonomy, "
    "not a control framework, and it is not published as an end-to-end "
    "requirement-to-cutover traceability spine — that structural use is the "
    "framework's contribution. Second, the framework treats the APQC as the "
    "default nomenclature and explicitly declares nomenclature as swappable: "
    "an SAP-native process taxonomy or a bespoke client taxonomy can replace "
    "the APQC without changing the spine's mechanics, provided the replacement "
    "carries stable IDs.",
)

add("h3", "3.3 Adoption-first sequencing")

add(
    "p",
    "The framework's third choice is to move learning and role design forward "
    "in the plan, on the evidence that people, not technology, are now the "
    "binding constraint. The strongest quantitative support is Prosci's "
    "finding that 63% of AI implementation challenges are human-factor and "
    "user proficiency accounts for 38% of failure points versus 16% "
    "attributable to technical issues "
    "(" + L("Prosci, 2025", "https://www.prosci.com/blog/why-ai-transformation-fails") + "), "
    "the Wharton/GBK AI Adoption Report's statement that people and processes "
    "are the new constraint with training a top challenge for 46% of "
    "respondents "
    "(" + L("Wharton and GBK, 2025", "https://ai.wharton.upenn.edu/wp-content/uploads/2025/10/2025-Wharton-GBK-AI-Adoption-Report_Full-Report.pdf") + "), "
    "EY's finding that 88% report AI use but only 5% report advanced use and "
    "only 12% report sufficient training, leaving up to 40% of productivity "
    "gains on the table "
    "(" + L("EY, 2025", "https://www.ey.com/en_gl/newsroom/2025/11/ey-survey-reveals-companies-are-missing-out-on-up-to-40-percent-of-ai-productivity-gains-due-to-gaps-in-talent-strategy") + "), "
    "and Panorama Consulting's finding that fewer than 25% of surveyed ERP "
    "programs report intense organisational-change-management focus "
    "(" + L("Panorama, 2026", "https://4439340.fs1.hubspotusercontent-na1.net/hubfs/4439340/Reports/ERP%20Report/2026-erp-report-panorama-consulting-group.pdf") + "). "
    "The Project Management Institute's earlier work on knowledge transfer is "
    "the anchor for the durability point: knowledge-transfer-effective "
    "organisations improve outcomes by approximately 35%, and 34% of "
    "unsuccessful projects are harmed by untimely or inaccurate knowledge "
    "transfer "
    "(" + L("PMI, 2015", "https://www.pmi.org/-/media/pmi/documents/public/pdf/learning/thought-leadership/pulse/capture-value-knowledge-transfer.pdf") + ").",
)

add(
    "p",
    "In practice this means the plan reads differently. Role design, learning-"
    "path assignment, and human-authorised decision rehearsal are scheduled "
    "in the Prepare and Explore phases rather than deferred to Deploy. The "
    "hypercare model is designed against expected human-adoption gaps rather "
    "than expected technical defects. The metric for phase gate exit shifts "
    "from artifact completeness to authorised-decision throughput.",
)

add("h3", "3.4 The human-authorised decision as the control boundary")

add(
    "p",
    "The framework's control boundary between AI-prepared analysis and "
    "accountable human action is the human-authorised decision artifact. AI "
    "assembles evidence, reconciles figures, drafts the summary, and proposes "
    "recipients. A named person amends, rejects, or authorises the package. "
    "The retained record is the point-in-time evidence plus the communication "
    "the named person chose to send. The regulatory landing is already "
    "compatible: EU AI Act Article 14 requires override, stop, anomaly "
    "detection, automation-bias countermeasures, and two-person verification "
    "for Annex III 1(a) systems "
    "(" + L("EU AI Act Article 14", "https://artificialintelligenceact.eu/article/14/") + "), "
    "the NIST AI Risk Management Framework requires documented oversight "
    "processes and differentiated human-AI roles "
    "(" + L("NIST AI 100-1", "https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf") + "), "
    "and ISO/IEC 42001 supplies the certifiable AI-management-system wrapper. "
    "Empirical work is beginning to test whether human-final-say preserves "
    "quality without slowing throughput; the finding is directionally "
    "supportive "
    "(" + L("Yang et al., 2026, Management Science", "https://ideas.repec.org/a/inm/ormnsc/v72y2026i1p242-264.html") + "), "
    "while scholarship is properly sceptical that oversight is self-executing "
    "(" + L("Enqvist, 2023", "https://www.tandfonline.com/doi/full/10.1080/17579961.2023.2245683") + ").",
)


# 4. The SAP program context ---------------------------------------------

add("h2", "4. Applying the framework inside an SAP program")

add(
    "p",
    "The SAP program context matters because it is where a large share of "
    "enterprise transformation spend already lives and because SAP has begun "
    "moving AI into the delivery methodology itself. SAP's own release notes "
    "state that Cloud ALM can generate business requirements from Fit-to-"
    "Standard workshop transcripts, cutting requirements-creation time by up "
    "to 50% and downstream user-story creation time by up to 20%, with "
    "mandatory consultant review before save "
    "(" + L("SAP News, Q4 2025", "https://news.sap.com/2026/01/sap-business-ai-release-highlights-q4-2025/") + "; " + L("SAP Cloud ALM requirement generation", "https://www.sap.com/products/technology-platform/cloud-alm-requirement-generation.html") + "). "
    "Joule has grown from more than 1,300 skills in early 2025 to 35 "
    "solutions, more than 30 specialised agents, and more than 2,500 skills "
    "by Q1 2026 "
    "(" + L("SAP News, 2025", "https://news.sap.com/2025/02/joule-sap-uniquely-delivers-ai-agents/") + "; " + L("SAP News, Q1 2026", "https://news.sap.com/2026/04/sap-business-ai-release-highlights-q1-2026/") + "). "
    "SAP is also moving the exit path: Solution Manager mainstream maintenance "
    "ends 31 December 2027, and the transition to Cloud ALM is itself "
    "delivered as an SAP Activate roadmap "
    "(" + L("SAP Support", "https://support.sap.com/en/alm/sap-cloud-alm/transition-to-sap-cloud-alm.html") + ").",
)

add(
    "tbl",
    (
        ["SAP Activate phase", "DI framework contribution", "Landing tool"],
        [
            ["Discover", "Baseline decision inventory; fit-to-DI heat map; sovereign-surface scoping", "Client DMZ; SAP Signavio"],
            ["Prepare", "APQC spine adoption; role design; learning-path assignment; DMZ AI stand-up", "SAP Cloud ALM; Signavio; Joule"],
            ["Explore", "Fit-to-standard sessions traced by PCF ID; human-authorised decision rehearsal", "SAP Cloud ALM (requirement generation)"],
            ["Realize", "Test plan and dataset lineage on the same PCF ID; migration objects registered", "SAP Cloud ALM; migration cockpit"],
            ["Deploy", "Cutover authorised as decision artifact; hypercare designed against adoption gaps", "SAP Cloud ALM; ticketing"],
            ["Run", "Sovereign context repository handed to client; DT4DI-style maturity metric adopted", "Client-owned DMZ surface"],
        ],
    ),
)

add(
    "p",
    "The framework is deliberately additive to this toolchain: SAP Cloud ALM "
    "and SAP Signavio remain authoritative for their respective concerns; "
    "Joule remains the in-application copilot; the sovereign context-"
    "reasoning surface orchestrates work around them and holds program memory "
    "on behalf of the client.",
)


# 5. Program memory case ------------------------------------------------

add("h2", "5. Program memory and the asset-recovery case")

add(
    "p",
    "The argument for treating the sovereign context-reasoning repository as "
    "a capital asset rests on a documented pattern: transformation programs "
    "roll off, their consultants leave, and their institutional context "
    "leaves with them. PMI's own work names this directly — knowledge-"
    "transfer-effective organisations improve outcomes by approximately 35%, "
    "and 34% of unsuccessful projects are harmed by untimely or inaccurate "
    "knowledge transfer "
    "(" + L("PMI, 2015", "https://www.pmi.org/-/media/pmi/documents/public/pdf/learning/thought-leadership/pulse/capture-value-knowledge-transfer.pdf") + "). "
    "ERP-specific work is older but consistent: knowledge \"may vanish soon "
    "after implementation\" once the delivery team leaves "
    "(" + L("Revia, 2007", "http://www.diva-portal.org/smash/get/diva2:4611/FULLTEXT01.pdf") + "). "
    "The Standish CHAOS figures often cited alongside these arguments are "
    "contested at method level over 5,457 forecasts "
    "(" + L("Eveleens and Verhoef, IEEE, 2010", "https://www.cs.vu.nl/~x/the_rise_and_fall_of_the_chaos_report_figures.pdf") + ") "
    "and are used here only as context, not as evidence.",
)

add(
    "p",
    "IKEA is a useful case because the transformation is publicly documented "
    "and because the attribution is instructive. The ERP-anchored "
    "transformation is Inter IKEA Supply's: a new ERP is \"the main change "
    "driver for the business transformation,\" the digital core and general "
    "ledger were replaced in FY25, and the programme continues through FY26 "
    "and FY27 "
    "(" + L("Inter IKEA Holding FY25 annual report", "https://www.inter.ikea.com/-/media/interikea/igi/financial-reports/fy25-financial-reports/inter-ikea-holding-bv-annual-report-fy25-final.pdf?rev=10c81cc96c064789932e13ebf6229492&sc_lang=en") + "). "
    "The EUR 3.4bn FY24 capex, which includes business transformation, is "
    "Ingka Group's rather than Inter IKEA's "
    "(" + L("Ingka Group FY24", "https://www.ingka.com/static/ingkagroup_annualsummaryandsustainabilityreport_fy24.pdf") + "). "
    "No primary source states a single consolidated headline figure for the "
    "combined transformation program spend across the IKEA franchise "
    "structure, so any single number will be a paraphrase and should be "
    "treated with care.",
)

add(
    "p",
    "The point is not the headline figure. The point is that programs of this "
    "scale generate multi-year context that is worth more, retained, than the "
    "next headline consulting engagement, and that AI now makes retaining it "
    "practical for the first time. The compounding capital asset is the "
    "sovereign, indexed, and searchable record of what the program decided "
    "and why. Framing this as \"program memory\" rather than \"analytics\" "
    "changes the buying question — from which platform will host the "
    "analytics, to which side of the contract holds the resulting asset when "
    "the engagement ends.",
)

add(
    "p",
    "There is also a defensibility question that the buying conversation "
    "tends to skip. Copyright, in the US framing, protects fixed expression "
    "and not ideas, methods, or reasoning patterns (the idea/expression "
    "dichotomy in 17 U.S.C. \u00a7 102(b), "
    + L("U.S. Copyright Act, \u00a7 102(b)", "https://www.copyright.gov/title17/92chap1.html#102") +
    "). Patents can reach further into methods but expire and require public "
    "disclosure. The regime that actually rewards a client for compounding a "
    "sovereign reasoning surface inside its own DMZ is trade-secret protection, "
    "which turns on the client keeping the material confidential and taking "
    "reasonable measures to do so ("
    + L("Defend Trade Secrets Act, 18 U.S.C. \u00a7 1836", "https://www.law.cornell.edu/uscode/text/18/1836") +
    "). Program memory held by an SI is at best jointly held; program memory "
    "held inside the client's DMZ, under the client's access controls, is the "
    "legal shape of a trade secret. This is one of the practical reasons the "
    "framework insists on the client-DMZ location for the reasoning surface, "
    "independent of the sovereignty argument.",
)


# 6. Client vs SI boundary -----------------------------------------------

add("h2", "6. Client and systems-integrator tooling balance")

add(
    "p",
    "One of the framework's harder claims is that both the client and the "
    "systems integrator now hold AI context-reasoning capital, and the "
    "boundary between them must be negotiated deliberately rather than "
    "assumed away. The market is currently offering three incompatible "
    "answers. IDC names \"Service Provider Agentic AI Platforms\" as "
    "provider-owned platforms that persist after engagement end and urges "
    "explicit IP and data terms "
    "(" + L("IDC", "https://www.idc.com/resource-center/blog/from-labor-arbitrage-to-platform-led-outcomes-how-agentic-ai-is-rewriting-the-it-services-playbook/") + "). "
    "Vendors are converging on client-owned patterns in their marketing "
    "material "
    "(" + L("Accenture AI Refinery", "https://www.accenture.com/us-en/services/ai-data/ai-refinery") + "; " + L("IBM Enterprise Advantage, 2026", "https://newsroom.ibm.com/2026-01-19-ibm-launches-enterprise-advantage-service-to-help-businesses-scale-agentic-ai") + "). "
    "McKinsey argues that the ERP vendors themselves may own the agentic "
    "layer "
    "(" + L("McKinsey", "https://www.mckinsey.com/capabilities/mckinsey-technology/our-insights/the-end-of-erp-as-we-know-it-five-ways-ai-is-disrupting-erp") + "). "
    "The peer-reviewed literature is essentially silent on this three-way "
    "contest; the boundary is being specified in legal commentary rather "
    "than in academic work "
    "(" + L("Morgan Lewis, 2024", "https://www.morganlewis.com/blogs/sourcingatmorganlewis/2024/09/structuring-rights-to-ai-ml-outputs-insights-and-improvements-when-customer-data-is-foundational") + ").",
)

add(
    "p",
    "The framework's position is that systems integrators are expected and "
    "entitled to adopt new tooling faster than clients — that is the "
    "effective role of the integrator — but the sovereign context-reasoning "
    "repository is the client's residual, and treating it otherwise "
    "reproduces the platform-lock-in pattern of the previous generation of "
    "tooling in a form that is harder to unwind because the asset is context "
    "rather than code. The corollary is that client-side tooling must be "
    "planned in parallel with SI-side tooling from the Discover phase forward, "
    "not retrofitted at Run.",
)


# 7. Adoption-first, in detail -------------------------------------------

add("h2", "7. Adoption sequencing and the ADKAR handshake")

add(
    "p",
    "The framework's adoption-first sequencing is designed to compose with "
    "Prosci's ADKAR model and Kotter's eight-step model rather than replace "
    "them. The primary handshake is that Awareness and Desire (ADKAR) are "
    "sequenced against the Discover and Prepare phases; Knowledge and "
    "Ability against Explore and Realize; and Reinforcement against Deploy "
    "and Run. What is different is the priority: learning-path assignment "
    "and human-authorised decision rehearsal are scheduled in Prepare, not "
    "after Realize, because the empirical constraint is now people rather "
    "than technical delivery.",
)

add(
    "p",
    "The change-management literature also gives a specific number for the "
    "ERP context: change management is approximately 40% of ERP-adjacent "
    "success versus 25% for technical configuration "
    "(" + L("ERP Today", "https://erp.today/how-ai-is-forcing-erp-vendors-to-rethink-the-human-side-of-transformation/") + "), "
    "which is consistent with Panorama's finding that fewer than 25% of "
    "surveyed programs report intense OCM focus "
    "(" + L("Panorama, 2026", "https://4439340.fs1.hubspotusercontent-na1.net/hubfs/4439340/Reports/ERP%20Report/2026-erp-report-panorama-consulting-group.pdf") + "). "
    "The framework proposes that programs treat the OCM budget line as the "
    "primary variable and design the technical plan around it, rather than "
    "the reverse. Formal causal testing of adoption-first sequencing is "
    "\"n.a.\" in the current literature; this is one of the paper's open "
    "invitations to peer review.",
)


# 8. Open questions / peer review invitation ----------------------------

add("h2", "8. Open questions and peer-review invitation")

add(
    "p",
    "The framework is offered as a practitioner argument, and the author does "
    "not have the data to close every claim in it. The following are the "
    "specific places where the argument is thin, contradictory, or ahead of "
    "the literature, and where peer review is invited:",
)

add(
    "bul",
    [
        "Decision intelligence has a canonical definition but not yet a shared set of measurable constructs or a peer-reviewed instrument; a practitioner instrument is proposed but not validated.",
        "TM Forum DT4DI is telco-scoped and publishes no named operator case study; extending its ontology and maturity model to enterprise SAP programs is proposed but unvalidated.",
        "The APQC PCF has stable five-digit IDs but is not published as an end-to-end requirement-to-cutover traceability spine; this structural use is the paper's novel contribution and has no published precedent.",
        "SAP's stated productivity figures for Cloud ALM AI requirements generation (up to 50% requirements-time reduction, up to 20% user-story-time reduction) are vendor-reported and not independently replicated.",
        "Sovereign AI is used in two incompatible senses (national capability and organisational data residency) and the paper adopts the organisational sense without defending the definitional choice at length.",
        "Client-DMZ agent deployment is asserted more strongly by vendor architecture than by documented deployments; named enterprise deployments are \"n.a.\" in current primary literature.",
        "Program-memory loss is well-evidenced in aggregate (PMI) but weakly evidenced for the specific pattern of consultant roll-off in SAP transformations.",
        "The client-versus-integrator boundary is subject to a direct contradiction between IDC and McKinsey and is not treated in peer-reviewed literature; the framework's position is a normative one.",
        "Adoption-first sequencing rests on cross-sectional surveys rather than experimental or quasi-experimental tests, and formal causal evaluation is \"n.a.\" in the current literature.",
        "Human oversight at program-decision volume may not scale without sampling and escalation rules; the framework proposes human-authorised decision artifacts as the control boundary but does not yet specify the sampling rule.",
    ],
)

add(
    "p",
    "Reviewers are asked to focus, where possible, on the four claims that "
    "are load-bearing for the framework as a whole: (1) the client-DMZ "
    "sovereignty claim, (2) the APQC-spine traceability claim, (3) the "
    "adoption-first sequencing claim, and (4) the human-authorised decision "
    "artifact as the control boundary. Commentary is invited via GitHub "
    "issues on the paper's public repository "
    "(" + L("EVEglyphDesign/decision-intelligence-framework", "https://github.com/EVEglyphDesign/decision-intelligence-framework") + ").",
)


# 9. Closing ------------------------------------------------------------

add("h2", "9. Conclusion")

add(
    "p",
    "The AI generation of enterprise tooling does not displace the previous "
    "generation. It adds a new dimension — a set of tools for managing all "
    "the old tools — and it moves the compounding asset from operational "
    "throughput to the sovereign record of how the enterprise learns. The "
    "framework proposed here is a practitioner argument for treating that "
    "record as a client-owned capital asset, for tying it to the process "
    "spine already available in the APQC PCF, and for resequencing the plan "
    "on the evidence that people are now the binding constraint. Standards "
    "will catch up. Programs cannot wait for them. What programs can do is "
    "adopt a common practitioner framework that is honest about where it is "
    "ahead of the literature, and invite peer review to close the gap.",
)


# --- Appendices ---------------------------------------------------------

add("h2", "Appendix A. Suggested peer-review venues")

add(
    "p",
    "The paper is offered for submission at the author's discretion to any of "
    "the following. MIT Sloan Management Review is included in the "
    "practitioner literature above but is no longer accepting submissions "
    "and is not a viable venue "
    "(" + L("MIT SMR author guidelines", "https://sloanreview.mit.edu/authors/") + ").",
)

add(
    "bul",
    [
        L("MIS Quarterly Executive", "https://aisel.aisnet.org/misqe/policies.html") + " — MISQE Editorial Policies. Single-blind, up to 7,500 words, best fit for a practitioner framework grounded in field engagement.",
        L("Hawaii International Conference on System Sciences (HICSS)", "https://hicss.hawaii.edu/authors/") + " — minitrack model, double-blind, review June to August.",
        L("IEEE Software", "https://www.computer.org/digital-library/magazines/so/cfp-ieee-software") + " — between research and practice; wants project successes and failures.",
        L("Communications of the ACM (Practice section)", "https://cacm.acm.org/practice/communications-practice-section-welcomes-submissions/") + " — postmortems and cautionary tales; contact editors first (" + L("ACM author overview", "https://authors.acm.org/magazines/cacm") + ").",
        L("Journal of Enterprise Information Management", "https://www.emeraldgrouppublishing.com/journal/jeim") + " — explicitly accepts consultant case experience.",
        L("TM Forum Collaboration", "https://www.tmforum.org/member-projects/collaboration") + " — member-only, IPR form required; a contribution route rather than an article submission.",
        L("ISACA Journal", "https://www.isaca.org/resources/isaca-journal/submit-an-article") + " — 2,000 to 3,000 words, double-blind, no AI assistance permitted.",
        L("Journal of Decision Systems", "https://www.tandfonline.com/journals/tjds20/about-this-journal") + " — decision systems and augmented decision environments.",
        L("Intelligent Decision Technologies", "https://journals.sagepub.com/doi/10.1177/18724981251316079") + " — AI plus decision support plus systems engineering.",
    ],
)

add("h2", "Appendix B. Framework primitives (glossary)")

add(
    "bul",
    [
        "<b>Sovereign context-reasoning surface.</b> An AI reasoning surface running inside the client's DMZ that holds program context (transcripts, decisions, rationale) as a client-owned capital asset.",
        "<b>APQC-spined traceability.</b> A program-wide numbering scheme anchored on APQC PCF five-digit stable IDs, threaded through blueprint, technical design, technical object, test plan, dataset, and role and authorisation records.",
        "<b>Human-authorised decision artifact.</b> The point-in-time evidence package plus the communication a named person reviewed, edited, and chose to send. The control boundary between AI-prepared analysis and accountable human action.",
        "<b>Adoption-first sequencing.</b> Scheduling role design, learning-path assignment, and human-authorised decision rehearsal in the Prepare and Explore phases of SAP Activate rather than deferring them to Deploy.",
        "<b>Program memory.</b> The sovereign, indexed, and searchable record of what the program decided and why. Retained across engagements as a compounding client-owned asset rather than lost when consultants roll off.",
        "<b>Additive positioning.</b> The framework does not displace SAP Cloud ALM, Signavio, Solution Manager, Joule, Jira, or Azure DevOps. It orchestrates work around them and holds the sovereign record beside them.",
    ],
)
