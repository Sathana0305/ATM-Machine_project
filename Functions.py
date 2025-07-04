accounts = []
def create_account(name, acc_id, email, password):
    account = {
        "name": name,
        "id": acc_id,
        "email": email,
        "pin": password,
        "balance": 0
    }
    accounts.append(account)
    return account
def find_account_by_id(acc_id):
    for acc in accounts:
        if acc["id"] == acc_id:
            return acc
    return None
def find_ids_by_email(email):
    return [acc["id"] for acc in accounts if acc["email"].lower() == email.lower()]
def withdraw_money(account, amount):
    if amount <= 0:
        return "Invalid amount"
    if account["balance"] >= amount:
        account["balance"] -= amount
        return f"₹{amount} withdrawn. Remaining balance: ₹{account['balance']}"
    else:
        return "Insufficient balance"
def deposit_money(account, amount):
    if amount <= 0:
        return "Invalid amount"
    account["balance"] += amount
    return f"₹{amount} deposited. Total balance: ₹{account['balance']}"
def reset_password(account, new_password):
    account["pin"] = new_password
