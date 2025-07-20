from pywebio.input import *
from pywebio.output import *
from pywebio.session import run_js
from pywebio.session import eval_js
from pywebio import start_server
from pywebio.session import *
import smtplib
from email.message import EmailMessage
from pywebio.output import put_text
categories = {
    "Shirts": [
        {"name": "Black T-Shirt", "price": 599, "stock": 6, "img": "https://www.bing.com/th?id=OPAC.kJGZwywZZcvmIQ474C474&o=5&pid=21.1&w=160&h=240&rs=1&qlt=100&dpr=0.9&o=2&c=8&pcl=f5f5f5"},
        {"name": "White Shirt", "price": 7959, "stock": 5, "img": "https://image.hm.com/assets/hm/d8/44/d8448609077aab2dc0d837df8cdd9625816e6e42.jpg?imwidth=1260"},
        {"name": "The Short Sleeve T-Shirt", "price": 799, "stock": 5, "img": "https://www.thefashionisto.com/wp-content/uploads/2023/07/Types-of-Shirts-Men-White-T-Shirt.jpg"},
        {"name": "The Pocket Tee", "price": 7939, "stock": 5, "img": "https://www.thefashionisto.com/wp-content/uploads/2023/07/Types-of-Shirts-Men-Pocket-T-Shirt-UNIQLO-Orange.jpg"},
        {"name": "Red Hoodie", "price": 9939, "stock": 10, "img": "data:image/jpeg;base64,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"},
        {"name": "The Polo Shirt", "price": 7969, "stock": 5, "img": "https://www.thefashionisto.com/wp-content/uploads/2023/07/Types-of-Shirts-Men-Polo-Shirt-Abercrombie-Fitch.jpg"},
        {"name": "The Button-Down Shirt", "price": 7969, "stock": 50, "img": "https://www.thefashionisto.com/wp-content/uploads/2023/07/Types-of-Shirts-Men-Button-down.jpg"},
        {"name": "The Chambray Shirt", "price": 9499, "stock": 57, "img": "https://www.thefashionisto.com/wp-content/uploads/2023/07/Types-of-Shirts-Men-Chambray-Theory.jpg"},
        {"name": "The Flannel Shirt", "price": 799, "stock": 75, "img": "https://www.thefashionisto.com/wp-content/uploads/2023/07/Types-of-Shirts-Men-Flannel.jpg"},
        {"name": "The Denim Shirt", "price": 8939, "stock": 15, "img": "https://www.thefashionisto.com/wp-content/uploads/2023/07/Types-of-Shirts-Men-Denim.jpg"},
        {"name": "The Flannel Shirt", "price": 799, "stock": 25, "img": "https://www.thefashionisto.com/wp-content/uploads/2023/07/Types-of-Shirts-Men-Flannel.jpg"},
        {"name": "The Denim Shirt", "price": 499, "stock": 35, "img": "https://www.thefashionisto.com/wp-content/uploads/2023/07/Types-of-Shirts-Men-Denim.jpg"},
    ],
    "Sneakers": [
        {"name": "Nike Air Max", "price": 3299, "stock": 5, "img": "https://www.bing.com/th?id=OPAC.%2bTZx2Rm0vIRWWg474C474&o=5&pid=21.1&w=148&h=148&rs=1&qlt=100&dpr=0.9&o=2&bw=6&bc=FFFFFF"},
        {"name": "Adidas Sneakers", "price": 2899, "stock": 4, "img": "data:image/webp;base64,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"},
        {"name": "Puma Running", "price": 2699, "stock": 3, "img": "https://th.bing.com/th/id/OIP.ccdIR7fwmzpoAH4LeyYX0AHaJT?w=137&h=180&c=7&r=0&o=7&pid=1.7&rm=3"},
        {"name": "Converse-Canvas-Sneakers", "price": 2699, "stock": 3, "img": "https://www.thefashionisto.com/wp-content/uploads/2024/03/Converse-Canvas-Sneakers.jpg"},
        {"name": "adidas-Stan-Smith-Leather-Sneakers", "price": 2699, "stock": 3, "img": "https://www.thefashionisto.com/wp-content/uploads/2024/03/adidas-Stan-Smith-Leather-Sneakers.jpg"},
        {"name": "Running-Sneakers", "price": 2699, "stock": 3, "img": "https://www.thefashionisto.com/wp-content/uploads/2024/03/Asics-Running-Sneakers.jpg"},
        {"name": "Training-Sneakers", "price": 2699, "stock": 3, "img": "https://www.thefashionisto.com/wp-content/uploads/2024/03/adidas-Training-Sneakers.jpg"},
        {"name": "Nike-High-Top-Sneakers-Basketball", "price": 2699, "stock": 3, "img": "https://www.thefashionisto.com/wp-content/uploads/2024/03/Nike-High-Top-Sneakers-Basketball.jpg"},
        {"name": "Skateboard-Shoes", "price": 2699, "stock": 3, "img": "https://www.thefashionisto.com/wp-content/uploads/2024/03/Vans-Skateboard-Shoes.jpg"},
        {"name": "Sneaker Boots", "price": 2699, "stock": 3, "img": "https://www.thefashionisto.com/wp-content/uploads/2024/03/Vans-Sneaker-Boots.jpg"},
        {"name": "Skateboard-Shoes", "price": 2699, "stock": 3, "img": "https://www.thefashionisto.com/wp-content/uploads/2024/03/Vans-Skateboard-Shoes.jpg"},
        {"name": "Sneaker Boots", "price": 2699, "stock": 3, "img": "https://www.thefashionisto.com/wp-content/uploads/2024/03/Vans-Sneaker-Boots.jpg"},
    ],
    "Skin Products": [
        {"name": "Clinique Face Wash for men", "price": 349, "stock": 8, "img": "https://a.cdnsbn.com/images/products/l/27077080421.jpg"},
        {"name": "Beardo FaceCream", "price": 699, "stock": 5, "img": "data:image/webp;base64,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"},
        {"name": "Garnier Moisturizer", "price": 599, "stock": 6, "img": "data:image/webp;base64,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"},
        {"name": "Mama Earth Ubtan Face Wash", "price": 349, "stock": 8, "img": "https://www.bing.com/th?id=OPAC.xYCsM6kgLQ26lg474C474&o=5&pid=21.1&w=148&h=223&rs=1&qlt=100&dpr=0.9&o=2&bw=6&bc=FFFFFF"},
        {"name": "Pilgrim korean foaming face wash", "price": 349, "stock": 8, "img": "https://www.bing.com/th?id=OPAC.fVqWR3rb6eHwrw474C474&o=5&pid=21.1&w=160&h=235&rs=1&qlt=100&dpr=0.9&o=2&pcl=f5f5f5"},
        {"name": "Himalaya face wash", "price": 349, "stock": 8, "img": "https://ts2.mm.bing.net/th?id=OIP.EugVR-vamHLXa2p0auPpzAHaHa&pid=15.1"},
        {"name": "Moisturizing Face Wash (For Dry Skin)", "price": 349, "stock": 8, "img": "https://img.mensxp.com/media/shop/catalog/products/M/717795/moisturizing-face-wash-for-dry-skin-100-ml-55257-default.jpg?w=345&h=551&cc=1"},
        {"name": "De-Tan Face Scrub With Kakadu Plum and Sepiwhite", "price": 349, "stock": 8, "img": "https://img.mensxp.com/media/shop/catalog/products/F/face-moisturiser-1-1628165206-1641806831.jpeg?w=345&h=551&cc=1"},
        {"name": "Satthwa 100% Pure Cold Pressed Carrier Argan Oil for Hair, Face & Skin (30 ml)", "price": 349, "stock": 8, "img": "https://img.mensxp.com/media/shop/catalog/products/S/779513/satthwa-100-pure-cold-pressed-carrier-argan-oil-for-hair-face-and-skin-30-ml-72153-default.jpg?w=345&h=551&cc=1"}, 
    ]}


