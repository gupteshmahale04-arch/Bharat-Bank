"""
BharatBank - Indian Bank Management System
Run: streamlit run bank_app.py
"""

import json
import random
import string
from pathlib import Path
import streamlit as st

# ─── Page Config ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="BharatBank",
    page_icon="🏦",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ─── Custom CSS ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=DM+Sans:wght@300;400;500;600&display=swap');

:root {
    --saffron:  #FF6B35;
    --navy:     #0A1F44;
    --gold:     #C9A84C;
    --cream:    #FDF6EC;
    --green:    #138808;
    --white:    #FFFFFF;
    --lightbg:  #F4F7FB;
    --border:   #D8E0EE;
    --text:     #1E2A3A;
    --subtext:  #5A6A82;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    color: var(--text);
}

/* --- Sidebar --- */
section[data-testid="stSidebar"] {
    background: var(--navy) !important;
    border-right: 4px solid var(--saffron);
}
section[data-testid="stSidebar"] * {
    color: var(--white) !important;
}
section[data-testid="stSidebar"] .stRadio label {
    font-size: 0.97rem;
    padding: 6px 4px;
    cursor: pointer;
}

/* --- Hero Header --- */
.bank-header {
    background: linear-gradient(135deg, var(--navy) 0%, #1a3563 60%, #0d2b58 100%);
    border-radius: 18px;
    padding: 2rem 2.5rem 1.6rem 2.5rem;
    margin-bottom: 1.8rem;
    display: flex;
    align-items: center;
    gap: 1.4rem;
    border-left: 6px solid var(--saffron);
    box-shadow: 0 8px 32px rgba(10,31,68,0.18);
    position: relative;
    overflow: hidden;
}
.bank-header::after {
    content: "🇮🇳";
    position: absolute;
    right: 2rem;
    top: 50%;
    transform: translateY(-50%);
    font-size: 3.5rem;
    opacity: 0.15;
}
.bank-header h1 {
    font-family: 'Playfair Display', serif;
    font-size: 2.2rem;
    color: var(--white) !important;
    margin: 0;
    letter-spacing: 1px;
}
.bank-header p {
    color: #A8BBDA !important;
    margin: 0.2rem 0 0 0;
    font-size: 0.9rem;
    font-weight: 300;
    letter-spacing: 2px;
    text-transform: uppercase;
}
.bank-logo {
    font-size: 3rem;
    background: var(--saffron);
    border-radius: 14px;
    padding: 0.3rem 0.6rem;
    line-height: 1;
}

/* --- Section title --- */
.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem;
    color: var(--navy);
    border-bottom: 3px solid var(--saffron);
    padding-bottom: 0.5rem;
    margin-bottom: 1.4rem;
}

/* --- Info Cards --- */
.info-card {
    background: var(--white);
    border-radius: 14px;
    padding: 1.2rem 1.5rem;
    border: 1px solid var(--border);
    box-shadow: 0 2px 12px rgba(10,31,68,0.06);
    margin-bottom: 0.8rem;
}
.info-card .label {
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: var(--subtext);
    font-weight: 500;
}
.info-card .value {
    font-size: 1.1rem;
    font-weight: 600;
    color: var(--navy);
    margin-top: 3px;
}
.info-card .balance-value {
    font-family: 'Playfair Display', serif;
    font-size: 1.9rem;
    color: var(--green);
}

/* --- Stat strip --- */
.stat-strip {
    display: flex;
    gap: 1rem;
    margin-bottom: 1.4rem;
    flex-wrap: wrap;
}
.stat-box {
    flex: 1;
    min-width: 110px;
    background: var(--navy);
    color: var(--white) !important;
    border-radius: 12px;
    padding: 1rem;
    text-align: center;
}
.stat-box .stat-num {
    font-family: 'Playfair Display', serif;
    font-size: 1.8rem;
    color: var(--saffron) !important;
}
.stat-box .stat-lbl {
    font-size: 0.72rem;
    text-transform: uppercase;
    letter-spacing: 1.4px;
    color: #A8BBDA !important;
    margin-top: 2px;
}

/* --- Success / Error banners --- */
.success-banner {
    background: #E6F9EE;
    border-left: 5px solid var(--green);
    border-radius: 10px;
    padding: 1rem 1.2rem;
    color: #0D5E25;
    font-weight: 500;
    margin-bottom: 1rem;
}
.error-banner {
    background: #FEF0EF;
    border-left: 5px solid #E53E3E;
    border-radius: 10px;
    padding: 1rem 1.2rem;
    color: #822727;
    font-weight: 500;
    margin-bottom: 1rem;
}
.warn-banner {
    background: #FFFBEB;
    border-left: 5px solid var(--gold);
    border-radius: 10px;
    padding: 1rem 1.2rem;
    color: #7B5E1F;
    font-weight: 500;
    margin-bottom: 1rem;
}

