# 🧑‍💻 Freelance Management Module for Odoo

This custom **Odoo 18 module** allows users to manage freelancing workflows, including posting projects, bidding on them, and registering as either a client or a freelancer.

## 🚀 Features

- ✅ Freelancers can register and create profiles  
- ✅ Clients can register and post freelance projects  
- ✅ Freelancers can place bids on open projects  
- ✅ Project owners can review bids and accept proposals  
- ✅ Integrated with Odoo's activity tracking and messaging system

---

## 🗂 Folder Structure

freelance/ ├── init.py ├── manifest.py ├── models/ │ ├── init.py │ ├── project.py │ ├── bid.py │ ├── freelancer.py │ └── client.py ├── views/ │ ├── project_views.xml │ ├── bid_views.xml │ └── menus.xml ├── security/ │ ├── ir.model.access.csv │ └── security.xml └── static/ └── description/ └── icon.png


---

## 🧱 Requirements

- **Odoo 18.0** (`20250330` version or later)
- Python 3.10+
- PostgreSQL 12+

---

## 📦 Installation Guide

### 📁 Step 1: Add the Module

Copy the entire module directory (`freelance`) into your Odoo addons path:

### bash
cp -r freelance /opt/odoo/odoo-18.0/odoo/addons/

### Or if you're on Windows:

Copy the `freelance` folder to:
C:\odoo 18.0.20250330\server\odoo\addons\

👋 Contribution

PRs are welcome! Feel free to fork this module and enhance it.


📄 License

MIT License

💡 Contact

For support or questions, reach out via GitHub Issues or contact https://github.com/koki-mekonnen.