orders=[]
# Common Style
def set_black_theme():
    put_html('''
    <style>
        body {
            margin: 0;
            font-family: 'Segoe UI', sans-serif;
            background-color: #fff0f5;
        }
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: white;
            padding: 12px 40px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.08);
        }
        .navbar h1 {
            color: #222;
            font-size: 26px;
            font-weight: bold;
        }
        .navbar h1 span {
            color: #f06292;
        }
        .navbar .actions button {
            margin-left: 15px;
            padding: 8px 16px;
            background-color: #f06292;
            color: white;
            border: none;
            border-radius: 20px;
            cursor: pointer;
            font-size: 14px;
        }
        .hero {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 60px 80px;
            background: linear-gradient(to right, #ffeef5, #fff0f5);
        }
        .hero-text {
            max-width: 600px;
        }
        .hero-text h1 {
            font-size: 50px;
            font-weight: bold;
            color: #222;
        }
        .hero-text h1 span {
            color: #2196f3;
        }
        .hero-text h2 {
            font-size: 26px;
            color: #e91e63;
            margin-top: 10px;
        }
        .hero-text p {
            color: #777;
            line-height: 1.6;
            margin: 20px 0;
        }
        .hero-text button {
            padding: 12px 25px;
            font-size: 16px;
            background-color: #111;
            color: white;
            border: none;
            border-radius: 25px;
            cursor: pointer;
        }
        .hero-img img {
            width: 460px;
            border-radius: 10px;
            animation: slideFade 8s infinite alternate;
        }

        @keyframes slideFade {
            0% {opacity: 0.6; transform: scale(1);}
            50% {opacity: 1; transform: scale(1.03);}
            100% {opacity: 0.6; transform: scale(1);}
        }

        @media screen and (max-width: 768px) {
            .hero {
                flex-direction: column;
                text-align: center;
                padding: 30px 20px;
            }
            .hero-img img {
                width: 100%;
                margin-top: 20px;
            }
        }
    </style>''')

