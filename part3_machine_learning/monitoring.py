baseline_mae = 300.75

new_mae = 520

drift = (
    (new_mae - baseline_mae)
    / baseline_mae
)

print(
    "n\Model Monitoring"
)

print(
    f"Baseline MAE: {baseline_mae}"
)

print(
    f"Current MAE: {new_mae}"
)

print(
    f"Error Drift: {drift:.2%}"
)

threshold = 0.20

if drift > threshold:
    status = "Alert / Requires / Investigation"
else:
    status = "PASS / Normal"
print(
    f"System status: {status}"
)