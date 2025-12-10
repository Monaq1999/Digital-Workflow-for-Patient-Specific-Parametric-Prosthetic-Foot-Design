import csv
from pathlib import Path
from google.colab import files
from dataclasses import dataclass, asdict


OUTPUT_CSV = Path("fusion_params_from_user.csv") # Name of the CSV that Fusion will import

BASE_LARGE = { # Base Geometry -face offsets (cm)
    "P1": 5.0,
    "P2": 2.0,
    "P3": 2.0,
    "P4": 2.0,
    "P5": 4.0,
    "P6": 5.0,
    "P7": 2.0,
    "P8": 2.0,
    "P9": 2.0,
}

SIZE_SCALES = { #Size scales (Halved proportions)
    "XS": -1.0,
    "S":  -0.5,
    "M":   0.0,
    "L":   0.5,
    "XL":  1.0,
}

UNITS = "cm"

@dataclass
class ProstheticParams:
    P1: float
    P2: float
    P3: float
    P4: float
    P5: float
    P6: float
    P7: float
    P8: float
    P9: float


def params_from_scale(scale: float) -> ProstheticParams:
    vals = {k: v * scale for k, v in BASE_LARGE.items()}
    return ProstheticParams(**vals)


def params_from_custom_p1(custom_p1_cm: float) -> ProstheticParams:
    base_p1 = BASE_LARGE["P1"]
    scale = custom_p1_cm / base_p1
    return params_from_scale(scale)


# User input

print("🦿 Prosthetic Foot Parametric Sizer") 
print("--------------------------------------------------------")
print("• Enter a size: XS, S, M, L, XL")
print("       OR")
print("• Enter a numeric custom P1 value in cm (e.g. 2.5)\n")

user_input = input("Size or custom P1 (cm): ").strip()

try:
    # Custom numeric P1
    custom_p1 = float(user_input)
    params = params_from_custom_p1(custom_p1)
    label = f"Custom_P1_{custom_p1:.3f}cm"
except ValueError:
    # Named size
    size_key = user_input.upper()
    if size_key not in SIZE_SCALES:
        raise ValueError("Invalid input. Use XS, S, M, L, XL or a number.")
    scale = SIZE_SCALES[size_key]
    params = params_from_scale(scale)
    label = size_key

print("\nUsing configuration:", label)
for name, value in asdict(params).items():
    print(f"  {name} = {value:.3f} {UNITS}")

# Generate fusion compatable CSV

header = ["Name", "Unit", "Expression", "Value", "Comments", "Favorite"]

with OUTPUT_CSV.open("w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)

    for pname, value in asdict(params).items():
        fusion_name = pname.lower()  # P1 -> p1
        writer.writerow([
            fusion_name,   # Name
            UNITS,         # Unit
            value,         # Expression
            "",            # Value (Fusion computes)
            label,         # Comments
            "true",        # Favorite
        ])

print(f"\n CSV created: {OUTPUT_CSV}")

# Automatically download

files.download(str(OUTPUT_CSV))