def show_orders():
    clear()
    set_black_theme()

    put_html("<h2 style='color:#ffc107; text-align:center;'>📦 Your Orders</h2>")

    if not orders:
        put_html("""
            <div style="text-align:center; margin-top:20px;">
                <img src="https://cdn-icons-png.flaticon.com/512/2038/2038854.png" width="160px"><br><br>
                <p style="color:white;">No previous orders found.</p>
                <button onclick="PyWebIO.pushData('home')" 
                    style="padding:10px 25px; background:#007bff; color:white; border:none; border-radius:8px; font-weight:bold;">
                    🏠 Back to Home
                </button>
            </div>
        """)
        action = eval_js("new Promise(resolve => {window.PyWebIO.pushData = resolve;})")
        if action == 'home':
            home_page()
        return

    for order in orders:
        put_html("<hr style='border:1px solid #444;'>")
        put_html(f"""
            <div style='color:white; padding:10px; text-align:center;'>
                <b>Total:</b> ₹{order['total']}<br>
                <b>Payment:</b> {order['method']}<br>
                <b>Address:</b> {order['address']}
            </div>
        """)
        put_html("<div style='display:flex; flex-wrap:wrap; justify-content:center; gap:20px;'>")
        for item in order["items"]:
            put_html(f"""
                <div style='background:#111; padding:10px; border-radius:10px; color:white; width:200px; text-align:center;'>
                    <img src='{item["img"]}' width='100' style='border-radius:8px;'><br><br>
                    <b>{item["name"]}</b><br>
                    ₹{item["price"]}
                </div>
            """)
        put_html("</div>")

    put_html("""
        <div style='text-align:center; margin-top:30px;'>
            <button onclick="PyWebIO.pushData('home')" 
                style="padding:10px 25px; background:#007bff; color:white; border:none; border-radius:8px; font-weight:bold;">
                🏠 Back to Home
            </button>
        </div>
    """)
    action = eval_js("new Promise(resolve => {window.PyWebIO.pushData = resolve;})")
    if action == 'home':
        home_page()

# Apply coupon
def apply_coupon():
    clear()
    set_black_theme()

    put_html("""
        <div style="background:#1e1e1e; padding:30px; border-radius:10px; color:white; text-align:center;">
            <h2>🎟️ Apply Coupon</h2>
            <p style="color:#ccc;">Enter your coupon code below:</p>
            <input id="coupon_input" type="text" placeholder="Enter coupon code"
                style="padding:10px; width:70%; border-radius:5px; border:none; background:#000; color:white;"><br><br>

            <div style="display:flex; justify-content:center; gap:20px;">
                <button onclick="
                    let code = document.getElementById('coupon_input').value;
                    if(code.trim() === '') alert('❌ Please enter a coupon code');
                    else PyWebIO.pushData(code);
                "
                style="padding:10px 20px; background:#007bff; color:white; border:none; border-radius:5px;">
                    Apply
                </button>

                <button onclick="PyWebIO.pushData('home')"
                    style="padding:10px 20px; background:#28a745; color:white; border:none; border-radius:5px;">
                    🏠 Back to Home
                </button>
            </div>
        </div>
    """)

    # Wait for either "Apply" (coupon code) or "home"
    code = eval_js("new Promise(resolve => {window.PyWebIO=window.PyWebIO||{}; PyWebIO.pushData=resolve;})")

    if code == "home":
        home_page()
        return

    if code.strip().lower() == "save10":
        put_html("<h4 style='color:lightgreen;'>✅ Coupon applied! You get 10% off.</h4>")
    else:
        put_html("<h4 style='color:red;'>❌ Invalid coupon code.</h4>")

cart = []
user = "guest"
users = {}
wallet_balance = 1000  

def is_valid_upi(upi_id):
    return "@" in upi_id and len(upi_id.split("@")[0]) >= 3

