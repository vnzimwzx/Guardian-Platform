# 🛡️ Guardian Platform - Autonomous File Engineering & RPA Hub

An automated, ultra-lightweight Robotic Process Automation (RPA) ecosystem built in Python and Batch/VBScript architecture. This system is designed to execute completely in the background upon Windows logon, providing autonomous file sorting and live financial data synchronization without user intervention.

## 🚀 Core Features

- **Autonomous Workspace Optimization (`organizador.py`):** Automatically scans and segregates loose files and client folders from the Desktop into dedicated, high-level directory categories (ZIP, PDF, PNG, XLSX) with built-in recursive file extraction and exception handling.
- **Live Financial Data Ingestion (`guardian_hub.py`):** Performs real-time web scraping via financial APIs to fetch live USD and EUR commercial exchange rates, structured dynamically into clean analytical data pipelines using **Pandas** and stored directly into compressed `.xlsx` binary storage.
- **Stealth Windows Integration (`invisible_guardian.vbs`):** Bypasses standard command-line flashing UI by wrapping the pipeline in a silent VBScript shell instance linked to the native Windows Task Scheduler (`taskschd.msc`).
- **Ghost Spectre & Superlite Compatibility:** Highly optimized data pipeline with terminal-driven visual feedback, engineered to run smoothly on lightweight system architectures (Intel Core i5 / 8GB RAM environments).

## 🛠️ Tech Stack

- **Language:** Python 3.11+
- **Data Engineering:** Pandas, OpenPyXL
- **Networking & Web Scraping:** Requests API
- **Shell Automation:** Windows Batch, VBScript (WScript.Shell)
- **Environment:** Visual Studio Code

---
*Developed by Antony Vinicius — Dedicated to building highly-efficient autonomous software architecture.*
