# FDE Field Tool: 1-Tap OTP Approval & Falsifiable SLA Metric Tracker
def approve_challan_with_otp(challan_id: str, otp_ok: bool, wait_mins: float) -> dict:
    SLA_TARGET_MINS = 10.0  # আমাদের ফলসিফায়েবল সাকসেস মেট্রিক (১০ মিনিটের নিচে)

    if not otp_ok:
        return {"challan": challan_id, "status": "REJECTED", "sla_met": False}

    # ওটিপি মিলে গেলে সাথে সাথে ডিজিটাল সই ও মেট্রিক যাচাই
    sla_passed = wait_mins < SLA_TARGET_MINS
    return {
        "challan": challan_id,
        "status": "DIGITALLY_SIGNED_AND_CLEARED",
        "clearance_mins": wait_mins,
        "sla_met": sla_passed
    }

if __name__ == "__main__":
    # আড়াই ঘণ্টার (১৫০ মিনিট) কাগুজে সই এখন ফোনের ওটিপিতে ৬.৫ মিনিটে ক্লিয়ার
    print(approve_challan_with_otp("CHL-2026-889", otp_ok=True, wait_mins=6.5))
