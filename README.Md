# 🏦 BharatBank — Python Banking Management System

A simple yet fully functional **Bank Management System** built in Python, featuring both a **CLI version** (`Main.py`) and a polished **Streamlit web UI** (`Ui.py`). Data is stored locally in a JSON file — no database setup needed.

---

## ✨ Features

- 🆕 **Open Account** — Create a new bank account with name, age, email, and a 4-digit PIN
- 💰 **Deposit Money** — Add funds to any account securely using account number + PIN
- 💸 **Withdraw Money** — Withdraw funds with balance validation
- 👁️ **View Account Details** — See name, email, age, account number, and current balance
- ✏️ **Update Details** — Change name, email, or PIN after authentication
- 🗑️ **Close Account** — Permanently delete an account (with confirmation)

---

## 📁 Project Structure

```
BharatBank/
│
├── Main.py                  # CLI-based banking application
├── Ui.py                    # Streamlit web UI (BharatBank)
├── bharatbank_db.json       # JSON database (auto-created on first run)
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/BharatBank.git
   cd BharatBank
   ```

2. **Install dependencies** (only needed for the web UI)
   ```bash
   pip install streamlit
   ```

---

## ▶️ Running the App

### Option 1 — Web UI (Recommended)

```bash
streamlit run Ui.py
```

Then open your browser at `http://localhost:8501`

### Option 2 — Command Line Interface

```bash
python Main.py
```

Follow the on-screen menu prompts.

---

## 🖥️ Web UI Preview

The Streamlit UI features:
- Indian-themed design (saffron, navy, green palette)
- Sidebar navigation
- Secure PIN-masked inputs
- Real-time success/error banners
- Responsive card-based account detail view

---

## 🗄️ Database

User data is stored in a local JSON file (`bharatbank_db.json`). Each record looks like:

```json
{
  "name": "Ravi Kumar",
  "age": 25,
  "email": "ravi@example.com",
  "AccountNo": "BB5062MQOY8300",
  "pin": 1234,
  "balance": 5000
}
```

> ⚠️ **Note:** PINs are stored in plain text in the JSON file. This project is intended for learning purposes only — do not use it for real financial data.

---

## ⚙️ Account Number Format

Account numbers are auto-generated in the format:

```
BB + [8 alphanumeric characters] + [4 digits]  →  e.g. BB5062MQOY8300
```

---

## 📋 CLI Menu Options

```
Press 1 → Create Account
Press 2 → Deposit Money
Press 3 → Withdraw Money
Press 4 → View Account Details
Press 5 → Update Account Details
Press 6 → Delete Account
Press 0 → Exit
```

---

## 🛡️ Validation Rules

| Rule | Detail |
|---|---|
| Minimum age | 12 years |
| PIN format | Exactly 4 digits |
| Withdrawal | Cannot exceed current balance |
| Account closure | Requires manual confirmation |

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/NewFeature`)
3. Commit your changes (`git commit -m 'Add NewFeature'`)
4. Push to the branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

Made with ❤️ in **Indore, Madhya Pradesh, India**

> *BharatBank · Regulated by RBI · Member DICGC · Deposits insured up to ₹5,00,000*