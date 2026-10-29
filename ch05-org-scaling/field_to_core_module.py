# FDE Field-to-Core Pattern: Reusable Core Engine + Branch Configs
class CoreReconcilerEngine:
    def __init__(self, branch_cfg: dict):
        self.branch = branch_cfg["name"]
        self.tol_pct = branch_cfg["tolerance_pct"]

    def verify(self, declared_kg: float, actual_kg: float) -> dict:
        max_diff = declared_kg * (self.tol_pct / 100.0)
        passed = abs(actual_kg - declared_kg) <= max_diff
        return {"branch": self.branch, "status": "APPROVED" if passed else "FLAGGED"}

if __name__ == "__main__":
    # কোর কোডে হাত না দিয়ে শুধু কনফিগ বদলেই ভিন্ন ব্রাঞ্চে ডেপ্লয়মেন্ট
    BRANCH_CONFIGS = [
        {"name": "Chattogram_Port", "tolerance_pct": 1.0},
        {"name": "Narayanganj_Cement", "tolerance_pct": 0.5}
    ]
    for cfg in BRANCH_CONFIGS:
        print(CoreReconcilerEngine(cfg).verify(declared_kg=50000, actual_kg=50350))
