# AI, Data Science & Statistics Workforce & Skill Mismatch Analytics Dashboard

This project is an interactive analytics dashboard designed to bridge the gap between educational supply (academic graduates) and industry demand (job openings) in Artificial Intelligence (AI), Data Science (DS), and Statistics. 

## Project Objectives & Architecture

The dashboard is structured into three primary analytical tabs:

1. **Tab 1: Supply Side (Academic):** Maps academic throughput, degree curriculum alignments, core skill teachings, tuition fees, and graduate employment progression.
2. **Tab 2: Demand Side (Industry):** Tracks real-time job openings, desired core skills, hiring companies, and salary distributions across career levels.
3. **Tab 3: Analytical Gap Analysis (Skill Mismatch Matrix):** Automated cross-comparison between academic curricula and job requirements to quantify skill surplus, skill deficit, and market alignment index.

## Data Sources

The dashboard backend is designed to ingest and aggregate the following Open Data CSV sources:

**Supply Side (Tab 1):**
* NCES IPEDS Completion Data (US Dept. of Education)
* Eurostat Tertiary Education Graduates (Eurostat Open Data Portal)
* University Curricula & Employment Tracker

**Demand Side (Tab 2):**
* AI Job Market Global Dataset
* Data Science Job Postings & Skills Dataset (Tech, Healthcare, Finance)
* Data Science, AI & ML Job Salaries Dataset

## Career Progression Framework

The demand-side analysis categorizes roles into core experience levels:
* **Entry-Level / Junior (EN):** 0-2 years experience.
* **Mid-Level (MI):** 2-5 years experience.
* **Senior / Lead (SE/EX):** 5+ years experience.
* **Executive:** Leadership roles.

## Tech Stack
* **Language:** Python 3.10+
* **Dashboard Framework:** Streamlit (Compliant with BRD requirements)
* **Visualization Engine:** Plotly (Plotly Express / Graph Objects)
* **Data Processing:** Pandas 
