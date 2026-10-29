# FDE Field Diagnostic: As-Is Workflow Bottleneck Analyzer
def analyze_workflow_bottlenecks(workflow_steps: list) -> dict:
    diagnostics = []
    total_wasted_minutes = 0

    for step in workflow_steps:
        sop_min = step["sop_time_min"]
        real_min = step["real_time_min"]
        delta = real_min - sop_min

        # বাস্তবের সময় এসওপির দ্বিগুণ বা বেশি হলেই সেটা প্রাইমারি বটলনেক
        if delta > 0 and real_min >= (sop_min * 2):
            diagnostics.append({
                "step": step["name"],
                "delay_min": delta,
                "action": "AUTOMATE_NOW" if step["is_manual"] else "OPTIMIZE_INFRA"
            })
            total_wasted_minutes += delta

    return {"total_delay_min": total_wasted_minutes, "bottlenecks": diagnostics}

if __name__ == "__main__":
    # শ্যাডো সেশনে স্টপওয়াচ ধরে পাওয়া আসল ফিল্ড ডেটা
    field_audit_data = [
        {"name": "Invoice Verification", "sop_time_min": 5, "real_time_min": 45, "is_manual": True},
        {"name": "Manager Physical Sign", "sop_time_min": 10, "real_time_min": 120, "is_manual": True},
        {"name": "ERP Data Sync", "sop_time_min": 2, "real_time_min": 3, "is_manual": False}
    ]
    print(analyze_workflow_bottlenecks(field_audit_data))