def collect_address():
    put_html("""
        <div style="background:#1e1e1e; color:white; padding:20px; border-radius:10px; margin-top:20px;">
            <h3>Enter Delivery Address and Email</h3>
            <input name='name' placeholder='Name' style='background:black;color:white;padding:10px;border:none;width:90%;margin-bottom:10px;border-radius:5px;'><br>
            <input name='door' placeholder='Door No.' style='background:black;color:white;padding:10px;border:none;width:90%;margin-bottom:10px;border-radius:5px;'><br>
            <input name='street' placeholder='Street' style='background:black;color:white;padding:10px;border:none;width:90%;margin-bottom:10px;border-radius:5px;'><br>
            <input name='district' placeholder='District' style='background:black;color:white;padding:10px;border:none;width:90%;margin-bottom:10px;border-radius:5px;'><br>
            <input name='state' placeholder='State' style='background:black;color:white;padding:10px;border:none;width:90%;margin-bottom:10px;border-radius:5px;'><br>
            <input name='email' placeholder='Email' type='email' style='background:black;color:white;padding:10px;border:none;width:90%;margin-bottom:10px;border-radius:5px;'><br>
            <button onclick="
                let values = ['name', 'door', 'street', 'district', 'state', 'email'].map(n => document.getElementsByName(n)[0].value);
                if(values.some(v => v.trim() === '')) alert('❌ Please fill all fields');
                else PyWebIO.pushData(values);
            " style='background:#28a745;color:white;padding:10px 20px;border:none;border-radius:5px;'>Submit</button>
        </div>
    """)
    
    data = eval_js("new Promise(resolve => {window.PyWebIO=window.PyWebIO||{}; PyWebIO.pushData=resolve;})")
    if not data or len(data) != 6:
        put_html("<h4 style='color:red;'>❌ Failed to collect address. Please try again.</h4>")
        return None

    return {
        'name': data[0],
        'door': data[1],
        'street': data[2],
        'district': data[3],
        'state': data[4],
        'email': data[5]
    }


import smtplib
from email.message import EmailMessage
from pywebio.output import put_text

def send_email(user_email, subject, body):
    from_email = "vijayvijayvijay282@gmail.com"  
    app_password = "ibttuxuskqjkkyup"  

    try:
        recipients = [user_email, from_email]  
        msg = EmailMessage()
        msg["From"] = from_email
        msg["To"] = ", ".join(recipients)
        msg["Subject"] = subject
        msg.set_content(body)

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(from_email, app_password)
            server.send_message(msg)

        put_text("✅ Confirmation email sent to user and admin!")

    except Exception as e:
        put_text(f"❌ Failed to send email: {e}")
def process_payment(amount):
    mode = radio("Select Payment Mode", options=["UPI", "Wallet", "Cash on Delivery"], required=True)
    
    if mode == "UPI":
        upi_id = input("Enter your UPI ID", type=TEXT, required=True)
        if not is_valid_upi(upi_id):
            toast("Invalid UPI ID!", color="error")
            return False
        toast(f"₹{amount} paid via UPI: {upi_id}", color="success")
        return True

    elif mode == "Wallet":
        global wallet_balance
        if wallet_balance >= amount:
            wallet_balance -= amount
            toast(f"₹{amount} deducted from Wallet. Remaining: ₹{wallet_balance}", color="success")
            return True
        else:
            toast("Insufficient wallet balance!", color="error")
            return False

    elif mode == "Cash on Delivery":
        toast(f"Order of ₹{amount} placed with COD.", color="success")
        return True 
