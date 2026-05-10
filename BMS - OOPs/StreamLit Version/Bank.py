import random
import string
import json
import streamlit as st
from pathlib import Path

# ─── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="ZK Bank",
    page_icon="🏦",
    layout="centered",
)

# ─── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Mono', monospace;
}

/* Background */
.stApp {
    background: #0a0a0f;
    color: #e8e4d9;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: #0f0f1a !important;
    border-right: 1px solid #1e1e2e;
}

[data-testid="stSidebar"] * {
    color: #e8e4d9 !important;
}

/* Header */
.bank-header {
    font-family: 'Syne', sans-serif;
    font-size: 3rem;
    font-weight: 800;
    letter-spacing: -2px;
    color: #c8b560;
    line-height: 1;
    margin-bottom: 4px;
}

.bank-tagline {
    font-size: 0.75rem;
    letter-spacing: 4px;
    color: #5a5a6e;
    text-transform: uppercase;
    margin-bottom: 2rem;
}

/* Cards */
.info-card {
    background: #13131f;
    border: 1px solid #1e1e2e;
    border-radius: 8px;
    padding: 1.2rem 1.5rem;
    margin: 0.5rem 0;
}

.info-card .label {
    font-size: 0.65rem;
    letter-spacing: 3px;
    color: #5a5a6e;
    text-transform: uppercase;
    margin-bottom: 2px;
}

.info-card .value {
    font-size: 1.1rem;
    color: #e8e4d9;
    font-weight: 500;
}

