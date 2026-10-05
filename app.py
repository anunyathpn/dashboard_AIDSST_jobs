import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

st.set_page_config(page_title="Workforce & Skill Mismatch Analytics", layout="wide")

st.title("AI, Data Science & Statistics Workforce & Skill Mismatch Analytics")
st.markdown("Bridge the gap between educational supply and industry demand through interactive analytics.")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", [
    "Overview", 
    "1. Supply Side (Academic)", 
    "2. Demand Side (Industry)", 
    "3. Skill Mismatch (Gap Analysis)"
])

if page == "Overview":
    st.header("Project Overview")
    st.markdown("""
    This dashboard analyzes the global workforce in Artificial Intelligence (AI), Data Science (DS), and Statistics.
    
    ### Core Objectives
    1. **Supply Side Analysis:** Map academic throughput, degree curriculum alignments, core skill teachings, tuition fees, and graduate employment progression.
    2. **Demand Side Analysis:** Track real-time job openings, desired core skills, hiring companies, and salary distributions.
    3. **Skill Mismatch & Gap Analysis:** Automated cross-comparison between academic curricula and job requirements to quantify skill surplus, deficit, and market alignment.
    """)

elif page == "1. Supply Side (Academic)":
    st.header("Tab 1: Supply Side — Academic Graduates & Taught Skills")
    
    # KPIs
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Annual Graduates", "123,000", "+5.2%")
    col2.metric("Avg Tuition Fee", "$25,000", "-2%")
    col3.metric("Year-1 Employment Rate", "82%", "+1.5%")
    col4.metric("Top Taught Skill", "Python")

    st.markdown("---")
    
    colA, colB = st.columns(2)
    with colA:
        # Graph 1.1: Annual Graduates Output
        years = ['2021', '2022', '2023', '2024', '2025']
        df_grads = pd.DataFrame({
            'Year': years * 3,
            'Graduates': np.random.randint(10000, 50000, 15),
            'Program': ['B.Sc. Data Science']*5 + ['M.Sc. Artificial Intelligence']*5 + ['B.Sc. Applied Statistics']*5
        })
        fig1_1 = px.bar(df_grads, x='Year', y='Graduates', color='Program', 
                        title='Graph 1.1: Annual Graduates Output by Program', barmode='group')
        st.plotly_chart(fig1_1, use_container_width=True)

    with colB:
        # Graph 1.2: Mandatory Course Curriculum & Skill Coverage
        skills = ['Python', 'SQL', 'Linear Algebra', 'Machine Learning', 'Cloud Computing', 'MLOps']
        programs = ['B.Sc. DS', 'M.Sc. AI', 'B.Sc. Stat']
        coverage_matrix = np.random.randint(1, 6, size=(len(programs), len(skills)))
        fig1_2 = px.imshow(coverage_matrix, labels=dict(x="Skills", y="Programs", color="Coverage Score"),
                           x=skills, y=programs, title="Graph 1.2: Skill Coverage Matrix")
        st.plotly_chart(fig1_2, use_container_width=True)
        
    colC, colD = st.columns(2)
    with colC:
        # Graph 1.3: Post-Graduation Employment Cohort
        cohort_years = ['Year 1', 'Year 2', 'Year 3']
        df_cohort = pd.DataFrame({
            'Horizon': cohort_years * 3,
            'Rate (%)': [82, 88, 92, 10, 8, 5, 8, 4, 3],
            'Status': ['Employed in Field']*3 + ['Employed Out-of-Field']*3 + ['Unemployed']*3
        })
        fig1_3 = px.line(df_cohort, x='Horizon', y='Rate (%)', color='Status', 
                         title='Graph 1.3: Post-Graduation Employment Cohort', markers=True)
        st.plotly_chart(fig1_3, use_container_width=True)
        
    with colD:
        # Graph 1.4: Academic Program Tuition Fee vs. Employment Rate
        df_tuition = pd.DataFrame({
            'Tuition ($)': np.random.randint(10000, 60000, 20),
            'Employment Rate (%)': np.random.uniform(70, 98, 20),
            'Capacity': np.random.randint(50, 500, 20),
            'Level': ['Undergraduate', 'Graduate'] * 10
        })
        fig1_4 = px.scatter(df_tuition, x='Tuition ($)', y='Employment Rate (%)', size='Capacity', color='Level',
                            title='Graph 1.4: Tuition Fee vs. Employment Rate')
        st.plotly_chart(fig1_4, use_container_width=True)