def view_cart():
    global cart, wallet_balance, orders
    clear()
    set_black_theme()

    put_html("<h2 style='color:#ffc107;'>🛒 Your Cart</h2>")

    if not cart:
        put_image("https://th.bing.com/th/id/OIP.KdQaeEbw5-cYnyTcHjBMKwHaFv?w=266&h=207", width="180px")
        put_text("Your cart is empty!")
        put_buttons(["🏠 Back to Home"], [home_page])
        return
    total = sum(item["price"] for item in cart)

    for item in cart:
        put_html(f"""
            <div style='margin:10px;padding:10px;border:1px solid #333;border-radius:10px;background:#111;color:white;'>
                <img src='{item["img"]}' width='100'><br>
                <b>{item["name"]}</b><br>₹{item["price"]}
            </div>
        """)

    put_html(f"<h4 style='color:white;'>🧾 Total Amount: ₹{total}</h4>")

    # Confirm purchase
    put_html("""
        <div style="background:#222;padding:20px;border-radius:10px;margin-top:10px;">
            <h3 style='color:white;text-align:center;'>Do you want to proceed to purchase?</h3>
            <div style='text-align:center;'>
                <button onclick="PyWebIO.pushData('Yes')" style='margin-right:10px;padding:10px 20px;background:#007bff;color:white;border:none;border-radius:5px;'>Yes</button>
                <button onclick="PyWebIO.pushData('No')" style='padding:10px 20px;background:#007bff;color:white;border:none;border-radius:5px;'>No</button>
            </div>
        </div>
    """)
    decision = eval_js("new Promise(resolve => {window.PyWebIO.pushData=resolve;})")
    if decision != "Yes":
        return
    # Choose payment method
    put_html("""
        <div style='margin-top:20px;padding:20px;background:#1e1e1e;border-radius:10px;color:white;'>
            <h3>Select Payment Method</h3>
            <label><input type="radio" name="pay" value="UPI"> UPI</label><br>
            <label><input type="radio" name="pay" value="Wallet"> Wallet</label><br>
            <label><input type="radio" name="pay" value="COD"> Cash on Delivery</label><br><br>
            <button onclick="PyWebIO.pushData(document.querySelector('input[name=pay]:checked')?.value || '')"
                    style='padding:10px 20px;background:#007bff;color:white;border:none;border-radius:5px;font-weight:bold;'>
                Proceed
            </button>
        </div>
    """)
    payment_method = eval_js("new Promise(resolve => {window.PyWebIO.pushData=resolve;})")

    if payment_method not in ['UPI', 'Wallet', 'COD']:
        put_html("<h4 style='color:red;'>❌ Please select a payment method.</h4>")
        return

    upi_id = ""
    if payment_method == "UPI":
        put_html("""
            <div style="background:#1e1e1e;color:white;padding:20px;border-radius:10px;margin-top:20px;">
                <h3>Enter your UPI ID</h3>
                <input id="upiInput" type="text" placeholder="example@upi"
                       style="padding:10px;width:80%;border-radius:5px;border:none;margin-top:10px;"><br><br>
                <button onclick="
                    let val = document.getElementById('upiInput').value;
                    if(val.includes('@')) PyWebIO.pushData(val);
                    else alert('❌ Invalid UPI format. Must contain @');
                "
                style="padding:10px 20px;background:#007bff;color:white;border:none;border-radius:5px;">Submit</button>
            </div>
        """)
        upi_id = eval_js("new Promise(resolve => {window.PyWebIO.pushData=resolve;})")

    elif payment_method == "Wallet":
        if wallet_balance < total:
            put_text(f"❌ Insufficient wallet balance. Available: ₹{wallet_balance}")
            return
        wallet_balance -= total
    put_html("""
        <div style="background:#1e1e1e;color:white;padding:20px;border-radius:10px;margin-top:20px;">
            <h3>Enter Delivery Address</h3>
            <input name='name' placeholder='Name' style='background:black;color:white;padding:10px;width:90%;margin-bottom:10px;border-radius:5px;'><br>
            <input name='email' placeholder='Email' style='background:black;color:white;padding:10px;width:90%;margin-bottom:10px;border-radius:5px;'><br>
            <input name='door' placeholder='Door No' style='background:black;color:white;padding:10px;width:90%;margin-bottom:10px;border-radius:5px;'><br>
            <input name='street' placeholder='Street' style='background:black;color:white;padding:10px;width:90%;margin-bottom:10px;border-radius:5px;'><br>
            <input name='district' placeholder='District' style='background:black;color:white;padding:10px;width:90%;margin-bottom:10px;border-radius:5px;'><br>
            <input name='state' placeholder='State' style='background:black;color:white;padding:10px;width:90%;margin-bottom:10px;border-radius:5px;'><br>
            <button onclick="
                let inputs = ['name', 'email', 'door', 'street', 'district', 'state'].map(n => document.getElementsByName(n)[0].value);
                if(inputs.some(v => v.trim() === '')) alert('❌ Please fill all fields');
                else PyWebIO.pushData(inputs);
            " style='background:#28a745;color:white;padding:10px 20px;border:none;border-radius:5px;'>Submit</button>
        </div>
    """)
    address_data = eval_js("new Promise(resolve => {window.PyWebIO.pushData=resolve;})")

    if not address_data or len(address_data) != 6:
        put_html("<h4 style='color:red;'>❌ Failed to collect address. Please try again.</h4>")
        put_buttons(["🏠 Back to Home"], [home_page])
        return

    name, email, door, street, district, state = address_data
    full_address = f"{door}, {street}, {district}, {state}"

    # Save order
    orders.append({
        "items": cart.copy(),
        "total": total,
        "method": payment_method,
        "address": full_address,
        "upi": upi_id if payment_method == "UPI" else None,
        "email": email
    })

    # Send email
    email_body = f"""Hi {name},

Your order has been placed successfully!

Items:
""" + "\n".join([f" - {item['name']} (₹{item['price']})" for item in cart]) + f"""

Total: ₹{total}
Payment Mode: {payment_method}
Delivery Address: {full_address}

Thanks for shopping with us!
- ShopNStyle
"""
    
    send_email(email, "🛍️ ShopNStyle Order Confirmation", email_body)

    cart.clear()
    put_html("<h3 style='color:#90ee90;'>✅ Order Placed Successfully!</h3>")
    put_text(f"Amount Paid: ₹{total}")
    put_text(f"Delivery Address: {full_address}")
    put_text(f"Payment Method: {payment_method}" + (f" (UPI: {upi_id})" if payment_method == "UPI" else ""))
    put_text("Thank you for shopping with us!")
    put_buttons(["🏠 Back to Home"], [home_page])