.balance-card {
    background: linear-gradient(135deg, #1a1a0f 0%, #13131f 100%);
    border: 1px solid #c8b560;
    border-radius: 8px;
    padding: 1.5rem;
    text-align: center;
    margin: 1rem 0;
}

.balance-label {
    font-size: 0.65rem;
    letter-spacing: 4px;
    color: #c8b560;
    text-transform: uppercase;
}

.balance-amount {
    font-family: 'Syne', sans-serif;
    font-size: 2.5rem;
    font-weight: 700;
    color: #c8b560;
}

/* Success / Error boxes */
.msg-success {
    background: #0a1f0a;
    border: 1px solid #2a5a2a;
    border-radius: 6px;
    padding: 0.8rem 1.2rem;
    color: #6abf6a;
    font-size: 0.85rem;
    margin: 0.5rem 0;
}

.msg-error {
    background: #1f0a0a;
    border: 1px solid #5a2a2a;
    border-radius: 6px;
    padding: 0.8rem 1.2rem;
    color: #bf6a6a;
    font-size: 0.85rem;
    margin: 0.5rem 0;
}

/* Inputs */
.stTextInput > div > div > input,
.stNumberInput > div > div > input {
    background: #13131f !important;
    border: 1px solid #1e1e2e !important;
    border-radius: 6px !important;
    color: #e8e4d9 !important;
    font-family: 'DM Mono', monospace !important;
}

.stTextInput > div > div > input:focus,
.stNumberInput > div > div > input:focus {
    border-color: #c8b560 !important;
    box-shadow: 0 0 0 1px #c8b56040 !important;
}

/* Buttons */
.stButton > button {
    background: #c8b560 !important;
    color: #0a0a0f !important;
    border: none !important;
    border-radius: 4px !important;
    font-family: 'DM Mono', monospace !important;
    font-weight: 500 !important;
    letter-spacing: 1px !important;
    padding: 0.5rem 2rem !important;
    transition: all 0.15s ease !important;
}

.stButton > button:hover {
    background: #dfc970 !important;
    transform: translateY(-1px) !important;
}

/* Sidebar radio */
[data-testid="stSidebar"] .stRadio label {
    font-size: 0.85rem !important;
    letter-spacing: 1px !important;
}

/* Divider */
hr {
    border-color: #1e1e2e !important;
    margin: 1.5rem 0 !important;
}

/* Hide Streamlit branding */
#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ─── Data Layer ────────────────────────────────────────────────────────────────
DATA_FILE = Path("bank_data.json")

def load_data():
    if DATA_FILE.exists():
        with open(DATA_FILE) as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def generate_account_number():
    nums = random.choices(string.digits, k=2)
    low = random.choices(string.ascii_lowercase, k=3)
    up = random.choices(string.ascii_uppercase, k=3)
    sep = random.choices("!@#$%^&*", k=1)
    parts = nums + low + up + sep
    random.shuffle(parts)
    return "".join(parts)

def find_user(data, acc_no, pin):
    matches = [u for u in data if u["accountNo"] == acc_no and u["pin"] == pin]
    return matches[0] if matches else None

# ─── Helpers ───────────────────────────────────────────────────────────────────
def success(msg): st.markdown(f'<div class="msg-success">✓ {msg}</div>', unsafe_allow_html=True)
def error(msg):   st.markdown(f'<div class="msg-error">✗ {msg}</div>', unsafe_allow_html=True)

def info_row(label, value):
    st.markdown(f"""
    <div class="info-card">
        <div class="label">{label}</div>
        <div class="value">{value}</div>
    </div>""", unsafe_allow_html=True)

def auth_fields():
    acc = st.text_input("Account Number", placeholder="e.g. aB3!xY9")
    pin = st.text_input("PIN", type="password", placeholder="4-digit PIN")
    return acc.strip(), pin.strip()

# ─── Header ────────────────────────────────────────────────────────────────────
st.markdown('<div class="bank-header">ZK BANK</div>', unsafe_allow_html=True)
st.markdown('<div class="bank-tagline">Secure · Simple · Streamlined</div>', unsafe_allow_html=True)

# ─── Sidebar Navigation ────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div style="font-family:Syne,sans-serif;font-size:1.4rem;font-weight:700;color:#c8b560;margin-bottom:1.5rem;">MENU</div>', unsafe_allow_html=True)
    page = st.radio("", [
        "🆕  Create Account",
        "💰  Deposit",
        "💸  Withdraw",
        "📋  Account Details",
        "✏️  Update Account",
        "🗑️  Delete Account",
    ], label_visibility="collapsed")
    st.markdown("---")
    st.markdown('<div style="font-size:0.65rem;letter-spacing:2px;color:#5a5a6e;">POWERED BY ZAIN</div>', unsafe_allow_html=True)

data = load_data()

# ═══════════════════════════════════════════════════════════════════════════════
# 1. CREATE ACCOUNT
# ═══════════════════════════════════════════════════════════════════════════════
if "Create" in page:
    st.subheader("Open a New Account")
    st.markdown("---")

    name  = st.text_input("Full Name", placeholder="Muhammad Zain")
    age   = st.number_input("Age", min_value=1, max_value=120, value=18)
    email = st.text_input("Email", placeholder="zain@example.com")
    pin   = st.text_input("4-Digit PIN", type="password", placeholder="····")

    if st.button("Create Account"):
        if not all([name, email, pin]):
            error("All fields are required.")
        elif age < 18:
            error("You must be at least 18 years old.")
        elif not pin.isdigit() or len(pin) != 4:
            error("PIN must be exactly 4 digits.")
        elif any(u["email"] == email for u in data):
            error("An account with this email already exists.")
        else:
            acc_no = generate_account_number()
            new_account = {
                "name": name,
                "age": int(age),
                "email": email,
                "pin": pin,
                "accountNo": acc_no,
                "balance": 0,
            }
            data.append(new_account)
            save_data(data)
            success("Account created successfully!")
            st.markdown("---")
            info_row("Account Holder", name)
            info_row("Account Number", acc_no)
            info_row("Email", email)
            st.markdown(f'<div class="balance-card"><div class="balance-label">Opening Balance</div><div class="balance-amount">PKR 0</div></div>', unsafe_allow_html=True)
            st.info("📌 Save your Account Number — you'll need it to log in.")

# ═══════════════════════════════════════════════════════════════════════════════
# 2. DEPOSIT
# ═══════════════════════════════════════════════════════════════════════════════
elif "Deposit" in page:
    st.subheader("Deposit Money")
    st.markdown("---")

    acc, pin = auth_fields()
    amount = st.number_input("Amount to Deposit (PKR)", min_value=1, max_value=100000, value=1000)

    if st.button("Deposit"):
        user = find_user(data, acc, pin)
        if not user:
            error("Invalid account number or PIN.")
        elif amount <= 0:
            error("Amount must be greater than 0.")
        else:
            user["balance"] += amount
            save_data(data)
            success(f"PKR {amount:,} deposited successfully!")
            st.markdown(f'<div class="balance-card"><div class="balance-label">New Balance</div><div class="balance-amount">PKR {user["balance"]:,}</div></div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# 3. WITHDRAW
# ═══════════════════════════════════════════════════════════════════════════════
elif "Withdraw" in page:
    st.subheader("Withdraw Money")
    st.markdown("---")

    acc, pin = auth_fields()
    amount = st.number_input("Amount to Withdraw (PKR)", min_value=1, max_value=100000, value=500)

    if st.button("Withdraw"):
        user = find_user(data, acc, pin)
        if not user:
            error("Invalid account number or PIN.")
        elif amount <= 0:
            error("Amount must be greater than 0.")
        elif amount > user["balance"]:
            error(f"Insufficient balance. Current balance: PKR {user['balance']:,}")
        else:
            user["balance"] -= amount
            save_data(data)
            success(f"PKR {amount:,} withdrawn successfully!")
            st.markdown(f'<div class="balance-card"><div class="balance-label">Remaining Balance</div><div class="balance-amount">PKR {user["balance"]:,}</div></div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# 4. ACCOUNT DETAILS
# ═══════════════════════════════════════════════════════════════════════════════
elif "Details" in page:
    st.subheader("Account Details")
    st.markdown("---")

    acc, pin = auth_fields()

    if st.button("View Details"):
        user = find_user(data, acc, pin)
        if not user:
            error("Invalid account number or PIN.")
        else:
            info_row("Account Holder", user["name"])
            info_row("Age", str(user["age"]))
            info_row("Email", user["email"])
            info_row("Account Number", user["accountNo"])
            st.markdown(f'<div class="balance-card"><div class="balance-label">Current Balance</div><div class="balance-amount">PKR {user["balance"]:,}</div></div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# 5. UPDATE ACCOUNT
# ═══════════════════════════════════════════════════════════════════════════════
elif "Update" in page:
    st.subheader("Update Account Details")
    st.markdown("---")

    acc, pin = auth_fields()

    if st.button("Load Account"):
        user = find_user(data, acc, pin)
        if not user:
            error("Invalid account number or PIN.")
        else:
            st.session_state["update_user_acc"] = acc
            st.session_state["update_user_pin"] = pin
            success(f"Welcome, {user['name']}! Update your details below.")

    if "update_user_acc" in st.session_state:
        user = find_user(data, st.session_state["update_user_acc"], st.session_state["update_user_pin"])
        if user:
            st.markdown("---")
            new_name  = st.text_input("New Name (leave blank to keep)", placeholder=user["name"])
            new_email = st.text_input("New Email (leave blank to keep)", placeholder=user["email"])
            new_pin   = st.text_input("New PIN (leave blank to keep)", type="password", placeholder="····")

            if st.button("Save Changes"):
                changed = False
                if new_name.strip():
                    user["name"] = new_name.strip()
                    changed = True
                if new_email.strip():
                    user["email"] = new_email.strip()
                    changed = True
                if new_pin.strip():
                    if not new_pin.isdigit() or len(new_pin) != 4:
                        error("New PIN must be exactly 4 digits. Other changes saved.")
                    else:
                        user["pin"] = new_pin.strip()
                        changed = True
                if changed:
                    save_data(data)
                    success("Account updated successfully!")
                    del st.session_state["update_user_acc"]
                    del st.session_state["update_user_pin"]

# ═══════════════════════════════════════════════════════════════════════════════
# 6. DELETE ACCOUNT
# ═══════════════════════════════════════════════════════════════════════════════
elif "Delete" in page:
    st.subheader("Delete Account")
    st.markdown("---")
    st.warning("⚠️ This action is permanent and cannot be undone.")

    acc, pin = auth_fields()

    if st.button("Verify Account"):
        user = find_user(data, acc, pin)
        if not user:
            error("Invalid account number or PIN.")
        else:
            st.session_state["del_acc"] = acc
            st.session_state["del_pin"] = pin
            st.session_state["del_name"] = user["name"]

    if "del_acc" in st.session_state:
        st.markdown("---")
        st.markdown(f'<div class="msg-error">You are about to delete the account of <strong>{st.session_state["del_name"]}</strong>.</div>', unsafe_allow_html=True)
        confirm = st.checkbox("I understand this action is irreversible")

        if st.button("Permanently Delete Account") and confirm:
            user = find_user(data, st.session_state["del_acc"], st.session_state["del_pin"])
            if user:
                data.remove(user)
                save_data(data)
                success("Account deleted successfully.")
                for key in ["del_acc", "del_pin", "del_name"]:
                    if key in st.session_state:
                        del st.session_state[key]
        elif st.button("Cancel"):
            for key in ["del_acc", "del_pin", "del_name"]:
                if key in st.session_state:
                    del st.session_state[key]