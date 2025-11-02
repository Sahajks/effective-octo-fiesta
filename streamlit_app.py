import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time

# Page config - Premium Setup
st.set_page_config(
    page_title="TrapMeme AI v6.0 - Institutional Platform",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# PREMIUM RED & YELLOW THEME
st.markdown("""
<style>
    /* Main Theme Colors */
    :root {
        --primary-red: #FF6B6B;
        --primary-yellow: #FFD93D;
        --accent-orange: #FF9A3D;
        --dark-bg: #0F0F1A;
        --card-bg: #1A1A2E;
        --text-light: #FFFFFF;
        --text-gold: #FFD700;
    }
    
    .main {
        background: linear-gradient(135deg, var(--dark-bg) 0%, #16213E 100%);
        color: var(--text-light);
    }
    
    /* Premium Header */
    .main-header {
        font-size: 3.5rem;
        background: linear-gradient(45deg, var(--primary-red), var(--primary-yellow), var(--accent-orange));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 800;
        text-shadow: 0 4px 8px rgba(255,107,107,0.3);
    }
    
    /* RED Column Styling */
    .red-column {
        background: linear-gradient(135deg, rgba(255,107,107,0.15) 0%, rgba(255,107,107,0.05) 100%);
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 5px solid var(--primary-red);
        border-right: 2px solid rgba(255,107,107,0.3);
        margin: 0.5rem;
        box-shadow: 0 8px 32px rgba(255,107,107,0.1);
    }
    
    /* YELLOW Column Styling */
    .yellow-column {
        background: linear-gradient(135deg, rgba(255,217,61,0.15) 0%, rgba(255,217,61,0.05) 100%);
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 5px solid var(--primary-yellow);
        border-right: 2px solid rgba(255,217,61,0.3);
        margin: 0.5rem;
        box-shadow: 0 8px 32px rgba(255,217,61,0.1);
    }
    
    /* Premium Cards */
    .premium-card {
        background: var(--card-bg);
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.1);
        margin: 0.5rem 0;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    }
    
    /* Buttons with Premium Theme */
    .stButton button {
        background: linear-gradient(45deg, var(--primary-red), var(--primary-yellow)) !important;
        color: var(--dark-bg) !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        padding: 0.5rem 1rem !important;
    }
    
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255,107,107,0.4) !important;
    }
    
    /* Metric Cards */
    .metric-card-red {
        background: linear-gradient(135deg, rgba(255,107,107,0.2), rgba(255,107,107,0.05));
        border-left: 4px solid var(--primary-red);
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    
    .metric-card-yellow {
        background: linear-gradient(135deg, rgba(255,217,61,0.2), rgba(255,217,61,0.05));
        border-left: 4px solid var(--primary-yellow);
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Mock live price data
def get_live_price(coin):
    prices = {
        "BTC/USDT": 43250 + np.random.randint(-100, 100),
        "ETH/USDT": 2550 + np.random.randint(-20, 20),
        "SOL/USDT": 105 + np.random.randint(-5, 5),
        "ADA/USDT": 0.52 + np.random.uniform(-0.02, 0.02),
        "XRP/USDT": 0.62 + np.random.uniform(-0.02, 0.02),
        "DOT/USDT": 7.2 + np.random.uniform(-0.2, 0.2)
    }
    return prices.get(coin, 0)

# Generate professional chart with theme colors
def generate_trading_chart(coin, price_data):
    fig = go.Figure()
    
    # Candlestick chart with theme colors
    fig.add_trace(go.Candlestick(
        x=price_data['timestamp'],
        open=price_data['open'],
        high=price_data['high'],
        low=price_data['low'],
        close=price_data['close'],
        increasing_line_color='#FFD93D',  # Yellow for up
        decreasing_line_color='#FF6B6B',  # Red for down
        name=coin
    ))
    
    # Add indicators
    fig.add_trace(go.Scatter(
        x=price_data['timestamp'],
        y=price_data['sma_20'],
        line=dict(color='#4ECDC4', width=3),
        name='SMA 20'
    ))
    
    fig.update_layout(
        title=f'<b>{coin} - Professional Trading Chart</b>',
        xaxis_title='Time',
        yaxis_title='Price (USDT)',
        template='plotly_dark',
        height=500,
        showlegend=True,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white')
    )
    
    return fig

# Generate mock price data
def generate_price_data(coin, current_price):
    dates = pd.date_range(end=datetime.now(), periods=100, freq='1H')
    prices = []
    
    price = current_price
    for i in range(100):
        change = np.random.normal(0, current_price * 0.002)
        price = max(price + change, current_price * 0.8)
        prices.append(price)
    
    df = pd.DataFrame({
        'timestamp': dates,
        'open': prices,
        'high': [p + abs(np.random.normal(0, current_price * 0.01)) for p in prices],
        'low': [p - abs(np.random.normal(0, current_price * 0.01)) for p in prices],
        'close': prices,
        'sma_20': pd.Series(prices).rolling(20).mean()
    })
    
    return df

# Advanced AI Analysis Engine
def run_ai_analysis(coin, current_price, capital, risk_tolerance):
    price_data = generate_price_data(coin, current_price)
    latest_close = price_data['close'].iloc[-1]
    sma_20 = price_data['sma_20'].iloc[-1]
    
    # AI-driven calculations
    rsi = max(20, min(80, 50 + (latest_close - sma_20) / sma_20 * 1000))
    volatility = price_data['close'].pct_change().std() * 100
    
    # Strategy selection
    if rsi < 35 and latest_close > sma_20:
        strategy = "QUANTUM MOMENTUM EXPLOSION"
        leverage = min(50, 10 + (35 - rsi) * 2)
        confidence = 0.89
        theme_color = "yellow"
    elif rsi > 65 and latest_close < sma_20:
        strategy = "NEURAL MEAN REVERSION"
        leverage = 8
        confidence = 0.83
        theme_color = "red"
    elif volatility > 8:
        strategy = "VOLATILITY HARVESTING ALGO"
        leverage = 12
        confidence = 0.86
        theme_color = "yellow"
    else:
        strategy = "AI STATISTICAL ARBITRAGE"
        leverage = 15
        confidence = 0.81
        theme_color = "red"
    
    # Risk assessment
    var_1d = latest_close * 0.021
    expected_shortfall = latest_close * 0.038
    
    # Position sizing
    position_size = capital * 0.15
    max_risk = position_size * 0.08
    
    # Entry/Exit levels
    entry_min = latest_close * 0.995
    entry_max = latest_close * 1.005
    stop_loss = latest_close * 0.985
    take_profit = latest_close * 1.035
    
    return {
        'strategy': strategy,
        'leverage': leverage,
        'confidence': confidence,
        'rsi': rsi,
        'volatility': volatility,
        'var_1d': var_1d,
        'expected_shortfall': expected_shortfall,
        'position_size': position_size,
        'max_risk': max_risk,
        'entry_min': entry_min,
        'entry_max': entry_max,
        'stop_loss': stop_loss,
        'take_profit': take_profit,
        'price_data': price_data,
        'theme_color': theme_color
    }

# Main Application
def main():
    # Sidebar - Premium Authentication
    with st.sidebar:
        st.markdown("""
        <div style='text-align: center; padding: 1rem; background: linear-gradient(135deg, rgba(255,107,107,0.2), rgba(255,217,61,0.2)); border-radius: 15px; margin-bottom: 2rem;'>
            <h2 style='color: #FFD93D; margin: 0;'>🚀 TRAPMEME AI</h2>
            <p style='color: #FF6B6B; margin: 0;'>v6.0 PREMIUM</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🔐 Authentication")
        
        auth_tab1, auth_tab2 = st.tabs(["🔑 Login", "📝 Sign Up"])
        
        with auth_tab1:
            email = st.text_input("Email", placeholder="trader@premium.com")
            password = st.text_input("Password", type="password", placeholder="••••••••")
            if st.button("🚀 Access Platform", use_container_width=True):
                st.success("Welcome back, Premium Trader!")
        
        with auth_tab2:
            new_email = st.text_input("New Email", placeholder="new@trader.com")
            new_password = st.text_input("New Password", type="password", placeholder="••••••••")
            if st.button("⭐ Join Premium", use_container_width=True):
                st.success("Premium account created!")
        
        st.markdown("---")
        st.markdown("### 📈 Live Markets")
        
        # Live market data with theme
        coins = ["BTC/USDT", "ETH/USDT", "SOL/USDT", "ADA/USDT", "XRP/USDT", "DOT/USDT"]
        for coin in coins:
            price = get_live_price(coin)
            change = np.random.uniform(-3, 3)
            color = "#FFD93D" if change >= 0 else "#FF6B6B"
            st.markdown(f"""
            <div class="premium-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="color: {color}; font-weight: 600;">{coin}</span>
                    <span style="color: white;">${price:,.2f}</span>
                </div>
                <div style="color: {color}; font-size: 0.8rem; text-align: right;">{change:+.2f}%</div>
            </div>
            """, unsafe_allow_html=True)
    
    # Main content area with RED & YELLOW columns
    st.markdown('<h1 class="main-header">🚀 TRAPMEME AI v6.0 PREMIUM</h1>', unsafe_allow_html=True)
    st.markdown("### <span style='color: #FFD93D;'>Institutional-Grade Trading Platform</span>", unsafe_allow_html=True)
    
    # Main columns with theme
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="red-column">', unsafe_allow_html=True)
        st.markdown("### 🎯 AI Trading Terminal")
        
        # Trading inputs
        terminal_col1, terminal_col2 = st.columns(2)
        
        with terminal_col1:
            selected_coin = st.selectbox("💰 Select Asset", [
                "BTC/USDT", "ETH/USDT", "SOL/USDT", 
                "ADA/USDT", "XRP/USDT", "DOT/USDT"
            ])
            current_price = get_live_price(selected_coin)
            st.markdown(f"""
            <div class="metric-card-red">
                <h3 style='color: #FF6B6B; margin: 0;'>Live Price</h3>
                <h2 style='color: #FFD93D; margin: 0;'>${current_price:,.2f}</h2>
            </div>
            """, unsafe_allow_html=True)
        
        with terminal_col2:
            trading_capital = st.number_input("💼 Trading Capital ($)", 
                                            value=10000, 
                                            min_value=100, 
                                            step=1000)
            risk_tolerance = st.select_slider("🎯 Risk Profile", 
                                            options=["Conservative", "Moderate", "Aggressive", "Institutional"])
        
        # Analysis button
        if st.button("🚀 RUN AI QUANTUM ANALYSIS", use_container_width=True, type="primary"):
            with st.spinner("🔄 Running Institutional Analysis..."):
                time.sleep(2)
                analysis_result = run_ai_analysis(selected_coin, current_price, trading_capital, risk_tolerance)
                
                st.success("✅ AI Analysis Complete!")
                
                # Chart
                with st.expander("📊 Trading Chart & Analysis", expanded=True):
                    chart = generate_trading_chart(selected_coin, analysis_result['price_data'])
                    st.plotly_chart(chart, use_container_width=True)
                
                # Strategy details with theme colors
                col_a, col_b, col_c, col_d = st.columns(4)
                with col_a:
                    st.markdown(f"""
                    <div class="metric-card-{analysis_result['theme_color']}">
                        <h4>AI Strategy</h4>
                        <h3>{analysis_result['strategy']}</h3>
                    </div>
                    """, unsafe_allow_html=True)
                with col_b:
                    st.markdown(f"""
                    <div class="metric-card-{analysis_result['theme_color']}">
                        <h4>Confidence</h4>
                        <h3>{analysis_result['confidence']*100:.1f}%</h3>
                    </div>
                    """, unsafe_allow_html=True)
                with col_c:
                    st.markdown(f"""
                    <div class="metric-card-{analysis_result['theme_color']}">
                        <h4>Leverage</h4>
                        <h3>{analysis_result['leverage']}x</h3>
                    </div>
                    """, unsafe_allow_html=True)
                with col_d:
                    st.markdown(f"""
                    <div class="metric-card-{analysis_result['theme_color']}">
                        <h4>RSI</h4>
                        <h3>{analysis_result['rsi']:.1f}</h3>
                    </div>
                    """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="yellow-column">', unsafe_allow_html=True)
        st.markdown("### 💰 Portfolio Overview")
        
        # Portfolio metrics
        st.markdown("""
        <div class="premium-card">
            <h4 style='color: #FFD93D;'>Total Value</h4>
            <h2 style='color: white;'>$125,430</h2>
            <p style='color: #4ECDC4;'>+2.3% Today</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="premium-card">
            <h4 style='color: #FFD93D;'>Today's P&L</h4>
            <h2 style='color: white;'>$2,890</h2>
            <p style='color: #4ECDC4;'>+1.8%</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="premium-card">
            <h4 style='color: #FFD93D;'>Win Rate</h4>
            <h2 style='color: white;'>87.3%</h2>
            <p style='color: #4ECDC4;'>+2.1%</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("### 🔔 Premium Alerts")
        
        # Telegram integration
        st.text_input("📱 Telegram Chat ID", placeholder="Enter your Telegram ID")
        st.selectbox("⏰ Alert Frequency", ["Real-time", "15min", "1H", "4H"])
        
        if st.button("✅ Enable Premium Alerts", use_container_width=True):
            st.success("Telegram alerts activated!")
        
        st.markdown("---")
        st.markdown("### ⚡ Quick Actions")
        
        # Action buttons
        if st.button("📊 Portfolio Analytics", use_container_width=True):
            st.info("Opening Portfolio Dashboard...")
        
        if st.button("🔄 Market Scanner", use_container_width=True):
            st.info("Scanning for opportunities...")
        
        if st.button("📈 Performance Report", use_container_width=True):
            st.info("Generating report...")
        
        st.markdown('</div>', unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; padding: 2rem; background: linear-gradient(135deg, rgba(255,107,107,0.1), rgba(255,217,61,0.1)); border-radius: 15px;'>
        <p style='color: #FFD93D; font-size: 1.2rem; margin: 0;'>🚀 <b>TrapMeme AI v6.0 PREMIUM</b></p>
        <p style='color: #FF6B6B; margin: 0;'>Institutional Trading Platform | Red & Yellow Premium Theme</p>
        <p style='color: #4ECDC4; margin: 0;'>Advanced AI/ML • Real-time Analytics • Risk Management</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
