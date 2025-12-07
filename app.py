import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from collections import defaultdict
import io

st.set_page_config(page_title="Smart Financial Coach", page_icon="💰", layout="wide")

# Custom CSS for better styling
st.markdown("""
    <style>
    .big-font {
        font-size:50px !important;
        font-weight: bold;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

def detect_subscriptions(df):
    """
    AI-powered subscription detection using pattern matching.
    Detects recurring charges based on:
    - Same merchant name (fuzzy matching)
    - Similar amounts (within $1)
    - Regular intervals (~28-35 days apart)
    """
    # Convert date to datetime
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')
    
    # Group by description to find recurring patterns
    merchant_groups = defaultdict(list)
    
    for idx, row in df.iterrows():
        # Clean merchant name (remove extra words for better matching)
        merchant = row['description'].split()[0]  # Take first word as merchant identifier
        merchant_groups[merchant].append({
            'date': row['date'],
            'amount': row['amount'],
            'full_description': row['description'],
            'category': row['category']
        })
    
    subscriptions = []
    
    for merchant, transactions in merchant_groups.items():
        if len(transactions) < 2:
            continue
            
        # Sort by date
        transactions = sorted(transactions, key=lambda x: x['date'])
        
        # Check for recurring pattern
        intervals = []
        amounts = [t['amount'] for t in transactions]
        
        for i in range(len(transactions) - 1):
            interval = (transactions[i+1]['date'] - transactions[i]['date']).days
            intervals.append(interval)
        
        # Check if amounts are similar and intervals are consistent
        avg_amount = sum(amounts) / len(amounts)
        amount_variance = all(abs(amt - avg_amount) <= 1.0 for amt in amounts)
        
        if intervals:
            avg_interval = sum(intervals) / len(intervals)
            interval_consistent = all(25 <= interval <= 35 for interval in intervals)
            
            if amount_variance and interval_consistent:
                subscriptions.append({
                    'Service': transactions[0]['full_description'],
                    'Monthly Cost': f"${avg_amount:.2f}",
                    'Frequency': f"Every ~{int(avg_interval)} days",
                    'Category': transactions[0]['category'],
                    'Times Charged': len(transactions),
                    'Last Charge': transactions[-1]['date'].strftime('%Y-%m-%d'),
                    'Annual Cost': f"${(avg_amount * 12):.2f}",
                    'cost_numeric': avg_amount
                })
    
    return pd.DataFrame(subscriptions)

def main():
    # Header
    st.markdown('<p class="big-font">💰 Smart Financial Coach</p>', unsafe_allow_html=True)
    st.markdown("### AI-Powered Subscription Detector")
    st.markdown("---")
    
    # Sidebar
    with st.sidebar:
        st.header("About")
        st.info("""
        This tool uses AI pattern recognition to automatically detect 
        recurring subscriptions in your transaction history.
        
        **Features:**
        - Automatic subscription detection
        - Cost analysis and savings tracker
        - Privacy-focused (all processing done locally)
        """)
        
        st.header("How It Works")
        st.markdown("""
        1. Upload your transaction CSV
        2. AI analyzes patterns in your spending
        3. Identifies recurring charges
        4. Mark subscriptions you want to cancel
        5. See your potential savings!
        """)
    
    # File upload
    st.subheader("📁 Upload Your Transaction Data")
    uploaded_file = st.file_uploader(
        "Upload a CSV file with columns: date, description, amount, category",
        type=['csv'],
        help="Your data is processed locally and never stored"
    )
    
    # Demo data option
    col1, col2 = st.columns([3, 1])
    with col2:
        use_demo = st.button("🎯 Use Demo Data", type="secondary")
    
    if use_demo or uploaded_file is not None:
        # Load data
        if use_demo:
            df = pd.read_csv('transactions.csv')
            st.success("✅ Loaded demo data with 50 sample transactions")
        else:
            df = pd.read_csv(uploaded_file)
            st.success(f"✅ Loaded {len(df)} transactions")
        
        # Show sample of raw data
        with st.expander("View Raw Transaction Data (first 10 rows)"):
            st.dataframe(df.head(10), use_container_width=True)
        
        st.markdown("---")
        
        # Detect subscriptions
        st.subheader("🔍 AI Detection Results")
        
        with st.spinner("Analyzing transaction patterns with AI..."):
            subscriptions_df = detect_subscriptions(df)
        
        if len(subscriptions_df) > 0:
            # Metrics at the top
            col1, col2, col3 = st.columns(3)
            
            total_monthly = subscriptions_df['cost_numeric'].sum()
            total_annual = total_monthly * 12
            
            with col1:
                st.metric(
                    label="Subscriptions Detected",
                    value=len(subscriptions_df),
                    delta="Active recurring charges"
                )
            
            with col2:
                st.metric(
                    label="Total Monthly Cost",
                    value=f"${total_monthly:.2f}",
                    delta=f"${total_annual:.2f}/year"
                )
            
            with col3:
                st.metric(
                    label="Potential Annual Savings",
                    value=f"${total_annual:.2f}",
                    delta="If all canceled"
                )
            
            st.markdown("---")
            
            # Display subscriptions with cancellation tracker
            st.subheader("📋 Your Active Subscriptions")
            
            # Initialize session state for tracking cancellations
            if 'marked_for_cancellation' not in st.session_state:
                st.session_state.marked_for_cancellation = set()
            
            # Display each subscription as a card
            for idx, row in subscriptions_df.iterrows():
                col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
                
                with col1:
                    st.markdown(f"**{row['Service']}**")
                    st.caption(f"{row['Category']} • Last charged: {row['Last Charge']}")
                
                with col2:
                    st.markdown(f"**{row['Monthly Cost']}**/mo")
                    st.caption(row['Annual Cost'] + "/yr")
                
                with col3:
                    st.caption(f"Charged {row['Times Charged']}x")
                
                with col4:
                    checkbox_key = f"cancel_{idx}"
                    is_checked = st.checkbox(
                        "Want to Cancel?",
                        key=checkbox_key,
                        value=idx in st.session_state.marked_for_cancellation
                    )
                    
                    if is_checked:
                        st.session_state.marked_for_cancellation.add(idx)
                    elif idx in st.session_state.marked_for_cancellation:
                        st.session_state.marked_for_cancellation.remove(idx)
                
                st.markdown("---")
            
            # Savings calculation
            if st.session_state.marked_for_cancellation:
                st.markdown("### 💡 Your Potential Savings")
                
                marked_subscriptions = subscriptions_df.iloc[list(st.session_state.marked_for_cancellation)]
                monthly_savings = marked_subscriptions['cost_numeric'].sum()
                annual_savings = monthly_savings * 12
                
                col1, col2 = st.columns(2)
                with col1:
                    st.success(f"**Monthly Savings: ${monthly_savings:.2f}**")
                with col2:
                    st.success(f"**Annual Savings: ${annual_savings:.2f}**")
                
                st.markdown("#### Subscriptions Marked for Cancellation:")
                for idx in st.session_state.marked_for_cancellation:
                    row = subscriptions_df.iloc[idx]
                    st.markdown(f"- ❌ {row['Service']} ({row['Monthly Cost']}/month)")
            
            # Download report
            st.markdown("---")
            st.subheader("📊 Export Your Report")
            
            # Create downloadable CSV
            csv_buffer = io.StringIO()
            subscriptions_df.drop('cost_numeric', axis=1).to_csv(csv_buffer, index=False)
            
            st.download_button(
                label="⬇️ Download Subscription Report (CSV)",
                data=csv_buffer.getvalue(),
                file_name="subscriptions_report.csv",
                mime="text/csv"
            )
            
        else:
            st.info("🎉 No recurring subscriptions detected in your transaction history!")
            st.markdown("This could mean:")
            st.markdown("- You don't have any active subscriptions")
            st.markdown("- Your subscriptions haven't charged frequently enough to detect a pattern")
            st.markdown("- Try uploading more transaction history (3+ months recommended)")

if __name__ == "__main__":
    main()