elif page == "2. Demand Side (Industry)":
    st.header("Tab 2: Demand Side — Job Openings & Industry Skill Demands")
    
    # KPIs
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Active Postings", "45,230", "+12%")
    col2.metric("Top In-Demand Skill", "Python")
    col3.metric("Median Entry Salary", "$85,000")
    col4.metric("Top Hiring Industry", "Technology")

    st.markdown("---")
    
    colA, colB = st.columns(2)
    with colA:
        # Graph 2.1: Volume of Open Job Positions
        roles = ['Data Scientist', 'AI Engineer', 'ML Engineer', 'Data Engineer', 'Statistician']
        df_roles = pd.DataFrame({'Role': roles, 'Postings': [12000, 8500, 7000, 14000, 3730]})
        fig2_1 = px.bar(df_roles, x='Postings', y='Role', orientation='h', title='Graph 2.1: Open Positions by Role Title')
        fig2_1.update_layout(yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig2_1, use_container_width=True)
        
    with colB:
        # Graph 2.2: Top In-Demand Technical Skills
        skills_demand = ['Python', 'SQL', 'AWS', 'Docker', 'PyTorch', 'Spark', 'Kubernetes']
        df_skills = pd.DataFrame({'Skill': skills_demand, 'Demand (%)': [95, 80, 65, 50, 45, 40, 35]})
        fig2_2 = px.bar(df_skills, x='Demand (%)', y='Skill', orientation='h', title='Graph 2.2: In-Demand Technical Skills')
        fig2_2.update_layout(yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig2_2, use_container_width=True)

    colC, colD = st.columns(2)
    with colC:
        # Graph 2.3: Top Hiring Sectors
        sectors = ['Tech', 'Finance', 'Healthcare', 'Retail', 'Consulting']
        df_sectors = pd.DataFrame({'Sector': sectors, 'Postings': [15000, 9000, 6500, 4000, 10730]})
        fig2_3 = px.pie(df_sectors, names='Sector', values='Postings', hole=0.4, title='Graph 2.3: Hiring Industry Sectors')
        st.plotly_chart(fig2_3, use_container_width=True)

    with colD:
        # Graph 2.4: Salary Distribution
        exp_levels = ['Entry', 'Mid-Level', 'Senior', 'Executive']
        df_salary = pd.DataFrame({
            'Experience': np.repeat(exp_levels, 50),
            'Salary': np.concatenate([
                np.random.normal(85000, 10000, 50),
                np.random.normal(120000, 15000, 50),
                np.random.normal(160000, 20000, 50),
                np.random.normal(210000, 30000, 50)
            ])
        })
        fig2_4 = px.box(df_salary, x='Experience', y='Salary', color='Experience', title='Graph 2.4: Salary Distribution by Level')
        st.plotly_chart(fig2_4, use_container_width=True)

elif page == "3. Skill Mismatch (Gap Analysis)":
    st.header("Tab 3: Analytical Gap Analysis — Skill Mismatch Matrix")

    # KPIs
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Curriculum Alignment", "68%", "-2.4%")
    col2.metric("Critical Skill Deficits", "4")
    col3.metric("Oversupplied Skills", "3")
    col4.metric("High-Value Target", "MLOps")

    st.markdown("---")
    
    colA, colB = st.columns(2)
    with colA:
        # Graph 3.1: Skill Supply vs. Demand Quadrant
        mismatch_skills = ['Python', 'SQL', 'Basic Stats', 'MLOps', 'LLMs', 'Docker', 'Legacy DBs', 'Math Theory']
        df_mismatch = pd.DataFrame({
            'Skill': mismatch_skills,
            'Supply Score (%)': [90, 85, 95, 10, 5, 15, 60, 80],
            'Demand Score (%)': [95, 85, 40, 85, 75, 70, 10, 15],
            'Category': ['Core', 'Core', 'Niche', 'Deficit', 'Deficit', 'Deficit', 'Oversupply', 'Oversupply']
        })
        fig3_1 = px.scatter(df_mismatch, x='Supply Score (%)', y='Demand Score (%)', text='Skill', color='Category',
                            title='Graph 3.1: Skill Supply vs Demand (Mismatch Matrix)')
        fig3_1.add_hline(y=50, line_dash="dot")
        fig3_1.add_vline(x=50, line_dash="dot")
        fig3_1.update_traces(textposition='top center')
        st.plotly_chart(fig3_1, use_container_width=True)

    with colB:
        # Graph 3.2: Skill Gap Score Breakdown
        df_mismatch['Net Gap'] = df_mismatch['Demand Score (%)'] - df_mismatch['Supply Score (%)']
        df_mismatch = df_mismatch.sort_values('Net Gap')
        df_mismatch['Color'] = np.where(df_mismatch['Net Gap'] > 0, 'Shortage (Deficit)', 'Oversupply')
        
        fig3_2 = px.bar(df_mismatch, x='Net Gap', y='Skill', orientation='h', color='Color',
                        color_discrete_map={'Shortage (Deficit)': '#ef4444', 'Oversupply': '#3b82f6'},
                        title='Graph 3.2: Net Skill Gap Score')
        st.plotly_chart(fig3_2, use_container_width=True)

    # Graph 3.3: Salary Premium vs. Academic Coverage Correlation
    st.markdown("### Graph 3.3: Salary Premium vs. Academic Coverage Correlation")
    df_premium = pd.DataFrame({
        'Skill': ['MLOps', 'LLM Fine-Tuning', 'Docker', 'Python', 'SQL'],
        'Salary Premium ($)': [25000, 30000, 15000, 5000, 3000],
        'Academic Coverage (%)': [10, 5, 15, 90, 85]
    })
    
    fig3_3 = go.Figure()
    fig3_3.add_trace(go.Bar(x=df_premium['Skill'], y=df_premium['Salary Premium ($)'], name='Salary Premium ($)', marker_color='#f59e0b'))
    fig3_3.add_trace(go.Scatter(x=df_premium['Skill'], y=df_premium['Academic Coverage (%)'], name='Academic Coverage (%)', yaxis='y2', marker_color='#0f172a', mode='lines+markers'))
    
    fig3_3.update_layout(
        title='Salary Premium vs Academic Coverage',
        yaxis=dict(title='Salary Premium ($)'),
        yaxis2=dict(title='Academic Coverage (%)', overlaying='y', side='right', range=[0, 100]),
        barmode='group'
    )
    st.plotly_chart(fig3_3, use_container_width=True)