/* --- Input tweaks --- */
div[data-testid="stTextInput"] input,
div[data-testid="stNumberInput"] input {
    border-radius: 8px !important;
    border-color: var(--border) !important;
    font-family: 'DM Sans', sans-serif !important;
}
div[data-testid="stTextInput"] input:focus,
div[data-testid="stNumberInput"] input:focus {
    border-color: var(--saffron) !important;
    box-shadow: 0 0 0 2px rgba(255,107,53,0.15) !important;
}

/* --- Buttons --- */
div.stButton > button {
    background: var(--saffron) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.97rem !important;
    padding: 0.55rem 1.8rem !important;
    transition: background 0.2s, transform 0.1s !important;
    letter-spacing: 0.3px;
}
div.stButton > button:hover {
    background: #e85a28 !important;
    transform: translateY(-1px) !important;
}

/* --- Divider --- */
hr { border-color: var(--border) !important; }

/* --- Footer --- */
.footer {
    text-align: center;
    color: var(--subtext);
    font-size: 0.78rem;
    margin-top: 2.5rem;
    padding-top: 1rem;
    border-top: 1px solid var(--border);
    letter-spacing: 0.5px;
}
</style>
""", unsafe_allow_html=True)


# ─── Database helpers ────────────────────────────────────────────────────────
DATABASE = "bharatbank_db.json"

def load_data():
    if Path(DATABASE).exists():
        with open(DATABASE) as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATABASE, "w") as f:
        json.dump(data, f, indent=2)

def generate_account_no():
    alpha = random.choices(string.ascii_uppercase, k=4)
    num   = random.choices(string.digits, k=8)
    return "BB" + "".join(num[:4]) + "".join(alpha) + "".join(num[4:])

def find_user(data, accno, pin):
    matches = [u for u in data if u["AccountNo"] == accno and u["pin"] == int(pin)]
    return matches[0] if matches else None


# ─── Session state ───────────────────────────────────────────────────────────
if "msg" not in st.session_state:
    st.session_state.msg = ("", "")   # (text, type)


# ─── Header ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="bank-header">
  <div class="bank-logo">🏦</div>
  <div>
    <h1>BharatBank</h1>
    <p>Trusted Banking · Since 1947 · Serving Bharat</p>
  </div>
</div>
""", unsafe_allow_html=True)


