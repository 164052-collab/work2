import math

# ประวัติการคำนวณ
history = []

def show_menu():
    print("\n" + "="*40)
    print("   โปรแกรมคำนวณพื้นที่รูปทรงหลายแบบ")
    print("="*40)
    print("1. สี่เหลี่ยมมุมฉาก")
    print("2. จัตุรัส")
    print("3. สามเหลี่ยม")
    print("4. วงกลม")
    print("5. สี่เหลี่ยมคางหมู")
    print("6. ดูประวัติการคำนวณ")
    print("0. ออกจากโปรแกรม")
    print("="*40)

def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("  กรุณากรอกตัวเลขที่มากกว่า 0")
            else:
                return value
        except ValueError:
            print("  กรุณากรอกตัวเลขเท่านั้น")

def calc_rect():
    print("\n--- สี่เหลี่ยมมุมฉาก ---")
    กว้าง = get_number("กรอกความกว้าง: ")
    ยาว  = get_number("กรอกความยาว : ")
    พื้นที่ = กว้าง * ยาว
    print(f"สูตร    : กว้าง × ยาว = {กว้าง} × {ยาว}")
    print(f"พื้นที่  : {พื้นที่:.2f} ตารางหน่วย")
    history.append(f"สี่เหลี่ยมมุมฉาก ({กว้าง}×{ยาว}) = {พื้นที่:.2f}")

def calc_square():
    print("\n--- จัตุรัส ---")
    ด้าน = get_number("กรอกความยาวด้าน: ")
    พื้นที่ = ด้าน ** 2
    print(f"สูตร    : ด้าน² = {ด้าน}²")
    print(f"พื้นที่  : {พื้นที่:.2f} ตารางหน่วย")
    history.append(f"จัตุรัส (ด้าน={ด้าน}) = {พื้นที่:.2f}")

def calc_triangle():
    print("\n--- สามเหลี่ยม ---")
    ฐาน = get_number("กรอกความยาวฐาน  : ")
    สูง  = get_number("กรอกความสูง     : ")
    พื้นที่ = 0.5 * ฐาน * สูง
    print(f"สูตร    : ½ × ฐาน × สูง = ½ × {ฐาน} × {สูง}")
    print(f"พื้นที่  : {พื้นที่:.2f} ตารางหน่วย")
    history.append(f"สามเหลี่ยม (ฐาน={ฐาน}, สูง={สูง}) = {พื้นที่:.2f}")

def calc_circle():
    print("\n--- วงกลม ---")
    รัศมี = get_number("กรอกรัศมี: ")
    พื้นที่ = math.pi * รัศมี ** 2
    print(f"สูตร    : π × r² = π × {รัศมี}²")
    print(f"พื้นที่  : {พื้นที่:.2f} ตารางหน่วย")
    history.append(f"วงกลม (r={รัศมี}) = {พื้นที่:.2f}")

def calc_trapezoid():
    print("\n--- สี่เหลี่ยมคางหมู ---")
    a   = get_number("กรอกด้านขนาน a: ")
    b   = get_number("กรอกด้านขนาน b: ")
    สูง = get_number("กรอกความสูง   : ")
    พื้นที่ = 0.5 * (a + b) * สูง
    print(f"สูตร    : ½ × (a+b) × สูง = ½ × ({a}+{b}) × {สูง}")
    print(f"พื้นที่  : {พื้นที่:.2f} ตารางหน่วย")
    history.append(f"คางหมู (a={a}, b={b}, สูง={สูง}) = {พื้นที่:.2f}")

def show_history():
    print("\n--- ประวัติการคำนวณ ---")
    if not history:
        print("ยังไม่มีประวัติ")
    else:
        for i, item in enumerate(history, 1):
            print(f"{i}. {item}")

# ลูปหลักของโปรแกรม
actions = {
    "1": calc_rect,
    "2": calc_square,
    "3": calc_triangle,
    "4": calc_circle,
    "5": calc_trapezoid,
    "6": show_history,
}

while True:
    show_menu()
    choice = input("เลือกเมนู (0-6): ").strip()
    if choice == "0":
        print("ขอบคุณที่ใช้งานโปรแกรม!")
        break
    elif choice in actions:
        actions[choice]()
    else:
        print("กรุณาเลือก 0-6 เท่านั้น")