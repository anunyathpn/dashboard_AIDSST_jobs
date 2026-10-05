# Business Requirements Document (BRD)
## Project: AI, Data Science & Statistics Workforce & Skill Mismatch Analytics Dashboard
**Target Platform:** AntiGravity / Python Web Dashboard (Dash / Plotly / FastAPI)  
**Version:** 1.0.0  
**Date:** October 5, 2026  
**Status:** Approved for Development  

---

## 1. Executive Summary & Project Objectives

### 1.1 Executive Summary
The rapid growth of Artificial Intelligence (AI), Data Science (DS), and Statistics (Stat) industries has created a dynamic job market with evolving skill requirements. Educational institutions produce thousands of graduates annually, yet industry leaders frequently report skill gaps and hiring mismatches. This project defines the Business Requirements Document (BRD) for developing an **Interactive Analytics Dashboard** that bridges the gap between educational supply and industry demand.

### 1.2 Core Objectives
1. **Supply Side Analysis (Tab 1):** Map academic throughput, degree curriculum alignments, core skill teachings, tuition fees, and graduate employment progression across 1 to 3 years post-graduation.
2. **Demand Side Analysis (Tab 2):** Track real-time job openings, desired core skills, hiring companies, and salary distributions across career levels (Entry, Mid, Senior, Lead).
3. **Skill Mismatch & Gap Analysis (Tab 3):** Perform automated cross-comparison between academic curricula (Tab 1) and job requirements (Tab 2) to quantify skill surplus, skill deficit, and market alignment index.

---

## 2. Technical Architecture & Framework Guidelines

### 2.1 Backend Framework Requirements
- **Core Language:** Python 3.10+
- **Backend Framework:** Python (FastAPI / Dash Backend Server / Flask Engine)
- **Data Engine:** Pandas / DuckDB for fast in-memory querying and aggregation of Open Data CSV files.
- **REST / WebSocket Protocol:** Efficient data payload transmission for sub-second reactive filter execution.

### 2.2 Frontend & Dashboard Framework
- **Primary Visualization Engine:** `Plotly` (Plotly Express / Plotly Graph Objects)
- **Dashboard Framework:** `Dash by Plotly` or `Streamlit` / `FastAPI + Plotly.js`
- **Interactivity Standard (Cross-Filtering / Linked Callbacks):**
  - **Cross-Filtering across ALL graphs in a Tab:** Clicking a bar, pie segment, line node, or selecting a dropdown/slider filter in any chart MUST trigger a callback updating all other graphs on the active Tab.
  - State persistence across Tab switches using Dash `dcc.Store` or Python session state.

---

## 3. Tab-by-Tab Functional Requirements

---

### 3.1 Tab 1: Supply Side — Academic Graduates & Taught Skills (ปริมาณคนที่จบ และ skills ที่เรียนมา)

#### Goal:
Provide detailed insights into university production capacity, core mandatory course skills taught, graduate employment progression (Year 1 to Year 3), and tuition costs.

#### Key Performance Indicators (KPI Cards):
- Total Annual Graduates Output (AI / DS / Stat)
- Average Tuition Fee across Institutions
- Year-1 Average Employment Rate (%)
- Top Taught Technical Skill across Curricula

#### Required Visualizations & Interactivity (Linked via Plotly Callbacks):

1. **Graph 1.1: Annual Graduates Output by Academic Program & Degree Level**
   - **Type:** Stacked Bar Chart / Grouped Column Chart
   - **X-Axis:** Graduation Year (e.g., 2021 – 2026)
   - **Y-Axis:** Total Number of Graduates
   - **Color Dimension:** Academic Program Name (e.g., *B.Sc. Data Science*, *M.Sc. Artificial Intelligence*, *B.Sc. Applied Statistics*)
   - **Interaction:** Clicking a program bar filters all other Tab 1 graphs to show data exclusive to that selected program.

2. **Graph 1.2: Mandatory Course Curriculum & Skill Coverage Matrix**
   - **Type:** Heatmap / Horizontal Bar Chart
   - **Dimensions:** Academic Program vs. Mandatory Technical Courses & Skills Taught (e.g., Python, R, SQL, Linear Algebra, Machine Learning, Deep Learning, Cloud Computing, MLOps).
   - **Metric:** Course Credit Weight / Skill Coverage Score (1–5 scale).
   - **Interaction:** Selecting a specific skill highlight updates the graduate output and employment graphs.