# Product detail
def show_item_info(item):
    clear()
    set_black_theme()
    put_html(f"<h2>📝 {item['name']}</h2>")
    put_image(item['img'], width='200px')
    put_text(f"Price: ₹{item['price']}")
    put_text(f"Stock: {item['stock']}")
    put_buttons(["Add to Cart", "🏠 Back"], [lambda: add_to_cart(item), home_page])

# Add to cart
def add_to_cart(item):
    cart.append(item)
    popup("✅ Added", f"{item['name']} added to cart.")
    close_popup()
def show_product_detail(product):
    clear()
    set_black_theme()
    put_html(f"""
    <div style="text-align:center; color:white; background:#121212; padding:20px; border-radius:10px;">
        <img src="{product['img']}" style="width:200px; height:200px; object-fit:contain; border-radius:10px;"><br><br>
        <h2 style="color:#ff9800;">{product['name']}</h2>
        <h3 style="color:#90ee90;">₹{product['price']}</h3>
        <p><b>Category:</b> {product.get('category', 'General')}</p>
        
        <div style="display:flex; justify-content:center; gap:20px; flex-wrap:wrap; margin-top:20px;">
            <button onclick="PyWebIO.pushData('add')" style="padding:10px 20px; background:#007bff; color:white; border:none; border-radius:5px;">➕ Add to Cart</button>
            <button onclick="PyWebIO.pushData('cart')" style="padding:10px 20px; background:#007bff; color:white; border:none; border-radius:5px;">🛒 View Cart</button>
            <button onclick="PyWebIO.pushData('back')" style="padding:10px 20px; background:#007bff; color:white; border:none; border-radius:5px;">↩️ Back to Category</button>
            <button onclick="PyWebIO.pushData('home')" style="padding:10px 20px; background:#007bff; color:white; border:none; border-radius:5px;">🏠 Back to Home</button>
        </div>
    </div>
    """)

    action = eval_js("new Promise(resolve => {window.PyWebIO.pushData=resolve;})")

    if action == "add":
        add_to_cart(product)
        toast("✅ Added to cart!", duration=2)
        show_product_detail(product)
    elif action == "cart":
        view_cart()
    elif action == "back":
        show_products(product.get("category", "Shirts"))
    elif action == "home":
        home_page()

def get_product_category(product):
    for category, items in categories.items():
        if product in items:
            return category
    return "Home"


# View full category
def show_products(category_name):
    clear()
    set_black_theme()

    put_html(f"<h2 style='color:#ff9800; text-align:center;'>🛍️ {category_name}</h2>")
    put_html("<div style='display:flex; flex-wrap:wrap; justify-content:center; gap:25px; padding:10px;'>")

    for item in categories[category_name]:
        item["category"] = category_name  
        put_html(f"""
        <div style='
            display:inline-block;
            margin: 15px;
            padding: 15px;
            border: 1px solid #444;
            border-radius: 12px;
            background-color: #1e1e1e;
            color: white;
            text-align: center;
            width: 200px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.4);
            cursor: pointer;
        '
        onclick="PyWebIO.pushData('{item['name']}')">
            <div style="background:white; padding:10px; border-radius:10px;">
                <img src="{item['img']}" style="width:100%; height:150px; object-fit:contain;">
            </div>
            <div style="margin-top:10px;">
                <b>{item['name']}</b><br>
                ₹{item['price']}
            </div>
        </div>
        """)

    put_html("</div>")
    put_html("<div style='text-align:center; margin-top:30px;'>")
    put_buttons(["🏠 Back to Home"], [home_page])
    put_html("</div>")

    selected = eval_js("new Promise(resolve => {window.PyWebIO.pushData=resolve;})")

    for item in categories[category_name]:
        if item['name'] == selected:
            show_product_detail(item)
            return  
    