# ─── Sidebar nav ─────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🏦 BharatBank")
    st.markdown("---")
    menu = st.radio(
        "Navigation",
        options=[
            "🏠  Dashboard",
            "➕  Open Account",
            "💰  Deposit Money",
            "💸  Withdraw Money",
            "👁️  Account Details",
            "✏️  Update Details",
            "🗑️  Close Account",
        ],
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.markdown(
        "<small style='color:#7A8FAF;'>IFSC: BRTB0001 · MICR: 452005001<br>"
        "Indore Branch · MP, India</small>",
        unsafe_allow_html=True,
    )


# ─── Message banner ──────────────────────────────────────────────────────────
def show_msg():
    text, kind = st.session_state.msg
    if text:
        if kind == "success":
            st.markdown(f'<div class="success-banner">✅ {text}</div>', unsafe_allow_html=True)
        elif kind == "error":
            st.markdown(f'<div class="error-banner">❌ {text}</div>', unsafe_allow_html=True)
        elif kind == "warn":
            st.markdown(f'<div class="warn-banner">⚠️ {text}</div>', unsafe_allow_html=True)
        st.session_state.msg = ("", "")


# ═══════════════════════════════════════════════════════════════════════════════
# DASHBOARD
# ═══════════════════════════════════════════════════════════════════════════════
if "Dashboard" in menu:
    data = load_data()
    total_balance = sum(u["balance"] for u in data)

    st.markdown('<div class="section-title">📊 Bank Overview</div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="stat-strip">
      <div class="stat-box">
        <div class="stat-num">{len(data)}</div>
        <div class="stat-lbl">Total Accounts</div>
      </div>
      <div class="stat-box">
        <div class="stat-num">₹{total_balance:,.0f}</div>
        <div class="stat-lbl">Total Deposits</div>
      </div>
      <div class="stat-box">
        <div class="stat-num">{sum(1 for u in data if u['balance'] > 0)}</div>
        <div class="stat-lbl">Active Accounts</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### Recent Accounts")
    if data:
        for u in reversed(data[-5:]):
            st.markdown(f"""
            <div class="info-card">
              <div style="display:flex;justify-content:space-between;align-items:center;">
                <div>
                  <div class="label">Account Holder</div>
                  <div class="value">{u['name']}</div>
                  <div style="font-size:0.78rem;color:var(--subtext);margin-top:3px;">{u['AccountNo']}</div>
                </div>
                <div style="text-align:right;">
                  <div class="label">Balance</div>
                  <div class="balance-value">₹{u['balance']:,.2f}</div>
                </div>
              </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No accounts yet. Open the first account to get started!")

    show_msg()


# ═══════════════════════════════════════════════════════════════════════════════
# OPEN ACCOUNT
# ═══════════════════════════════════════════════════════════════════════════════
elif "Open Account" in menu:
    st.markdown('<div class="section-title">➕ Open New Account</div>', unsafe_allow_html=True)
    show_msg()

    with st.form("create_form"):
        col1, col2 = st.columns(2)
        with col1:
            name  = st.text_input("Full Name", placeholder="e.g. Ravi Kumar Sharma")
            email = st.text_input("Email Address", placeholder="ravi@example.com")
        with col2:
            age   = st.number_input("Age", min_value=1, max_value=120, value=25, step=1)
            pin   = st.text_input("4-Digit PIN", max_chars=4, type="password", placeholder="••••")

        st.markdown("*By opening an account you agree to BharatBank's Terms & Conditions.*")
        submitted = st.form_submit_button("🏦 Open Account")

    if submitted:
        if age < 12:
            st.session_state.msg = ("Minimum age to open an account is 12 years.", "error")
        elif not pin.isdigit() or len(pin) != 4:
            st.session_state.msg = ("PIN must be exactly 4 digits.", "error")
        elif not name.strip():
            st.session_state.msg = ("Please enter a valid name.", "error")
        else:
            data = load_data()
            acc_no = generate_account_no()
            data.append({
                "name":      name.strip(),
                "age":       int(age),
                "email":     email.strip(),
                "AccountNo": acc_no,
                "pin":       int(pin),
                "balance":   0,
            })
            save_data(data)
            st.session_state.msg = (f"Account opened successfully! Your Account No: {acc_no}", "success")

        st.rerun()


# ═══════════════════════════════════════════════════════════════════════════════
# DEPOSIT
# ═══════════════════════════════════════════════════════════════════════════════
elif "Deposit" in menu:
    st.markdown('<div class="section-title">💰 Deposit Money</div>', unsafe_allow_html=True)
    show_msg()

    with st.form("deposit_form"):
        accno  = st.text_input("Account Number", placeholder="BBxxxxxxXXXXxxxx")
        pin    = st.text_input("PIN", max_chars=4, type="password", placeholder="••••")
        amount = st.number_input("Amount to Deposit (₹)", min_value=1, step=100, value=500)
        submitted = st.form_submit_button("💰 Deposit")

    if submitted:
        data = load_data()
        user = find_user(data, accno.strip(), pin)
        if not user:
            st.session_state.msg = ("Invalid account number or PIN.", "error")
        else:
            user["balance"] += amount
            save_data(data)
            st.session_state.msg = (
                f"₹{amount:,.2f} deposited successfully. New balance: ₹{user['balance']:,.2f}", "success"
            )
        st.rerun()


# ═══════════════════════════════════════════════════════════════════════════════
# WITHDRAW
# ═══════════════════════════════════════════════════════════════════════════════
elif "Withdraw" in menu:
    st.markdown('<div class="section-title">💸 Withdraw Money</div>', unsafe_allow_html=True)
    show_msg()

    with st.form("withdraw_form"):
        accno  = st.text_input("Account Number", placeholder="BBxxxxxxXXXXxxxx")
        pin    = st.text_input("PIN", max_chars=4, type="password", placeholder="••••")
        amount = st.number_input("Amount to Withdraw (₹)", min_value=1, step=100, value=500)
        submitted = st.form_submit_button("💸 Withdraw")

    if submitted:
        data = load_data()
        user = find_user(data, accno.strip(), pin)
        if not user:
            st.session_state.msg = ("Invalid account number or PIN.", "error")
        elif amount > user["balance"]:
            st.session_state.msg = (
                f"Insufficient balance. Available: ₹{user['balance']:,.2f}", "warn"
            )
        else:
            user["balance"] -= amount
            save_data(data)
            st.session_state.msg = (
                f"₹{amount:,.2f} withdrawn successfully. Remaining balance: ₹{user['balance']:,.2f}", "success"
            )
        st.rerun()


# ═══════════════════════════════════════════════════════════════════════════════
# ACCOUNT DETAILS
# ═══════════════════════════════════════════════════════════════════════════════
elif "Account Details" in menu:
    st.markdown('<div class="section-title">👁️ Account Details</div>', unsafe_allow_html=True)
    show_msg()

    with st.form("details_form"):
        accno = st.text_input("Account Number", placeholder="BBxxxxxxXXXXxxxx")
        pin   = st.text_input("PIN", max_chars=4, type="password", placeholder="••••")
        submitted = st.form_submit_button("🔍 View Details")

    if submitted:
        data = load_data()
        user = find_user(data, accno.strip(), pin)
        if not user:
            st.session_state.msg = ("Invalid account number or PIN.", "error")
            st.rerun()
        else:
            st.markdown(f"""
            <div class="info-card">
              <div class="label">Account Holder</div>
              <div class="value" style="font-size:1.4rem;">{user['name']}</div>
            </div>
            <div class="info-card">
              <div class="label">Account Number</div>
              <div class="value">{user['AccountNo']}</div>
            </div>
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"""
                <div class="info-card">
                  <div class="label">Age</div>
                  <div class="value">{user['age']} years</div>
                </div>
                """, unsafe_allow_html=True)
            with col2:
                st.markdown(f"""
                <div class="info-card">
                  <div class="label">Email</div>
                  <div class="value">{user.get('email','—')}</div>
                </div>
                """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class="info-card" style="border-left:5px solid var(--green);">
              <div class="label">Available Balance</div>
              <div class="balance-value">₹{user['balance']:,.2f}</div>
            </div>
            """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# UPDATE DETAILS
# ═══════════════════════════════════════════════════════════════════════════════
elif "Update Details" in menu:
    st.markdown('<div class="section-title">✏️ Update Account Details</div>', unsafe_allow_html=True)
    show_msg()

    with st.form("auth_form"):
        accno = st.text_input("Account Number", placeholder="BBxxxxxxXXXXxxxx")
        pin   = st.text_input("PIN", max_chars=4, type="password", placeholder="••••")
        auth  = st.form_submit_button("🔓 Authenticate")

    if auth:
        data = load_data()
        user = find_user(data, accno.strip(), pin)
        if not user:
            st.session_state.msg = ("Invalid account number or PIN.", "error")
            st.rerun()
        else:
            st.session_state["update_accno"] = accno.strip()
            st.session_state["update_pin"]   = int(pin)

    if "update_accno" in st.session_state:
        data = load_data()
        user = find_user(data, st.session_state["update_accno"], str(st.session_state["update_pin"]))
        if user:
            st.success(f"Authenticated as **{user['name']}**")
            with st.form("update_form"):
                new_name  = st.text_input("New Name (leave blank to keep)", placeholder=user["name"])
                new_email = st.text_input("New Email (leave blank to keep)", placeholder=user.get("email",""))
                new_pin   = st.text_input("New PIN (leave blank to keep)", max_chars=4, type="password")
                save_btn  = st.form_submit_button("💾 Save Changes")

            if save_btn:
                if new_name.strip():
                    user["name"]  = new_name.strip()
                if new_email.strip():
                    user["email"] = new_email.strip()
                if new_pin:
                    if not new_pin.isdigit() or len(new_pin) != 4:
                        st.session_state.msg = ("New PIN must be 4 digits.", "error")
                        st.rerun()
                    user["pin"] = int(new_pin)
                save_data(data)
                del st.session_state["update_accno"]
                del st.session_state["update_pin"]
                st.session_state.msg = ("Account details updated successfully.", "success")
                st.rerun()


# ═══════════════════════════════════════════════════════════════════════════════
# CLOSE ACCOUNT
# ═══════════════════════════════════════════════════════════════════════════════
elif "Close Account" in menu:
    st.markdown('<div class="section-title">🗑️ Close Account</div>', unsafe_allow_html=True)
    show_msg()

    st.markdown('<div class="warn-banner">⚠️ Closing your account is permanent and cannot be undone.</div>', unsafe_allow_html=True)

    with st.form("delete_form"):
        accno   = st.text_input("Account Number", placeholder="BBxxxxxxXXXXxxxx")
        pin     = st.text_input("PIN", max_chars=4, type="password", placeholder="••••")
        confirm = st.checkbox("I understand this action is irreversible")
        submitted = st.form_submit_button("🗑️ Close Account")

    if submitted:
        if not confirm:
            st.session_state.msg = ("Please confirm by checking the box.", "warn")
        else:
            data = load_data()
            user = find_user(data, accno.strip(), pin)
            if not user:
                st.session_state.msg = ("Invalid account number or PIN.", "error")
            else:
                data.remove(user)
                save_data(data)
                st.session_state.msg = ("Account closed successfully. Thank you for banking with BharatBank.", "success")
        st.rerun()


# ─── Footer ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
  🏦 BharatBank · Regulated by RBI · Member DICGC · Deposits insured up to ₹5,00,000<br>
  © 2025 BharatBank Limited · All Rights Reserved · Indore, Madhya Pradesh
</div>
""", unsafe_allow_html=True)