3. **Graph 1.3: Post-Graduation Employment Cohort (Year 1, Year 2, Year 3)**
   - **Type:** Multi-Line Chart / Grouped Multi-Bar Chart
   - **X-Axis:** Employment Horizon (Year 1, Year 2, Year 3 Post-Graduation)
   - **Y-Axis:** Count / Percentage of Employed Graduates in AI/DS/Stat roles.
   - **Breakdown:** Status (Employed in Field, Employed Out-of-Field, Higher Education, Unemployed).
   - **Interaction:** Hovering or clicking a cohort year filters the tuition and course breakdown.

4. **Graph 1.4: Academic Program Tuition Fee vs. Graduate Employment Rate**
   - **Type:** Scatter Plot / Bubble Chart
   - **X-Axis:** Total Tuition Fee (THB / USD)
   - **Y-Axis:** Year-1 Employment Rate (%)
   - **Bubble Size:** Annual Graduate Capacity
   - **Color:** Institution / Degree Level (Undergraduate vs Graduate)
   - **Interaction:** Dynamic range slider for tuition fee filtering.

---

### 3.2 Tab 2: Demand Side — Job Openings & Industry Skill Demands (ปริมาณงานที่จ้าง และ skills ที่ต้องการ)

#### Goal:
Monitor the demand side of the job market by tracking job availability, in-demand technical and soft skills, hiring companies, and compensation benchmarks by experience level.

#### Key Performance Indicators (KPI Cards):
- Total Active Job Postings
- Top In-Demand Skill (e.g., Python / SQL / AWS)
- Median Starting Salary for Entry-Level Roles
- Top Hiring Industry Sector

#### Required Visualizations & Interactivity (Linked via Plotly Callbacks):

1. **Graph 2.1: Volume of Open Job Positions by Role Title & Country/Region**
   - **Type:** Horizontal Bar Chart / Treemap Visualization
   - **Metric:** Total Vacant Positions / Job Postings
   - **Dimensions:** Role Category (Data Scientist, AI Engineer, ML Engineer, Statistician, Data Engineer) and Geographic Location.
   - **Interaction:** Clicking a role title filters skills, companies, and salaries across Tab 2.

2. **Graph 2.2: Top In-Demand Technical Skills Frequency in Job Descriptions**
   - **Type:** Ranked Horizontal Bar Chart / Radar Chart
   - **X-Axis:** Percentage of Job Postings Explicitly Demanding the Skill
   - **Y-Axis:** Technical Skill Keyword (e.g., *Python, SQL, PyTorch, Docker, Kubernetes, Spark, RAG, AWS, A/B Testing*)
   - **Color:** Skill Category (Programming, MLOps, Statistics, Cloud, Frameworks)
   - **Interaction:** Clicking a skill highlights companies and role levels requiring that skill.

3. **Graph 2.3: Top Hiring Companies & Industry Sectors**
   - **Type:** Donut Chart / Packed Bubble Chart
   - **Metric:** Number of Active Job Postings per Company
   - **Category:** Hiring Company Name & Sector (Tech, Finance, Healthcare, Retail, Consulting).
   - **Interaction:** Filtering by company narrows down the required skills and salary distribution.

4. **Graph 2.4: Salary Distribution across Career Experience Levels**
   - **Type:** Box Plot / Violin Plot / Grouped Bar Chart
   - **X-Axis:** Career Experience Level (*Entry / Junior [0-2 yrs]*, *Mid-Level [2-5 yrs]*, *Senior / Lead [5+ yrs]*, *Executive*)
   - **Y-Axis:** Monthly / Annual Salary (USD or Local Currency equivalent)
   - **Overlay:** Minimum, Median, Maximum, and Percentile ranges.
   - **Interaction:** Linked with role category and country selectors.

---

### 3.3 Tab 3: Analytical Gap Analysis — Skill Mismatch Matrix (วิเคราะห์ สกิล mismatch จาก Tab 1 และ Tab 2)

#### Goal:
Synthesize data from Tab 1 (Supply Curriculum Skills) and Tab 2 (Demand Industry Required Skills) to pinpoint curriculum deficiencies, skills oversupply, and strategic alignment recommendations.

#### Key Performance Indicators (KPI Cards):
- Overall Curriculum Alignment Index (%)
- Critical Skill Deficit Count (High Demand, Low Academic Coverage)
- Oversupplied Skill Count (High Academic Coverage, Low Industry Demand)
- High-Value Emerging Skill Target

#### Required Visualizations & Interactivity (Linked via Plotly Callbacks):

