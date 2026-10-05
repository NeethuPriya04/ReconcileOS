# ReconcileOS — Autonomous 3-Way Match & Margin Leakage Auditor
> Built for WCC Launchpad 30 (Track: Agentic AI / Everyday Automation)

## 📌 Problem & Overview
High-volume retail hubs, e-commerce dark stores (Zepto, Blinkit), and FMCG warehouses lose 3% to 5% of gross procurement margins to short-shipments and price creep. 
Suppliers deliver fewer units than ordered (recorded on paper dock delivery challans), but invoice for the full quantity at higher rates. ReconcileOS deterministically cross-references Purchase Orders, Dock Receiving Reports, and Tax Invoices to stop margin leakage.

## ⚡ Key Capabilities
* **Deterministic Reconciliation Engine:** Eliminates LLM math hallucination with verified code calculations.
* **Forensic Evidence Modal:** Inspects gatekeeper delivery challans and highlights physical damage/shortfall notes.
* **Autonomous Dispute Dispatch:** Prepares structured Debit Memos and one-click WhatsApp dispute alerts.
* **Tamper-Evident Governance Ledger:** SHA-256 state tracking for every document hash and audit event.
* **Human-in-the-Loop Safeguard:** Financial withholding strictly requires manual managerial authorization.

## 🛠️ Architecture
1. **Extraction Agent:** Normalizes unstructured PO, Delivery Slip, and Invoice into typed JSON.
2. **Deterministic Math Tool:** Calculates Quantity Variance and Rate Creep.
3. **Evidence Linker:** Grounds variances to supervisor notes.
4. **Debit Memo Synthesizer:** Auto-generates formal deduction notices.
