def calculate_total_rent(
    base_rent,
    maintenance=0,
    water=0,
    electricity=0,
    gas=0,
    parking=0,
    discount=0,
    tax_percent=0,
    late_fee=0
):
    subtotal = (base_rent + maintenance + water + electricity + gas + parking)
    tax_amount = subtotal * (tax_percent / 100)
    total_before_discount = subtotal + tax_amount
    final_total = total_before_discount - discount + late_fee
    return subtotal, tax_amount, total_before_discount, final_total

def save_bill_to_file(data):
    with open("rent_bill.txt", "a", encoding="utf-8") as f:
        f.write("\n" + "="*50 + "\n")
        f.write("          MONTHLY RENT BILL\n")
        f.write("="*50 + "\n")
        f.write(f"Base Rent           : {data['base_rent']}\n")
        f.write(f"Maintenance         : {data['maintenance']}\n")
        f.write(f"Water Bill          : {data['water']}\n")
        f.write(f"Electricity Bill    : {data['electricity']}\n")
        f.write(f"Gas Bill            : {data['gas']}\n")
        f.write(f"Parking Charge      : {data['parking']}\n")
        f.write(f"Subtotal            : {data['subtotal']}\n")
        f.write(f"Tax ({data['tax_percent']}%)       : {data['tax_amount']}\n")
        f.write(f"Discount Applied    : {data['discount']}\n")
        f.write(f"Late Fee            : {data['late_fee']}\n")
        f.write("-"*50 + "\n")
        f.write(f"FINAL TOTAL TO PAY  : {data['final_total']}\n")
        f.write("="*50 + "\n\n")
    print("\n✅ Bill saved to rent_bill.txt")

def show_annual_estimate(final_rent):
    annual = final_rent * 12
    print(f"\n📅 Annual Rent Estimate : {annual}")

def security_deposit(base_rent):
    deposit = base_rent * 2
    print(f"🔒 Security Deposit (2x rent) : {deposit}")

def main():
    print("===== HEX SOFTWARES - ADVANCED RENT CALCULATOR =====")
    print("Please enter all required details below:\n")

    base_rent = float(input("Base Rent                     : "))
    maintenance = float(input("Maintenance Charge            : "))
    water = float(input("Water Bill                    : "))
    electricity = float(input("Electricity Bill              : "))
    gas = float(input("Gas Bill (0 if none)          : "))
    parking = float(input("Parking Charge (0 if none)    : "))
    tax_percent = float(input("Tax Percentage (e.g., 5)      : "))
    discount = float(input("Discount Amount               : "))
    late_fee = float(input("Late Fee (0 if none)          : "))

    subtotal, tax_amount, total_before_discount, final_total = calculate_total_rent(
        base_rent, maintenance, water, electricity, gas, parking,
        discount, tax_percent, late_fee
    )

    bill_data = {
        "base_rent": base_rent,
        "maintenance": maintenance,
        "water": water,
        "electricity": electricity,
        "gas": gas,
        "parking": parking,
        "tax_percent": tax_percent,
        "discount": discount,
        "late_fee": late_fee,
        "subtotal": subtotal,
        "tax_amount": round(tax_amount, 2),
        "final_total": round(final_total, 2)
    }

    print("\n" + "="*50)
    print("          FINAL RENT BILL")
    print("="*50)
    print(f"Base Rent           : {base_rent}")
    print(f"Maintenance         : {maintenance}")
    print(f"Water Bill          : {water}")
    print(f"Electricity Bill    : {electricity}")
    print(f"Gas Bill            : {gas}")
    print(f"Parking Charge      : {parking}")
    print(f"Subtotal            : {subtotal}")
    print(f"Tax ({tax_percent}%)           : {round(tax_amount, 2)}")
    print(f"Discount Applied    : {discount}")
    print(f"Late Fee            : {late_fee}")
    print("-"*50)
    print(f"FINAL TOTAL TO PAY  : {round(final_total, 2)}")
    print("="*50)

    security_deposit(base_rent)
    show_annual_estimate(final_total)
    save_bill_to_file(bill_data)

if __name__ == "__main__":
    main()
