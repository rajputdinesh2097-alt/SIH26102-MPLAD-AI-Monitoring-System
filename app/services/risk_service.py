def calculate_features(project):
    expenditure_ratio = 0

    if project.sanctioned_amount > 0:
        expenditure_ratio = (
            project.expenditure / project.sanctioned_amount
        ) * 100

    return {
        "expenditure_ratio": round(expenditure_ratio, 2),
        "progress": project.progress,
        "sanctioned_amount": project.sanctioned_amount,
        "expenditure": project.expenditure
    }

def calculate_risk(features):
    score = 0
    reasons = []

    if features["expenditure_ratio"] > 100:
        score += 40
        reasons.append("Expenditure is higher than sanctioned amount")

    if features["expenditure_ratio"] > features["progress"] + 20:
        score += 30
        reasons.append("Expenditure is significantly higher than project progress")

    if features["progress"] < 30 and features["expenditure_ratio"] > 50:
        score += 20
        reasons.append("High expenditure with low project progress")

    if score >= 61:
        risk_level = "High"
    elif score >= 31:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    return {
        "risk_score": score,
        "risk_level": risk_level,
        "reasons": reasons
    }

