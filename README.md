# 🏦 Banking Management System  

| 📖 Section | 📝 Details |
|------------|------------|
| **Project Name** | 🏦 Banking Management System |
| **Description** | 💳 A Python 🐍 console-based application that allows users to:<br>• Create new accounts<br>• Login as existing users<br>• Credit & Debit amounts<br>• Check account balance<br>• Delete account<br><br>All data is stored in a **nested dictionary 📂**. |
| **Data Structure** | ```python<br>users = {<br>    1001: {"Name": "Alice", "Phone": "9876543210", "PIN": 1234, "Balance": 5000},<br>    1002: {"Name": "Bob", "Phone": "9123456780", "PIN": 5678, "Balance": 3000}<br>}<br>``` |
| **New User Flow** | ✍️ Enter your **Name** + 📱 Phone Number → 🔢 System auto-generates **Account Number** + **PIN** → 💰 Balance starts at `0` |
| **Existing User Flow** | 🔑 Enter **Account Number** + **PIN** → Access operations menu |

---

# 🌟 Features  

| Option | Operation | Description |
|--------|------------|-------------|
| 1️⃣ | ➕ Credit Amount | Add money to the account |
| 2️⃣ | ➖ Debit Amount | Withdraw money if balance is sufficient |
| 3️⃣ | 📊 Check Balance | Display current balance |
| 4️⃣ | ❌ Delete Account | Remove the account permanently |
| 5️⃣ | 🏠 Home Page | Return to main menu |

---

# 🛠️ Technology Used  

| 🔧 Tool | 💡 Purpose |
|---------|------------|
| 🐍 Python | Core programming language |
| 📂 Nested Dictionary | Data storage of account details |

---

# 📋 How It Works  

| Step | Action |
|------|---------|
| 1️⃣ | Run the program |
| 2️⃣ | Select option → `1` (Existing User) or `2` (New User) |
| 3️⃣ | For **new user** → Enter Name + Phone Number → System generates **Account Number + PIN**, Balance = 0 |
| 4️⃣ | For **existing user** → Enter Account Number + PIN |

<img width="647" height="882" alt="image" src="https://github.com/user-attachments/assets/d0293bf3-aee1-426c-83bf-7a7a37d5bc76" />



| 5️⃣ | Access **Menu** (Credit, Debit, Check Balance, Delete, Home) |
| 6️⃣