def collect_address():
    clear()
    set_black_theme()
    put_html("""
        <div style="background:#1e1e1e; color:white; padding:20px; border-radius:10px; margin-top:20px;">
            <h3>Enter Your Address</h3>
            <input id="name" type="text" placeholder="Name" style="margin:5px; padding:8px; width:90%;"><br>
            <input id="door" type="text" placeholder="Door No" style="margin:5px; padding:8px; width:90%;"><br>
            <input id="street" type="text" placeholder="Street" style="margin:5px; padding:8px; width:90%;"><br>
            <input id="district" type="text" placeholder="District" style="margin:5px; padding:8px; width:90%;"><br>
            <input id="state" type="text" placeholder="State" style="margin:5px; padding:8px; width:90%;"><br><br>
            <button onclick="
                let name = document.getElementById('name').value;
                let door = document.getElementById('door').value;
                let street = document.getElementById('street').value;
                let district = document.getElementById('district').value;
                let state = document.getElementById('state').value;

                if(name && door && street && district && state){
                    PyWebIO.pushData([name, door, street, district, state]);
                } else {
                    alert('❌ Please fill all address fields');
                }
            " 
            style="padding:10px 20px; background:#007bff; color:white; border:none; border-radius:5px;">
            Submit</button>
        </div>
    """)

    # Wait for data from JS
    address_data = eval_js("await PyWebIO.receiveData()")

    # Validate and process
    if not address_data or len(address_data) != 5:
        put_html("<h4 style='color:red;'>❌ Failed to collect address. Please try again.</h4>")
        put_buttons(["🏠 Back to Home"], [home_page])
        return

    name, door, street, district, state = address_data
    full_address = f"{door}, {street}, {district}, {state}"

    put_html(f"""
        <div style="background:#1e1e1e; color:white; padding:20px; border-radius:10px; margin-top:20px;">
            <h3>✅ Address Confirmed</h3>
            <p><b>Name:</b> {name}</p>
            <p><b>Full Address:</b> {full_address}</p>
        </div>
    """)
def shop_now():
    clear()
    set_black_theme()
    put_html("<h2 style='color:white; margin-top:20px;'>🛍️ Available Products</h2><br>")

    for category, items in categories.items():
        # Header row: Category name + smaller "More" button
        put_row([
            put_html(f"<h3 style='color:#ffcc00; margin-right:15px'>{category}</h3>"),
            put_html(f"""
                <button style="
                    background:#03a9f4;
                    color:white;
                    border:none;
                    padding:4px 8px;
                    border-radius:5px;
                    cursor:pointer;
                    font-size:12px;
                    margin-top:8px;">
                    More &gt;
                </button>
            """)
        ])

        row = []
        for item in items[:4]:  # Show only first 4 items
            row.append(
                put_html(f"""
                <div style="background:#1c1c1c; color:white; padding:10px; border-radius:12px; 
                            width:180px; margin:8px; text-align:center; border:1px solid #333;
                            transition:transform 0.2s;" 
                     onmouseover="this.style.transform='scale(1.03)'" 
                     onmouseout="this.style.transform='scale(1)'">
                    <img src="{item['img']}" width="150" height="150" style="border-radius:8px;"><br><br>
                    <b style='font-size:16px'>{item['name']}</b><br>
                    <span style='color:#4caf50; font-size:15px;'>₹{item['price']}</span>
                </div>
                """)
            )

        put_row(row)
        put_html("<hr style='border-top:1px solid #444;'>")

    # Centered Back to Home Button
    put_html("""
        <div style="text-align:center; margin-top:30px;">
            <button onclick="location.reload()" style="
                background:#ff5722;
                color:white;
                border:none;
                padding:8px 18px;
                border-radius:6px;
                font-size:15px;
                cursor:pointer;">
                ⬅ Back to Home
            </button>
        </div>
    """)
def show_offers_carousel():
    put_html("""
    <h3 style='color:#fdd835;'>🔥 Offers For You</h3>
    <div style="max-width:800px; margin:auto; border:2px solid #444; border-radius:10px; overflow:hidden;">
      <div id="carousel" style="display:flex; transition: transform 3s ease;">
        <img src="https://d1csarkz8obe9u.cloudfront.net/posterpreviews/t-shirt-offer-ads-design-template-4c94b96d6d741dca6db3e1624b595511_screen.jpg?ts=1661504888" style="width:100%; flex-shrink:0;">
        <img src="https://th.bing.com/th/id/OIP.zKjrGqX85f8970yYYRkGqQHaHa?w=216&h=216&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3" style="width:100%; flex-shrink:0;">
        <img src="https://tse2.mm.bing.net/th/id/OIP.OVB1op_awNUSZVPaS_tOxAHaHa?r=0&w=1536&h=1536&rs=1&pid=ImgDetMain&o=7&rm=3 style="width:100%; flex-shrink:0;">
      </div>
    </div>
    <script>
      let index = 0;
      const carousel = document.getElementById('carousel');
      const totalImages = carousel.children.length;

      setInterval(() => {
        index = (index + 1) % totalImages;
        carousel.style.transform = 'translateX(-' + (index * 100) + '%)';
      }, 3000); // 3 seconds interval
    </script>
    """)

