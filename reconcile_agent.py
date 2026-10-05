"""
ReconcileOS Deterministic 3-Way Reconciliation Agent
Author: Neethu Priya Padamati
Track: Agentic AI / Everyday Automation
"""

def reconcile_three_way(po_data: dict, challan_data: dict, invoice_data: dict):
    results = []
    total_leakage = 0.0

    for item, po in po_data.items():
        receipt = challan_data.get(item, {})
        inv = invoice_data.get(item, {})

        rec_qty = receipt.get("received_qty", 0)
        billed_qty = inv.get("billed_qty", 0)
        agreed_price = po.get("unit_price", 0.0)
        billed_price = inv.get("unit_price", 0.0)

        # 1. Shortfall calculation
        qty_short = billed_qty - rec_qty
        shortfall_cost = max(0, qty_short) * billed_price

        # 2. Rate creep calculation
        rate_diff = billed_price - agreed_price
        rate_creep_cost = max(0.0, rate_diff) * rec_qty

        item_leakage = shortfall_cost + rate_creep_cost
        total_leakage += item_leakage

        results.append({
            "item": item,
            "ordered": po.get("qty", 0),
            "received": rec_qty,
            "billed": billed_qty,
            "shortfall": qty_short,
            "rate_variance": rate_diff,
            "financial_leakage": item_leakage,
            "status": "MATCHED" if item_leakage == 0 else "CRITICAL_VARIANCE",
            "evidence": receipt.get("dock_note", "")
        })

    return {
        "total_leakage_prevented": total_leakage,
        "requires_human_approval": total_leakage > 0,
        "line_items": results
    }

if __name__ == "__main__":
    po = {"Organic Almond Milk (1L)": {"qty": 500, "unit_price": 220.0}}
    challan = {"Organic Almond Milk (1L)": {"received_qty": 420, "dock_note": "Pallet 3 damaged, 80 rejected"}}
    invoice = {"Organic Almond Milk (1L)": {"billed_qty": 500, "unit_price": 240.0}}

    audit = reconcile_three_way(po, challan, invoice)
    print(f"Total Margin Leakage Prevented: INR {audit['total_leakage_prevented']}")
