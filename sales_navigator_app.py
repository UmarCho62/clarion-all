"""
ADA Compliance Sales Navigator
A comprehensive application to manage pet e-commerce leads and execute sales strategy
"""

import streamlit as st
import pandas as pd
import json
from datetime import datetime, timedelta
import os

# Page configuration
st.set_page_config(
    page_title="ADA Sales Navigator",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful styling
st.markdown("""
    <style>
    /* Main color scheme */
    :root {
        --primary-color: #2E86AB;
        --secondary-color: #A23B72;
        --success-color: #06A77D;
        --warning-color: #F18F01;
        --danger-color: #C73E1D;
        --background-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    /* Global styles */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main header styling */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    
    .main-header h1 {
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .main-header p {
        font-size: 1.1rem;
        margin: 0.5rem 0 0 0;
        opacity: 0.95;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #2E86AB 0%, #1a5276 100%);
        padding: 2rem 1rem;
    }
    
    [data-testid="stSidebar"] .css-1d391kg {
        background: transparent;
    }
    
    [data-testid="stSidebar"] h1 {
        color: white !important;
        font-size: 1.8rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    [data-testid="stSidebar"] label {
        color: white !important;
        font-weight: 600;
    }
    
    /* Radio buttons in sidebar */
    [data-testid="stSidebar"] .row-widget.stRadio > div {
        background: rgba(255,255,255,0.1);
        padding: 0.5rem;
        border-radius: 10px;
    }
    
    [data-testid="stSidebar"] .row-widget.stRadio > div > label > div:first-child {
        color: white !important;
    }
    
    /* Card styling */
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        border-left: 4px solid #667eea;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }
    
    .metric-card h3 {
        color: #2E86AB;
        font-size: 2rem;
        font-weight: 700;
        margin: 0;
    }
    
    .metric-card p {
        color: #666;
        font-size: 0.9rem;
        margin: 0.5rem 0 0 0;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Status badges */
    .status-badge {
        display: inline-block;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .status-not-contacted {
        background: #f0f0f0;
        color: #666;
    }
    
    .status-contacted {
        background: #e3f2fd;
        color: #1976d2;
    }
    
    .status-replied {
        background: #f3e5f5;
        color: #7b1fa2;
    }
    
    .status-meeting {
        background: #fff3e0;
        color: #f57c00;
    }
    
    .status-proposal {
        background: #e0f2f1;
        color: #00796b;
    }
    
    .status-won {
        background: #c8e6c9;
        color: #2e7d32;
    }
    
    .status-lost {
        background: #ffcdd2;
        color: #c62828;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 25px;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    
    /* Info boxes */
    .stAlert {
        border-radius: 10px;
        border: none;
        padding: 1rem 1.5rem;
    }
    
    /* Success box */
    .stSuccess {
        background: linear-gradient(135deg, #06A77D 0%, #05c896 100%);
        color: white;
    }
    
    /* Info box */
    .stInfo {
        background: linear-gradient(135deg, #2E86AB 0%, #4fa8d5 100%);
        color: white;
    }
    
    /* Warning box */
    .stWarning {
        background: linear-gradient(135deg, #F18F01 0%, #ffa726 100%);
        color: white;
    }
    
    /* Dataframe styling */
    .dataframe {
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 1rem;
        background: transparent;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: white;
        border-radius: 10px 10px 0 0;
        padding: 1rem 2rem;
        font-weight: 600;
        border: none;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    /* Metric container */
    [data-testid="stMetricValue"] {
        font-size: 2rem;
        font-weight: 700;
        color: #2E86AB;
    }
    
    [data-testid="stMetricLabel"] {
        font-size: 0.9rem;
        color: #666;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 600;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        font-weight: 600;
        padding: 1rem;
    }
    
    .streamlit-expanderContent {
        background: #f8f9fa;
        border-radius: 0 0 10px 10px;
        padding: 1.5rem;
        border: 2px solid #667eea;
    }
    
    /* Select box styling */
    .stSelectbox > div > div {
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        transition: all 0.3s ease;
    }
    
    .stSelectbox > div > div:hover {
        border-color: #667eea;
        box-shadow: 0 0 10px rgba(102, 126, 234, 0.2);
    }
    
    /* Text input styling */
    .stTextInput > div > div > input {
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 10px rgba(102, 126, 234, 0.3);
    }
    
    /* Text area styling */
    .stTextArea > div > div > textarea {
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        transition: all 0.3s ease;
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: #667eea;
        box-shadow: 0 0 10px rgba(102, 126, 234, 0.3);
    }
    
    /* Section headers */
    h1, h2, h3 {
        color: #2E86AB;
        font-weight: 700;
    }
    
    h1 {
        font-size: 2.5rem;
        margin-bottom: 1.5rem;
    }
    
    h2 {
        font-size: 2rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    
    h3 {
        font-size: 1.5rem;
        margin-top: 1.5rem;
        margin-bottom: 0.8rem;
    }
    
    /* Divider */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #667eea, transparent);
        margin: 2rem 0;
    }
    
    /* Code blocks */
    code {
        background: #f8f9fa;
        padding: 0.2rem 0.5rem;
        border-radius: 5px;
        color: #764ba2;
        font-weight: 600;
    }
    
    /* Markdown styling */
    .stMarkdown {
        font-size: 1rem;
        line-height: 1.6;
    }
    
    /* Column gaps */
    [data-testid="column"] {
        padding: 0.5rem;
    }
    
    /* Animate fade in */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .main .block-container {
        animation: fadeIn 0.5s ease-in;
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #764ba2;
    }
    
    /* Loading animation */
    .stSpinner > div {
        border-color: #667eea !important;
        border-right-color: transparent !important;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem;
        color: #666;
        font-size: 0.9rem;
        margin-top: 3rem;
        border-top: 2px solid #e0e0e0;
    }
    
    /* Highlight on hover for rows */
    .row-widget:hover {
        background: rgba(102, 126, 234, 0.05);
        border-radius: 10px;
        transition: all 0.3s ease;
    }
    </style>
""", unsafe_allow_html=True)

# File paths
LEADS_FILE = "pet_ecommerce_ada_prospects.csv"
STATUS_FILE = "lead_status.json"

# Load leads data
@st.cache_data
def load_leads():
    """Load the leads CSV file"""
    try:
        df = pd.read_csv(LEADS_FILE)
        return df
    except FileNotFoundError:
        st.error(f"Could not find {LEADS_FILE}. Please ensure the file exists.")
        return pd.DataFrame()

# Load/Save status data
def load_status():
    """Load lead status and notes from JSON file"""
    if os.path.exists(STATUS_FILE):
        with open(STATUS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_status(status_data):
    """Save lead status and notes to JSON file"""
    with open(STATUS_FILE, 'w') as f:
        json.dump(status_data, f, indent=2)

# Initialize session state
if 'status_data' not in st.session_state:
    st.session_state.status_data = load_status()

# Email templates
EMAIL_TEMPLATES = {
    "Initial Cold Outreach (Risk-Focused)": {
        "subject_lines": [
            "ADA Compliance Risk Assessment for {company}",
            "Protecting {company} from ADA website lawsuits",
            "Free accessibility audit for {company}"
        ],
        "body": """Hi {first_name},

I hope this email finds you well. I'm reaching out because {company} has built an impressive presence in the pet products industry, and I wanted to bring an important compliance matter to your attention.

E-commerce companies in the pet industry are increasingly targeted for ADA website accessibility lawsuits. In 2023, over 4,000 companies faced lawsuits averaging $60,000-$225,000 in total costs.

The good news: proactive compliance is far more cost-effective than reactive defense, and accessibility improvements often enhance the experience for all your customers.

I'd like to offer {company} a complimentary preliminary accessibility assessment to help you:

✓ Identify potential compliance gaps
✓ Understand your risk exposure level
✓ Receive a prioritized remediation roadmap
✓ Learn about ongoing compliance strategies

This assessment typically takes 48 hours and includes a detailed report with actionable recommendations.

Would you be open to a brief 15-minute call next week to discuss this?

Best regards,
[Your Name]"""
    },
    "Follow-Up Email (Value-Focused)": {
        "subject_lines": [
            "Re: ADA Compliance Risk Assessment for {company}",
            "How accessible websites drive 23% better conversions",
            "Following up: {company} website accessibility"
        ],
        "body": """Hi {first_name},

I wanted to follow up on my previous email about ADA website accessibility for {company}.

I understand that compliance initiatives can sometimes feel like "check-box" exercises, but I wanted to share how accessibility directly impacts business metrics our clients care about:

**Real Results from Pet E-commerce Clients:**
• 23% reduction in bounce rates
• 15% increase in mobile conversions
• 18% improvement in organic search traffic
• 50% fewer customer service inquiries about navigation

Beyond legal protection, accessibility is fundamentally about removing friction from your customer experience.

I'd love to show you some specific examples relevant to {specific_feature}.

Are you available for a quick 15-minute call this week?

Best regards,
[Your Name]"""
    },
    "Senior Executive Outreach": {
        "subject_lines": [
            "{company}'s Competitive Advantage in Inclusive Commerce",
            "Strategic accessibility opportunity for {company}",
            "Expanding {company}'s market reach by 26%"
        ],
        "body": """Hi {first_name},

As {title} at {company}, you've built an impressive brand in the pet products space. I'm reaching out with an opportunity to strengthen your competitive position while mitigating legal risk.

**The Situation:**
E-commerce accessibility lawsuits have increased 300% in recent years, with pet industry companies increasingly targeted. Simultaneously, the 61 million Americans with disabilities represent a $490B market largely underserved by online retailers.

**The Opportunity:**
Leading brands are turning ADA compliance from a legal obligation into a competitive advantage through:
• Enhanced customer experience for all users (15-30% conversion improvements)
• Expanded addressable market (26% of U.S. adults have disabilities)
• Strengthened brand reputation and CSR positioning
• Legal risk mitigation (avg. lawsuit cost: $150K+)

**The Ask:**
I'd like to offer {company} a complimentary strategic accessibility assessment - not just a technical audit, but a business-focused analysis of opportunities and risks specific to your market position.

Would you be open to a brief conversation about how accessibility can support {company}'s growth objectives?

Best regards,
[Your Name]"""
    },
    "Specialty/Niche Brand Outreach": {
        "subject_lines": [
            "Aligning {company}'s Values with Accessible Commerce",
            "Inclusivity + {business_type}: Natural fit for {company}",
            "Expanding {company}'s conscious consumer reach"
        ],
        "body": """Hi {first_name},

I've been following {company}'s journey in the {business_type} space, and I'm impressed by your brand's commitment to quality and values.

I'm reaching out because there's a natural alignment between your brand values and digital accessibility. Companies focused on premium products and conscious consumption are increasingly recognizing that inclusivity - ensuring everyone can access your products - is part of that commitment.

Beyond values alignment, accessibility offers practical benefits for brands like yours:

• Reach conscious consumers who value inclusive brands (75% preference)
• Enhance premium positioning through superior user experience
• Protect brand reputation from accessibility lawsuits (increasing in pet space)
• Support aging pet owners (largest customer demographic)

I'd love to explore how {company} could integrate accessibility into your brand story and customer experience.

Open to a brief call next week?

Best regards,
[Your Name]"""
    },
    "Subscription Service Specific": {
        "subject_lines": [
            "Improving {company}'s Subscription Experience Through Accessibility",
            "Reducing churn at {company} through better UX",
            "Subscription optimization for {company}"
        ],
        "body": """Hi {first_name},

Subscription services like {company} live and die by customer experience and retention rates. I'm reaching out because there's a critical element many subscription brands overlook: accessibility.

**The Subscription Accessibility Challenge:**

Your signup flow, account management, and modification process need to work flawlessly for all users. Accessibility barriers directly impact:

• Signup conversion rates (lost customers before they even start)
• Subscription management (frustrated customers cancel)
• Customer lifetime value (poor experience = higher churn)
• Senior market penetration (highest pet ownership + highest disability rates)

**The Opportunity:**

Subscription brands that prioritize accessibility see:
• 15-25% improvement in signup completion rates
• 30% reduction in "can't figure out how to..." support tickets
• Higher retention among 55+ demographic (fastest-growing pet owner segment)
• Competitive differentiation in crowded subscription market

I'd like to offer {company} a focused audit of your subscription user flows - the specific journeys that drive your revenue.

Would you be open to a brief discussion about optimizing these critical paths?

Best regards,
[Your Name]"""
    },
    "Healthcare/Pharmacy Specific": {
        "subject_lines": [
            "Healthcare Accessibility Compliance for {company}",
            "Dual compliance: FDA + ADA for {company}",
            "Protecting {company} from healthcare accessibility lawsuits"
        ],
        "body": """Hi {first_name},

As an online pet pharmacy/healthcare provider, {company} operates in a unique compliance environment. I'm reaching out because healthcare-related e-commerce faces heightened ADA scrutiny.

**Why Healthcare E-commerce Is Different:**

• OCR (Office for Civil Rights) enforces both HIPAA and accessibility
• Healthcare accessibility lawsuits see higher settlement amounts
• Prescription management must be accessible to all (legal requirement)
• Medical information must meet Section 508 standards
• Dual compliance (FDA + ADA) creates complex requirements

**Critical Healthcare Accessibility Elements:**

✓ Prescription upload and management interfaces
✓ Medical information and dosing instructions
✓ Patient portal accessibility
✓ Telehealth/consultation features (video, chat)
✓ Insurance and payment systems
✓ Appointment booking and records access

**The Stakes:**
Healthcare accessibility lawsuits average 2x higher settlements than general e-commerce, and regulatory agencies are increasing digital health scrutiny.

I specialize in healthcare e-commerce accessibility and would like to offer {company} a compliance-focused assessment.

Available for a call this week?

Best regards,
[Your Name]"""
    }
}

# Messaging frameworks
MESSAGING_FRAMEWORKS = {
    "Risk Mitigation (Legal/Compliance)": {
        "core_message": "Protect your business from costly ADA lawsuits and legal liability",
        "key_points": [
            "ADA lawsuits against e-commerce sites increased 300% in recent years",
            "Average lawsuit costs $110,000-$225,000 (settlement + legal fees)",
            "Pet industry companies increasingly targeted (online-only, visible brands)",
            "Proactive compliance is 90% cheaper than reactive defense",
            "Documentation and audit trails critical for legal defense"
        ],
        "statistics": [
            "4,000+ ADA website lawsuits filed in 2023",
            "Retailers are #1 target industry for ADA litigation",
            "E-commerce companies 5x more likely to be sued than brick-and-mortar",
            "70% of settlements could have been prevented with proactive compliance"
        ],
        "cta": "Let us conduct a free preliminary audit to identify your exposure areas"
    },
    "Market Expansion (Marketing/E-commerce)": {
        "core_message": "Reach 61 million more potential customers and increase conversions",
        "key_points": [
            "26% of U.S. adults have a disability (61 million people)",
            "Disability market has $490 billion in disposable income",
            "Accessible websites see 15-30% improvement in overall usability",
            "Better UX leads to higher conversion rates for ALL users",
            "Seniors (highest pet ownership rates) benefit most from accessibility"
        ],
        "statistics": [
            "71% of users with disabilities will leave a non-accessible website immediately",
            "Accessible websites see 50% lower bounce rates",
            "67% of seniors have vision impairments affecting web use",
            "Mobile accessibility issues affect 85% of sites"
        ],
        "cta": "Let's discuss how accessibility can expand your addressable market"
    },
    "Competitive Advantage (Executives/Brand)": {
        "core_message": "Lead your industry with inclusive, best-in-class customer experience",
        "key_points": [
            "Differentiate from competitors through inclusive design",
            "Enhance brand reputation and customer loyalty",
            "Demonstrate corporate social responsibility",
            "Attract socially-conscious consumers (especially Gen Z/Millennials)",
            "Industry leadership positioning"
        ],
        "statistics": [
            "75% of consumers prefer to buy from socially responsible companies",
            "Accessible brands see 28% higher customer loyalty scores",
            "92% of consumers have more favorable view of brands supporting social causes",
            "Companies with strong CSR see 20% higher employee satisfaction"
        ],
        "cta": "Position your brand as an industry leader in accessibility and inclusion"
    },
    "SEO & Technical Excellence (CTO/Technical)": {
        "core_message": "Improve search rankings, site performance, and technical quality",
        "key_points": [
            "Accessibility improvements align with Google's Core Web Vitals",
            "Semantic HTML and ARIA labels improve search indexing",
            "Accessible sites load 30% faster on average",
            "Mobile accessibility critical for Google's mobile-first indexing",
            "Technical SEO benefits from structured, accessible code"
        ],
        "statistics": [
            "Accessible websites rank 12% higher in search results",
            "53% of mobile users abandon sites that take >3 seconds to load",
            "Google prioritizes accessible, well-structured content",
            "Accessible sites have 50% better mobile performance scores"
        ],
        "cta": "Let's audit your site's technical accessibility and SEO opportunities"
    }
}

# Objection handling
OBJECTIONS = {
    "We're already WCAG compliant / We have an accessibility overlay": {
        "response": "That's great that you've already started thinking about accessibility. Many companies are surprised to learn that overlay solutions (like accessiBe, UserWay) don't provide complete legal protection - in fact, some have generated additional lawsuits. WCAG compliance also requires ongoing monitoring and testing, not just a one-time fix. I'd be happy to provide a second opinion audit to verify your current coverage and identify any gaps. Would that be valuable?",
        "key_points": [
            "Overlay solutions are controversial and don't prevent lawsuits",
            "WCAG compliance requires manual testing, not just automated tools",
            "Ongoing monitoring is essential (sites change constantly)",
            "Second opinion audits often find gaps in existing solutions"
        ]
    },
    "We've never been sued, so it's not a priority": {
        "response": "I appreciate that perspective, and you're right that many companies haven't faced lawsuits yet. However, the data shows that ADA website lawsuits are increasing exponentially - they've grown 300% in the past 5 years. The challenge is that these lawsuits are often filed in bulk by plaintiff law firms targeting entire industries. Once your sector is in their sights, multiple companies get hit simultaneously. The companies that prepared proactively spend $5,000-$15,000 on compliance, while those that waited spend $150,000+ on legal defense and settlements. Would you be open to understanding your specific risk profile?",
        "key_points": [
            "Lawsuits are increasing and often target industries in waves",
            "Proactive compliance is 10-15x cheaper than reactive defense",
            "Business benefits beyond legal protection",
            "Risk assessment helps quantify exposure"
        ]
    },
    "This seems expensive / We don't have budget for this": {
        "response": "I understand budget constraints are real. Let me put this in perspective: the average ADA lawsuit settlement is $60,000-$75,000, plus $50,000-$150,000 in legal fees - that's $110,000-$225,000 total. Our compliance program typically ranges from $5,000-$25,000 depending on site complexity, with ongoing monitoring at $500-$2,000/month. So you're looking at roughly 5-10% of the cost of a single lawsuit, with the added benefit of improved conversion rates that often offset the investment within 6-12 months. Would it be helpful to review some flexible options?",
        "key_points": [
            "Compliance costs 5-10% of lawsuit costs",
            "ROI from conversion improvements often pays for itself",
            "Phased implementation options available",
            "Insurance may cover or offer discounts for compliance"
        ]
    },
    "We're planning a website redesign soon, so let's wait": {
        "response": "A redesign is actually the perfect time to integrate accessibility from the ground up - it's much easier and less expensive than retrofitting later. However, waiting until the redesign means you're exposed to legal risk during the interim period, which could be 6-18 months. Also, if accessibility isn't scoped into your redesign from the beginning, it becomes an expensive add-on later. I'd recommend quick high-priority fixes now to reduce immediate risk, and partner with your redesign team to ensure accessibility is built in from the start. Would you like to discuss how we can work with your redesign timeline?",
        "key_points": [
            "Redesigns are ideal opportunities for accessibility",
            "Waiting creates ongoing legal exposure",
            "Building in accessibility is cheaper than retrofitting",
            "Can work alongside redesign team"
        ]
    },
    "Our customers haven't complained about accessibility": {
        "response": "That's a really common assumption, and it highlights an important reality: customers with disabilities typically don't complain - they just leave. Research shows 71% of users with disabilities will immediately leave an inaccessible website without reaching out. They've learned that most companies won't fix the issues, so they don't waste time complaining. This means you're likely losing customers and revenue without realizing it. Would you be interested in seeing data on how accessibility improvements impact overall conversion rates?",
        "key_points": [
            "Customers with disabilities leave rather than complain (71%)",
            "Lost revenue invisible in analytics",
            "Accessibility improvements benefit all users",
            "Conversion rate improvements measurable"
        ]
    },
    "We're a small company, they won't sue us": {
        "response": "I understand that logic, but unfortunately the data shows the opposite. Plaintiff firms actually prefer suing smaller companies because: 1) They're more likely to settle quickly rather than fight expensive litigation, 2) They often lack legal resources to mount strong defenses, and 3) They're less likely to have insurance or legal teams. We have scaled solutions specifically designed for small businesses that provide strong legal protection without enterprise-level costs. Would you like to see some options designed for companies your size?",
        "key_points": [
            "Small companies are actually preferred targets",
            "Quicker to settle, fewer resources to defend",
            "Compliance is more affordable for smaller sites",
            "Scaled solutions available"
        ]
    }
}

# Main application
def main():
    # Sidebar
    st.sidebar.title("🎯 ADA Sales Navigator")
    
    # Navigation
    page = st.sidebar.radio(
        "Navigation",
        ["📊 Lead Dashboard", "🔍 Lead Details", "✉️ Email Generator", 
         "💬 Talking Points", "📈 Pipeline Tracker", "📚 Knowledge Base"]
    )
    
    # Load data
    leads_df = load_leads()
    
    if leads_df.empty:
        st.error("No leads data available. Please check the CSV file.")
        return
    
    # Display selected page
    if page == "📊 Lead Dashboard":
        show_dashboard(leads_df)
    elif page == "🔍 Lead Details":
        show_lead_details(leads_df)
    elif page == "✉️ Email Generator":
        show_email_generator(leads_df)
    elif page == "💬 Talking Points":
        show_talking_points()
    elif page == "📈 Pipeline Tracker":
        show_pipeline_tracker(leads_df)
    elif page == "📚 Knowledge Base":
        show_knowledge_base()

def show_dashboard(leads_df):
    """Display the main dashboard with lead overview"""
    # Beautiful header
    st.markdown("""
        <div class="main-header">
            <h1>📊 Lead Dashboard</h1>
            <p>Manage your 100+ pet e-commerce prospects</p>
        </div>
    """, unsafe_allow_html=True)

    # Filters
    col1, col2, col3 = st.columns(3)

    with col1:
        business_types = ["All"] + sorted(leads_df['Business Type'].unique().tolist())
        selected_type = st.selectbox("Filter by Business Type", business_types)

    with col2:
        status_options = ["All", "Not Contacted", "Contacted", "Replied", "Meeting Scheduled", "Proposal Sent", "Closed Won", "Closed Lost"]
        selected_status = st.selectbox("Filter by Status", status_options)

    with col3:
        search_term = st.text_input("🔍 Search Company", "")

    # Apply filters
    filtered_df = leads_df.copy()
    if selected_type != "All":
        filtered_df = filtered_df[filtered_df['Business Type'] == selected_type]
    if search_term:
        filtered_df = filtered_df[filtered_df['Company Name'].str.contains(search_term, case=False, na=False)]

    # Add status column from session state
    filtered_df['Status'] = filtered_df['Company Name'].apply(
        lambda x: st.session_state.status_data.get(x, {}).get('status', 'Not Contacted')
    )

    if selected_status != "All":
        filtered_df = filtered_df[filtered_df['Status'] == selected_status]

    # Summary metrics
    st.subheader("📈 Summary")
    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)

    total_leads = len(filtered_df)
    contacted = len([x for x in filtered_df['Company Name'] if st.session_state.status_data.get(x, {}).get('status') in ['Contacted', 'Replied', 'Meeting Scheduled', 'Proposal Sent', 'Closed Won']])
    meetings = len([x for x in filtered_df['Company Name'] if st.session_state.status_data.get(x, {}).get('status') in ['Meeting Scheduled', 'Proposal Sent', 'Closed Won']])
    closed = len([x for x in filtered_df['Company Name'] if st.session_state.status_data.get(x, {}).get('status') == 'Closed Won'])
    initial_sent = len([x for x in filtered_df['Company Name'] if st.session_state.status_data.get(x, {}).get('initial_message_sent', False)])
    followup_sent = len([x for x in filtered_df['Company Name'] if st.session_state.status_data.get(x, {}).get('followup_sent', False)])
    email_contacted = len([x for x in filtered_df['Company Name'] if st.session_state.status_data.get(x, {}).get('email_contacted', False)])
    linkedin_contacted = len([x for x in filtered_df['Company Name'] if st.session_state.status_data.get(x, {}).get('linkedin_contacted', False)])

    col1.metric("Total", total_leads)
    col2.metric("Contacted", contacted)
    col3.metric("Initial", initial_sent)
    col4.metric("Follow-ups", followup_sent)
    col5.metric("📧 Email", email_contacted)
    col6.metric("💼 LinkedIn", linkedin_contacted)
    col7.metric("Meetings", meetings)
    col8.metric("Won", closed)

    # Display leads table with interactive checkboxes
    st.subheader("🎯 Leads")
    st.write("*Use checkboxes to track outreach progress and click 'Generate Email' for quick message creation*")

    # Display each lead with checkboxes and actions
    for idx, row in filtered_df.iterrows():
        company_name = row['Company Name']

        # Get current checkbox states
        current_data = st.session_state.status_data.get(company_name, {})
        initial_sent = current_data.get('initial_message_sent', False)
        followup_sent = current_data.get('followup_sent', False)
        linkedin_url = row.get('Primary Contact LinkedIn', '')

        # Create expander for each lead
        with st.expander(f"**#{row['#']}** - {company_name} ({row['Business Type']}) - Status: {row['Status']}"):
            col1, col2 = st.columns([2, 1])

            with col1:
                st.write(f"**Website:** [{row['Website']}](https://{row['Website']})")
                st.write(f"**Primary Contact:** {row['Primary Contact Role']}")
                st.write(f"**Business Type:** {row['Business Type']}")
                if linkedin_url:
                    st.write(f"**LinkedIn:** [View Profile]({linkedin_url})")

            with col2:
                # Checkboxes for workflow tracking
                new_initial = st.checkbox(
                    "✉️ Initial Message Sent",
                    value=initial_sent,
                    key=f"initial_{company_name}"
                )
                new_followup = st.checkbox(
                    "📨 Follow-up Sent",
                    value=followup_sent,
                    key=f"followup_{company_name}"
                )

                # Get additional tracking states
                email_contacted = current_data.get('email_contacted', False)
                linkedin_contacted = current_data.get('linkedin_contacted', False)

                new_email = st.checkbox(
                    "📧 Contacted via Email",
                    value=email_contacted,
                    key=f"email_{company_name}"
                )
                new_linkedin = st.checkbox(
                    "💼 Contacted via LinkedIn",
                    value=linkedin_contacted,
                    key=f"linkedin_{company_name}"
                )

            # Update status if checkboxes changed
            if new_initial != initial_sent or new_followup != followup_sent or new_email != email_contacted or new_linkedin != linkedin_contacted:
                if company_name not in st.session_state.status_data:
                    st.session_state.status_data[company_name] = {}
                st.session_state.status_data[company_name]['initial_message_sent'] = new_initial
                st.session_state.status_data[company_name]['followup_sent'] = new_followup
                st.session_state.status_data[company_name]['email_contacted'] = new_email
                st.session_state.status_data[company_name]['linkedin_contacted'] = new_linkedin
                save_status(st.session_state.status_data)

            # Message Templates - Always visible
            if True:
                st.markdown("---")
                st.markdown("### 📧 Message Templates")

                # Determine specific feature
                specific_features = {
                    'Subscription Service': "subscription signup flow",
                    'Online Pharmacy': "prescription management system",
                    'Pet Insurance': "policy comparison and claims portal",
                    'Specialty': "product filtering and checkout",
                    'Retailer': "product search and filtering",
                    'Marketplace': "booking and payment flow"
                }
                specific_feature = "website"
                for key, value in specific_features.items():
                    if key.lower() in row['Business Type'].lower():
                        specific_feature = value
                        break

                # Create two columns for both templates
                col_email, col_linkedin = st.columns([1.2, 1])

                # LEFT COLUMN: DETAILED EMAIL
                with col_email:
                    st.markdown("#### 📧 Detailed Email")

                    subject_line = f"ADA Compliance for {company_name} - Mitigating Risk"

                    email_body = f"""Hi [First Name],

I noticed {company_name}'s impressive presence in the {row['Business Type'].lower()} space. I wanted to reach out regarding a critical compliance issue affecting many pet e-commerce companies.

**The Challenge:**
Your {specific_feature} may have accessibility barriers that violate ADA Title III. With pet industry lawsuits increasing 320% since 2020, companies like {company_name} are prime targets.

**What We've Seen:**
• {row['Key Pain Points']}
• Risk of lawsuits ($20K-$75K+ in settlements)
• Potential brand damage and customer loss

**Our Solution:**
We provide comprehensive ADA compliance audits and remediation for pet e-commerce platforms. We've helped companies like yours:
✓ Achieve WCAG 2.1 AA compliance
✓ Protect against lawsuits
✓ Expand market reach by 15-20%
✓ Improve SEO and user experience

**Next Steps:**
I'd love to offer a complimentary accessibility audit of your {specific_feature}. This 30-minute assessment will identify specific risks and provide actionable recommendations.

Are you available for a brief call next week?

Best regards,
[Your Name]
ADA Compliance Specialist
[Your Email] | [Your Phone]

P.S. We work with 50+ pet brands and understand the unique challenges in your industry."""

                    st.markdown("**📬 Subject:**")
                    st.info(subject_line)

                    st.markdown("**📄 Body:**")
                    email_final = st.text_area(
                        "Edit as needed:",
                        value=email_body,
                        height=350,
                        key=f"email_body_{company_name}",
                        label_visibility="collapsed"
                    )

                    # Email action buttons
                    email_btn1, email_btn2 = st.columns(2)
                    with email_btn1:
                        if st.button("📋 Copy Email", key=f"copy_email_{company_name}", use_container_width=True):
                            st.code(email_final, language=None)
                            st.success("✅ Copy text above!")
                    with email_btn2:
                        if st.button("✅ Mark Email Sent", key=f"mark_email_{company_name}", use_container_width=True):
                            if company_name not in st.session_state.status_data:
                                st.session_state.status_data[company_name] = {}
                            st.session_state.status_data[company_name]['status'] = 'Contacted'
                            st.session_state.status_data[company_name]['last_contact'] = datetime.now().strftime('%Y-%m-%d')
                            st.session_state.status_data[company_name]['initial_message_sent'] = True
                            st.session_state.status_data[company_name]['email_contacted'] = True
                            save_status(st.session_state.status_data)
                            st.success("✅ Updated!")
                            st.rerun()

                # RIGHT COLUMN: LINKEDIN MESSAGE
                with col_linkedin:
                    st.markdown("#### 💼 LinkedIn Message")

                    contact_role = row['Primary Contact Role']
                    # Shorten role if too long
                    if len(contact_role) > 25:
                        role_display = contact_role.split()[0]
                    else:
                        role_display = contact_role

                    linkedin_msg = f"Hi [Name], congrats on {role_display} at {company_name}! Have you chosen an accessibility provider? We're a VC-backed startup achieving 100% ADA compliance fast & maintaining it forever. Quick chat?"

                    char_count = len(linkedin_msg)

                    if char_count > 300:
                        st.warning(f"⚠️ {char_count}/300 chars")
                    else:
                        st.success(f"✅ {char_count}/300 chars")

                    linkedin_final = st.text_area(
                        "Edit (replace [Name]):",
                        value=linkedin_msg,
                        height=150,
                        key=f"linkedin_body_{company_name}",
                        max_chars=300
                    )

                    # LinkedIn action buttons
                    li_btn1, li_btn2 = st.columns(2)
                    with li_btn1:
                        if st.button("📋 Copy LinkedIn", key=f"copy_li_{company_name}", use_container_width=True):
                            st.code(linkedin_final, language=None)
                            st.success("✅ Copy text above!")
                    with li_btn2:
                        if st.button("✅ Mark LI Sent", key=f"mark_li_{company_name}", use_container_width=True):
                            if company_name not in st.session_state.status_data:
                                st.session_state.status_data[company_name] = {}
                            st.session_state.status_data[company_name]['status'] = 'Contacted'
                            st.session_state.status_data[company_name]['last_contact'] = datetime.now().strftime('%Y-%m-%d')
                            st.session_state.status_data[company_name]['initial_message_sent'] = True
                            st.session_state.status_data[company_name]['linkedin_contacted'] = True
                            save_status(st.session_state.status_data)
                            st.success("✅ Updated!")
                            st.rerun()

                    if linkedin_url:
                        st.markdown("---")
                        if st.button("🔗 Open LinkedIn Profile", key=f"open_linkedin_{company_name}", use_container_width=True, type="secondary"):
                            st.markdown(f"[Click here to open]({linkedin_url})")
                            st.info("👆 Click the link above")

    # Quick actions section (keeping for backward compatibility)
    st.markdown("---")
    st.subheader("⚡ Quick Actions")
    selected_company = st.selectbox("Select a company for quick action", filtered_df['Company Name'].tolist())

    col1, col2, col3 = st.columns(3)
    if col1.button("📧 Generate Email", key="quick_email"):
        st.session_state.selected_company = selected_company
        st.session_state.page = "✉️ Email Generator"
        st.rerun()
    if col2.button("📋 View Details"):
        st.session_state.selected_company = selected_company
        st.session_state.page = "🔍 Lead Details"
        st.rerun()
    if col3.button("💬 Get Talking Points"):
        st.session_state.selected_company = selected_company
        st.session_state.page = "💬 Talking Points"
        st.rerun()

def show_lead_details(leads_df):
    """Show detailed information about a specific lead"""
    # Beautiful header
    st.markdown("""
        <div class="main-header">
            <h1>🔍 Lead Details</h1>
            <p>Deep dive into company information and tracking</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Company selection
    if 'selected_company' in st.session_state:
        default_idx = int(leads_df[leads_df['Company Name'] == st.session_state.selected_company].index[0])
    else:
        default_idx = 0

    selected_company = st.selectbox(
        "Select Company",
        leads_df['Company Name'].tolist(),
        index=default_idx
    )

    # Get company data
    company_data = leads_df[leads_df['Company Name'] == selected_company].iloc[0]
    
    # Display company information
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader(f"🏢 {company_data['Company Name']}")
        st.write(f"**Website:** [{company_data['Website']}](https://{company_data['Website']})")
        st.write(f"**Business Type:** {company_data['Business Type']}")
        
        st.markdown("---")
        
        st.write("**Primary Contact Role:** " + company_data['Primary Contact Role'])
        st.write("**Secondary Contact Role:** " + company_data['Secondary Contact Role'])
        
        st.markdown("---")
        
        st.write("**Messaging Focus:**")
        st.info(company_data['Messaging Focus'])
        
        st.write("**Key Pain Points:**")
        st.warning(company_data['Key Pain Points'])
    
    with col2:
        st.subheader("📊 Lead Status")
        
        # Get current status
        current_status = st.session_state.status_data.get(selected_company, {}).get('status', 'Not Contacted')
        
        # Status selector
        new_status = st.selectbox(
            "Status",
            ["Not Contacted", "Contacted", "Replied", "Meeting Scheduled", "Proposal Sent", "Closed Won", "Closed Lost"],
            index=["Not Contacted", "Contacted", "Replied", "Meeting Scheduled", "Proposal Sent", "Closed Won", "Closed Lost"].index(current_status)
        )
        
        # Last contact date
        current_date = st.session_state.status_data.get(selected_company, {}).get('last_contact', '')
        last_contact = st.date_input("Last Contact", value=datetime.strptime(current_date, '%Y-%m-%d') if current_date else None)
        
        # Next follow-up
        current_followup = st.session_state.status_data.get(selected_company, {}).get('next_followup', '')
        next_followup = st.date_input("Next Follow-up", value=datetime.strptime(current_followup, '%Y-%m-%d') if current_followup else None)
        
        # Notes
        current_notes = st.session_state.status_data.get(selected_company, {}).get('notes', '')
        notes = st.text_area("Notes", value=current_notes, height=150)
        
        # Save button
        if st.button("💾 Save Status", type="primary"):
            st.session_state.status_data[selected_company] = {
                'status': new_status,
                'last_contact': last_contact.strftime('%Y-%m-%d') if last_contact else '',
                'next_followup': next_followup.strftime('%Y-%m-%d') if next_followup else '',
                'notes': notes
            }
            save_status(st.session_state.status_data)
            st.success("✅ Status saved!")
    
    # Action buttons
    st.markdown("---")
    st.subheader("⚡ Actions")
    
    col1, col2, col3 = st.columns(3)
    
    if col1.button("📧 Generate Email"):
        st.session_state.selected_company = selected_company
        st.session_state.page = "✉️ Email Generator"
        st.rerun()
    
    if col2.button("💬 Get Talking Points"):
        st.session_state.selected_company = selected_company
        st.session_state.page = "💬 Talking Points"
        st.rerun()
    
    if col3.button("📊 Back to Dashboard"):
        st.rerun()

def show_email_generator(leads_df):
    """Generate customized emails based on templates"""
    # Beautiful header
    st.markdown("""
        <div class="main-header">
            <h1>✉️ Email Generator</h1>
            <p>Create personalized, professional outreach emails</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Company selection
    if 'selected_company' in st.session_state:
        default_idx = int(leads_df[leads_df['Company Name'] == st.session_state.selected_company].index[0])
    else:
        default_idx = 0

    selected_company = st.selectbox(
        "Select Company",
        leads_df['Company Name'].tolist(),
        index=default_idx
    )

    company_data = leads_df[leads_df['Company Name'] == selected_company].iloc[0]

    # Template selection
    st.subheader("📝 Select Email Template")
    
    template_name = st.selectbox(
        "Template Type",
        list(EMAIL_TEMPLATES.keys())
    )
    
    template = EMAIL_TEMPLATES[template_name]
    
    # Personalization fields
    st.subheader("✏️ Personalization")
    
    col1, col2 = st.columns(2)
    
    with col1:
        first_name = st.text_input("Contact First Name", "")
        your_name = st.text_input("Your Name", "")
    
    with col2:
        title = st.text_input("Contact Title", company_data['Primary Contact Role'])
        your_title = st.text_input("Your Title", "")
    
    # Generate subject lines
    st.markdown("---")
    st.subheader("📬 Subject Line Options")
    st.write("*Choose one of these subject lines for your email:*")

    subject_lines = [
        subj.format(
            company=company_data['Company Name'],
            business_type=company_data['Business Type'].lower()
        )
        for subj in template['subject_lines']
    ]

    for i, subject in enumerate(subject_lines, 1):
        st.info(f"**Option {i}:** {subject}")

    # Generate email body
    st.markdown("---")
    st.subheader("📄 Generated Email Message")
    st.write("*Edit the email below as needed, then copy it:*")
    
    # Determine specific feature based on business type
    specific_features = {
        'Subscription Service': "subscription signup flow",
        'Online Pharmacy': "prescription management system",
        'Pet Insurance': "policy comparison and claims portal",
        'Specialty': "product filtering and checkout",
        'Retailer': "product search and filtering",
        'Marketplace': "booking and payment flow"
    }
    
    specific_feature = "website navigation"
    for key, value in specific_features.items():
        if key.lower() in company_data['Business Type'].lower():
            specific_feature = value
            break
    
    # Format email body
    email_body = template['body'].format(
        first_name=first_name if first_name else "[First Name]",
        company=company_data['Company Name'],
        title=title,
        business_type=company_data['Business Type'].lower(),
        specific_feature=specific_feature
    )
    
    # Replace [Your Name] with actual name
    email_body = email_body.replace("[Your Name]", your_name if your_name else "[Your Name]")
    email_body = email_body.replace("[Your Title]", your_title if your_title else "[Your Title]")
    
    # Editable text area with prominent display
    final_email = st.text_area(
        "✍️ Your Email (Edit as needed):",
        value=email_body,
        height=400,
        help="This is your generated email. You can edit it directly in this box."
    )

    # Action buttons
    st.markdown("---")
    st.subheader("⚡ Actions")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📋 Copy Email", type="primary", use_container_width=True):
            st.success("✅ Email is ready to copy from the box above!")
            st.info("💡 **Tip:** Select all text in the email box above and press Ctrl+C (or Cmd+C on Mac)")

    with col2:
        if st.button("💾 Mark as Contacted", use_container_width=True):
            if selected_company not in st.session_state.status_data:
                st.session_state.status_data[selected_company] = {}
            st.session_state.status_data[selected_company]['status'] = 'Contacted'
            st.session_state.status_data[selected_company]['last_contact'] = datetime.now().strftime('%Y-%m-%d')
            st.session_state.status_data[selected_company]['initial_message_sent'] = True
            save_status(st.session_state.status_data)
            st.success("✅ Status updated to Contacted!")

    with col3:
        if st.button("🔄 Start Over", use_container_width=True):
            st.rerun()

    # Display final email in a code block for easy copying
    st.markdown("---")
    st.subheader("📋 Copy-Ready Format")
    st.code(final_email, language=None)
    st.caption("👆 Click the copy icon in the top-right of the box above to copy the entire email")

def show_talking_points():
    """Display messaging frameworks and talking points"""
    # Beautiful header
    st.markdown("""
        <div class="main-header">
            <h1>💬 Talking Points & Messaging</h1>
            <p>Master your sales conversations with proven frameworks</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Select company context
    if 'selected_company' in st.session_state:
        st.info(f"📍 Context: {st.session_state.selected_company}")
    
    # Messaging frameworks
    st.subheader("🎯 Messaging Frameworks")
    st.write("Choose the right messaging approach based on your contact's role and priorities:")
    
    framework_name = st.selectbox(
        "Select Framework",
        list(MESSAGING_FRAMEWORKS.keys())
    )
    
    framework = MESSAGING_FRAMEWORKS[framework_name]
    
    # Display framework
    st.markdown(f"### {framework_name}")
    
    st.markdown("**Core Message:**")
    st.success(framework['core_message'])
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Key Points:**")
        for point in framework['key_points']:
            st.markdown(f"• {point}")
    
    with col2:
        st.markdown("**Supporting Statistics:**")
        for stat in framework['statistics']:
            st.markdown(f"• {stat}")
    
    st.markdown("**Call to Action:**")
    st.info(framework['cta'])
    
    st.markdown("---")
    
    # Objection handling
    st.subheader("🛡️ Objection Handling")
    st.write("Prepare for common objections with these proven responses:")
    
    objection = st.selectbox(
        "Select Objection",
        list(OBJECTIONS.keys())
    )
    
    obj_data = OBJECTIONS[objection]
    
    st.markdown(f"**Objection:** *\"{objection}\"*")
    
    st.markdown("**Response:**")
    st.write(obj_data['response'])
    
    st.markdown("**Key Points to Emphasize:**")
    for point in obj_data['key_points']:
        st.markdown(f"• {point}")
    
    st.markdown("---")
    
    # Quick reference stats
    st.subheader("📊 Quick Reference Statistics")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Americans with Disabilities", "61 million", "26% of population")
        st.metric("Disability Market Value", "$490B", "disposable income")
    
    with col2:
        st.metric("ADA Lawsuit Increase", "300%", "2017-2022")
        st.metric("Average Lawsuit Cost", "$150K", "settlement + legal")
    
    with col3:
        st.metric("Users Who Leave", "71%", "if site inaccessible")
        st.metric("Conversion Improvement", "15-30%", "with accessibility")

def show_pipeline_tracker(leads_df):
    """Track sales pipeline and follow-ups"""
    # Beautiful header
    st.markdown("""
        <div class="main-header">
            <h1>📈 Pipeline Tracker</h1>
            <p>Monitor your progress and manage follow-ups</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Status breakdown
    st.subheader("📊 Pipeline Overview")
    
    status_counts = {}
    for company in leads_df['Company Name']:
        status = st.session_state.status_data.get(company, {}).get('status', 'Not Contacted')
        status_counts[status] = status_counts.get(status, 0) + 1
    
    col1, col2, col3, col4 = st.columns(4)
    
    col1.metric("Not Contacted", status_counts.get('Not Contacted', 0))
    col1.metric("Contacted", status_counts.get('Contacted', 0))
    
    col2.metric("Replied", status_counts.get('Replied', 0))
    col2.metric("Meeting Scheduled", status_counts.get('Meeting Scheduled', 0))
    
    col3.metric("Proposal Sent", status_counts.get('Proposal Sent', 0))
    col3.metric("Closed Won", status_counts.get('Closed Won', 0))
    
    col4.metric("Closed Lost", status_counts.get('Closed Lost', 0))
    total_active = sum(status_counts.get(s, 0) for s in ['Contacted', 'Replied', 'Meeting Scheduled', 'Proposal Sent'])
    col4.metric("Active Leads", total_active)
    
    # Follow-ups needed
    st.subheader("⏰ Follow-ups Needed")
    
    today = datetime.now().date()
    followup_leads = []
    
    for company in leads_df['Company Name']:
        company_status = st.session_state.status_data.get(company, {})
        next_followup = company_status.get('next_followup')
        if next_followup:
            followup_date = datetime.strptime(next_followup, '%Y-%m-%d').date()
            if followup_date <= today + timedelta(days=7):  # Next 7 days
                company_data = leads_df[leads_df['Company Name'] == company].iloc[0]
                days_until = (followup_date - today).days
                followup_leads.append({
                    'Company': company,
                    'Status': company_status.get('status', 'Not Contacted'),
                    'Follow-up Date': followup_date,
                    'Days Until': days_until,
                    'Website': company_data['Website']
                })
    
    if followup_leads:
        followup_df = pd.DataFrame(followup_leads)
        followup_df = followup_df.sort_values('Days Until')
        
        st.dataframe(
            followup_df,
            use_container_width=True,
            hide_index=True
        )
        
        # Quick action for follow-ups
        st.subheader("⚡ Quick Follow-up")
        selected = st.selectbox("Select company to follow up", [f['Company'] for f in followup_leads])
        
        if st.button("📧 Generate Follow-up Email"):
            st.session_state.selected_company = selected
            st.session_state.page = "✉️ Email Generator"
            st.rerun()
    else:
        st.info("No follow-ups scheduled in the next 7 days")
    
    # Recent activity
    st.subheader("📝 Recent Activity")
    
    recent_activity = []
    for company in leads_df['Company Name']:
        company_status = st.session_state.status_data.get(company, {})
        last_contact = company_status.get('last_contact')
        if last_contact:
            contact_date = datetime.strptime(last_contact, '%Y-%m-%d').date()
            days_ago = (today - contact_date).days
            if days_ago <= 30:  # Last 30 days
                recent_activity.append({
                    'Company': company,
                    'Status': company_status.get('status', 'Not Contacted'),
                    'Last Contact': contact_date,
                    'Days Ago': days_ago,
                    'Notes': company_status.get('notes', '')[:50] + '...' if len(company_status.get('notes', '')) > 50 else company_status.get('notes', '')
                })
    
    if recent_activity:
        activity_df = pd.DataFrame(recent_activity)
        activity_df = activity_df.sort_values('Last Contact', ascending=False)
        
        st.dataframe(
            activity_df,
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info("No activity in the last 30 days")

def show_knowledge_base():
    """Display comprehensive knowledge base"""
    # Beautiful header
    st.markdown("""
        <div class="main-header">
            <h1>📚 Knowledge Base</h1>
            <p>Complete sales strategy, pricing, legal cases & resources</p>
        </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["📖 Strategy Overview", "💼 Pricing Guide", "⚖️ Legal Cases", "🔧 Tools & Resources"])
    
    with tab1:
        st.header("Sales Strategy Overview")
        
        st.subheader("🎯 Target Contact Roles (by Priority)")
        
        roles = [
            ("1. CTO / VP of Technology", "High", "Technical implementation, ongoing monitoring", "Mid-to-large companies"),
            ("2. Compliance Officer", "High", "Legal protection, audit readiness", "Large companies, healthcare"),
            ("3. VP of Digital Experience", "High", "UX improvements, conversion rates", "All company sizes"),
            ("4. CMO / VP of Marketing", "Medium-High", "Brand reputation, CSR, market reach", "Brand-focused companies"),
            ("5. Head of Legal", "High", "Risk mitigation, legal strategy", "Companies with legal teams"),
            ("6. Accessibility Coordinator", "Medium", "Implementation support", "Companies investing in accessibility"),
            ("7. Product Manager", "Medium", "Product improvements, user experience", "Tech-forward companies")
        ]
        
        for role, authority, pain_points, best_for in roles:
            with st.expander(role):
                st.write(f"**Decision Authority:** {authority}")
                st.write(f"**Pain Points:** {pain_points}")
                st.write(f"**Best For:** {best_for}")
        
        st.markdown("---")
        
        st.subheader("📧 Follow-up Strategy")
        
        st.write("**6-Touch Value Drip Campaign:**")
        st.write("• **Day 0:** Initial outreach (risk or value-focused)")
        st.write("• **Day 3:** Case study relevant to their business")
        st.write("• **Day 7:** Educational content + specific insight about their site")
        st.write("• **Day 14:** Industry news/trends + urgency")
        st.write("• **Day 21:** Pivot to different messaging framework")
        st.write("• **Day 30:** Break-up email ('Should I close your file?')")
        
    with tab2:
        st.header("💼 Pricing Guide")
        
        st.subheader("Pricing by Company Size")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("### Small")
            st.write("$1M-$10M revenue")
            st.metric("Initial", "$5K-$15K")
            st.metric("Monthly", "$500-$1K")
            st.caption("Essential compliance + conversion improvements")
        
        with col2:
            st.markdown("### Medium")
            st.write("$10M-$100M revenue")
            st.metric("Initial", "$15K-$40K")
            st.metric("Monthly", "$1K-$3K")
            st.caption("Competitive advantage + risk mitigation")
        
        with col3:
            st.markdown("### Large")
            st.write("$100M+ revenue")
            st.metric("Initial", "$40K-$100K")
            st.metric("Monthly", "$3K-$10K")
            st.caption("Enterprise compliance + brand protection")
        
        st.markdown("---")
        
        st.subheader("Three-Tier Package Structure")
        
        with st.expander("Tier 1: Essential Compliance"):
            st.write("• Full WCAG 2.1 Level AA audit")
            st.write("• Priority issue remediation (high-risk items)")
            st.write("• Basic documentation for legal defense")
            st.write("• 90-day implementation support")
            st.info("**Best For:** Small companies, limited budget, immediate risk reduction")
        
        with st.expander("Tier 2: Complete Accessibility (Most Popular)"):
            st.write("• Everything in Tier 1, plus:")
            st.write("• Comprehensive remediation (all WCAG issues)")
            st.write("• User testing with people with disabilities")
            st.write("• Ongoing monitoring (quarterly audits)")
            st.write("• Training for internal teams")
            st.write("• VPAT documentation")
            st.info("**Best For:** Mid-size companies, competitive positioning")
        
        with st.expander("Tier 3: Enterprise Accessibility"):
            st.write("• Everything in Tier 2, plus:")
            st.write("• Multi-property compliance (web, mobile, kiosks)")
            st.write("• Custom accessibility governance framework")
            st.write("• Monthly monitoring and remediation")
            st.write("• Dedicated accessibility consultant")
            st.write("• Executive reporting")
            st.write("• Development/QA process integration")
            st.info("**Best For:** Large enterprises, multiple properties")
    
    with tab3:
        st.header("⚖️ Key Legal Cases")
        
        st.subheader("Important ADA Website Accessibility Cases")
        
        with st.expander("Robles v. Domino's Pizza (2019)"):
            st.write("**Ruling:** Supreme Court established that e-commerce websites must be accessible")
            st.write("**Significance:** Major precedent for website accessibility requirements")
            st.write("**Impact:** Opened floodgates for ADA website lawsuits")
            st.write("**Key Takeaway:** Websites are 'public accommodations' under ADA")
        
        with st.expander("Gil v. Winn-Dixie (2017)"):
            st.write("**Ruling:** Website accessibility required even for companies with physical stores")
            st.write("**Significance:** Clarified that digital accessibility is independent of physical locations")
            st.write("**Impact:** Can't argue 'physical store makes up for inaccessible website'")
            st.write("**Key Takeaway:** Digital and physical accessibility are both required")
        
        with st.expander("Andrews v. Blick Art Materials (2017)"):
            st.write("**Ruling:** E-commerce must meet WCAG 2.0 AA standards")
            st.write("**Significance:** Established WCAG as the compliance benchmark")
            st.write("**Impact:** Created clear technical standards for compliance")
            st.write("**Key Takeaway:** WCAG 2.0/2.1 Level AA is the legal standard")
        
        st.markdown("---")
        
        st.subheader("📊 Lawsuit Statistics")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("ADA Website Lawsuits (2023)", "4,000+")
            st.metric("Average Settlement", "$60K-$75K")
            st.metric("Average Legal Fees", "$50K-$150K")
        
        with col2:
            st.metric("Lawsuit Increase (2017-2022)", "300%")
            st.metric("Retail Lawsuits", "#1 Industry")
            st.metric("E-commerce Risk vs Physical", "5x Higher")
    
    with tab4:
        st.header("🔧 Tools & Resources")
        
        st.subheader("Contact Finding Tools")
        
        tools = [
            ("LinkedIn Sales Navigator", "Filter by company, title, seniority. Direct messaging.", "https://linkedin.com/sales"),
            ("ZoomInfo", "Email addresses, phone numbers, company technographics", "https://zoominfo.com"),
            ("Apollo.io", "Email finding, lead generation, buying signals", "https://apollo.io"),
            ("Hunter.io", "Email pattern identification and verification", "https://hunter.io"),
            ("Clearbit", "Company intelligence and contact data", "https://clearbit.com"),
            ("BuiltWith", "Technology stack identification", "https://builtwith.com"),
            ("Wappalyzer", "E-commerce platform detection", "https://wappalyzer.com")
        ]
        
        for name, description, url in tools:
            with st.expander(name):
                st.write(description)
                st.write(f"**URL:** [{url}]({url})")
        
        st.markdown("---")
        
        st.subheader("Success Metrics")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Outreach Metrics**")
            st.write("• Open Rate: 25-35%")
            st.write("• Reply Rate: 5-10%")
            st.write("• Meeting Rate: 2-5%")
            st.write("• Close Rate: 20-30%")
        
        with col2:
            st.write("**A/B Test Ideas**")
            st.write("• Risk vs. value subject lines")
            st.write("• Short vs. long email copy")
            st.write("• Statistics vs. stories")
            st.write("• Free audit vs. paid consultation")

# Run the app
if __name__ == "__main__":
    main()