# Home page
def home_page():
    clear()
    put_html('''
    <style>
        body {
            margin: 0;
            font-family: 'Segoe UI', sans-serif;
            background-color: #fff0f5;
        }
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: white;
            padding: 12px 40px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.08);
        }
        .navbar h1 {
            color: #222;
            font-size: 26px;
            font-weight: bold;
        }
        .navbar h1 span {
            color: #f06292;
        }
        .navbar .actions button {
            margin-left: 15px;
            padding: 8px 16px;
            background-color: #f06292;
            color: white;
            border: none;
            border-radius: 20px;
            cursor: pointer;
            font-size: 14px;
        }
        .hero {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 60px 80px;
            background: linear-gradient(to right, #ffeef5, #fff0f5);
        }
        .hero-text {
            max-width: 600px;
        }
        .hero-text h1 {
            font-size: 50px;
            font-weight: bold;
            color: #222;
        }
        .hero-text h1 span {
            color: #2196f3;
        }
        .hero-text h2 {
            font-size: 26px;
            color: #e91e63;
            margin-top: 10px;
        }
        .hero-text p {
            color: #777;
            line-height: 1.6;
            margin: 20px 0;
        }
        .hero-text button {
            padding: 12px 25px;
            font-size: 16px;
            background-color: #111;  /* Shop Now stays dark */
            color: white;
            border: none;
            border-radius: 25px;
            cursor: pointer;
        }
        .hero-img img {
            width: 460px;
            border-radius: 10px;
        }
        @media screen and (max-width: 768px) {
            .hero {
                flex-direction: column;
                text-align: center;
                padding: 30px 20px;
            }
            .hero-img img {
                width: 100%;
                margin-top: 20px;
            }
        }
        .category-button {
            padding:6px 15px;
            background-color:#f06292; /* pink */
            color:white;
            border:none;
            border-radius:15px;
            cursor:pointer;
        }
    </style>

    <div class="navbar">
        <h1>ShopNstyle<span>.</span></h1>
        <div class="actions">
            <button onclick="PyWebIO.pushData('view_cart')">🛒 Cart</button>
            <button onclick="PyWebIO.pushData('coupon')">🎟️ Coupon</button>
            <button onclick="PyWebIO.pushData('orders')">📦 Orders</button>
        </div>
    </div>

    <div class="hero">
        <div class="hero-text">
            <h1>ShopNsty<span>le</span></h1>
            <h2>New Fashion Shop</h2>
            <p>Discover handpicked fashion for every occasion. Stylish, comfortable, and affordable.</p>
            <button onclick="PyWebIO.pushData('shop_now')">Shop Now</button>
        </div>
        <div class="hero-img">
            <img src="https://as1.ftcdn.net/v2/jpg/07/02/99/00/1000_F_702990000_D0YuDwEwqFp9HkJqvgTV1S9nsYvBXsU3.jpg" alt="Fashion">
        </div>
    </div>
    ''')
    show_offers_carousel()

    def show_category(name, items):
        put_html(f"""
            <div style='display: flex; justify-content: space-between; align-items: center; margin-top:25px; background:#fdf4f9; padding:10px 15px; border-radius:10px;'>
                <h3 style='color:#ff4081;'>🛍️ {name}</h3>
                <button onclick="PyWebIO.pushData('more::{name}')" class="category-button">More</button>
            </div>
        """)
        html = "<div style='display: flex; flex-wrap: wrap; gap: 30px; padding:10px;'>"
        for item in items[:4]:
            html += f"""
                <div style='width:160px; background:white; padding:10px; border-radius:10px; text-align:center; cursor:pointer; box-shadow:0 2px 6px rgba(0,0,0,0.1);' 
                     onclick="PyWebIO.pushData('{item['name']}')">
                    <img src="{item['img']}" width="140" style="border-radius:6px;"><br>
                    <b style='color:#333;'>{item['name']}</b><br>
                    <small style='color:#888;'>₹{item['price']}</small>
                </div>
            """
        html += "</div>"
        put_html(html)

    # Display all categories
    for cat, items in categories.items():
        show_category(cat, items)

    # Handle button clicks
    clicked = eval_js("new Promise(resolve => {window.PyWebIO=window.PyWebIO||{};window.PyWebIO.pushData=resolve;})")

    if clicked == "view_cart":
        view_cart()
    elif clicked == "coupon":
        apply_coupon()
    elif clicked == "orders":
        show_orders()
    elif clicked == "shop_now":
        shop_now()
    elif clicked.startswith("more::"):
        category = clicked.split("::")[1]
        show_products(category)
    else:
        # Check if item clicked
        for items in categories.values():
            for item in items:
                if item["name"] == clicked:
                    show_item_info(item)

# Run server
if __name__ == "__main__":
    start_server(home_page, port=8080)