1. **Graph 3.1: Skill Supply vs. Demand Quadrant Analysis (The Mismatch Matrix)**
   - **Type:** 4-Quadrant Scatter Plot / Bubble Matrix
   - **X-Axis:** Academic Teaching Frequency Score (Supply % from Tab 1)
   - **Y-Axis:** Job Posting Demand Frequency Score (Demand % from Tab 2)
   - **Quadrants:**
     - **Quadrant I (High Supply, High Demand):** *Core Essentials* (e.g., Python, SQL, Basic Statistics)
     - **Quadrant II (Low Supply, High Demand):** *CRITICAL DEFICIT / SKILL GAP* (e.g., MLOps, LLM Fine-Tuning, Docker, PyTorch)
     - **Quadrant III (Low Supply, Low Demand):** *Niche Skills*
     - **Quadrant IV (High Supply, Low Demand):** *OVERSUPPLIED / OUTDATED* (e.g., Theoretical Math without execution, Legacy Software)
   - **Interaction:** Clicking a data point displays a detailed breakdown card of universities teaching vs. companies requiring that skill.

2. **Graph 3.2: Skill Gap Score Breakdown by Role Category**
   - **Type:** Diverging Bar Chart / Net Gap Rating Plot
   - **Metric:** `Net Gap = Demand Score (%) - Supply Score (%)`
   - **Positive Values:** Skill Shortage in Industry (Academia needs to add to curriculum)
   - **Negative Values:** Skill Oversupply / Excess Focus
   - **Interaction:** Dynamic filtering by Job Role (*Data Engineer vs. AI Research Engineer vs. Applied Statistician*).

3. **Graph 3.3: Salary Premium vs. Academic Coverage Correlation**
   - **Type:** Dual-Axis Line & Bar Chart
   - **Primary Y-Axis:** Average Starting Salary Premium for Candidate possessing Skill
   - **Secondary Y-Axis:** % of University Curricula Covering the Skill
   - **Objective:** Identify high-yield skills that offer high entry salaries but are rarely taught in standard university programs.

---

## 4. Open Data Sources Specification

AntiGravity should ingest, clean, and join the following open datasets to power the dashboard backend:

| Data Category | Dataset Name | Source / Provider | Format | Key Fields / Schema |
| :--- | :--- | :--- | :--- | :--- |
| **Supply (Tab 1)** | NCES IPEDS Completion Data | US Dept. of Education | `.csv` / API | `CIP_Code`, `Institution_Name`, `Degree_Level`, `Graduates_Count`, `Year`, `Tuition_Fee` |
| **Supply (Tab 1)** | Eurostat Tertiary Education Graduates | Eurostat Open Data Portal | `.csv` / `.tsv` | `Country`, `Field_of_Study` (ICT/Stat), `Graduates_Count`, `Year` |
| **Supply (Tab 1)** | University Curricula & Employment Tracker | Kaggle / Institutional Open Data | `.csv` | `Program_Name`, `Mandatory_Courses`, `Skills_Taught`, `Year1_Emp`, `Year2_Emp`, `Year3_Emp` |
| **Demand (Tab 2)** | AI Job Market Global Dataset | Kaggle Open Datasets | `.csv` | `Job_Title`, `Company`, `Industry`, `Location`, `Experience_Level`, `Salary_USD`, `Required_Skills` |
| **Demand (Tab 2)** | Data Science Job Postings & Skills | Kaggle Open Datasets | `.csv` | `Job_ID`, `Company_Name`, `Role_Category`, `Skill_Keywords`, `Posting_Date`, `Job_Type` |

---

## 5. Non-Functional & UI/UX Requirements

1. **Performance & Responsiveness:**
   - Initial dashboard load time < 2.5 seconds.
   - Cross-filtering graph update latency < 300 ms across all Plotly charts.
2. **Design Language & Theme:**
   - **Style:** Clean, professional enterprise dark/light theme (Navy Blue `#0f172a`, Accent Cyan `#06b6d4`, Warning Amber `#f59e0b`, Alert Red `#ef4444`).
   - Mobile and desktop responsive layout with dynamic grid container auto-fitting.
3. **Data Export & Handoff Capabilities:**
   - Include CSV export buttons for filtered datasets on each Tab.
   - Include high-resolution PNG/SVG export on Plotly graph toolbars.

---

## 6. AntiGravity Developer Handoff Checklist

- [ ] Initialize Python backend (`FastAPI` or `Dash App` container).
- [ ] Load and clean Open Data CSV files using Pandas/DuckDB schema pipeline.
- [ ] Build Tab 1 reactive layout and link Cross-Filtering callbacks (`dcc.Graph` `selectedData` / `clickData`).
- [ ] Build Tab 2 reactive layout for Job Openings, Companies, Skills, and Salary Boxplots.
- [ ] Implement Tab 3 Data Processing Function: Compute `Skill Mismatch Net Score = Demand_Pct - Supply_Pct` dynamically.
- [ ] Conduct end-to-end user acceptance testing for linked graph interactions across all 3 tabs.
