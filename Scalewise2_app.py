# ============================================================
# STEP 6B — CREATE SCALEWISE DEPLOYMENT PACKAGE
# ============================================================

import os
import joblib
import pandas as pd
import numpy as np

print("=" * 80)
print("SCALEWISE DEPLOYMENT PACKAGE")
print("=" * 80)


# ============================================================
# 1. CREATE FOLDER
# ============================================================

artifact_dir = "/content/scalewise_artifacts"

os.makedirs(
    artifact_dir,
    exist_ok=True
)


# ============================================================
# 2. SAVE PREPROCESSOR
# ============================================================

joblib.dump(
    preprocessor,
    f"{artifact_dir}/preprocessor.joblib"
)

print("✅ Preprocessor saved")


# ============================================================
# 3. SAVE FINAL MODELS
# ============================================================

# Extract actual estimators from best_models

final_models = {}

for target, info in best_models.items():

    if isinstance(info, dict):

        if "model" in info:
            final_models[target] = info["model"]

        elif "estimator" in info:
            final_models[target] = info["estimator"]

    else:

        final_models[target] = info


joblib.dump(
    final_models,
    f"{artifact_dir}/model1_final_models.joblib"
)

print("✅ Model 1 models saved")


# ============================================================
# 4. SAVE MODEL METADATA
# ============================================================

model_metadata = {}

for target, info in best_models.items():

    if isinstance(info, dict):

        model_metadata[target] = {
            "model_name": info.get(
                "model_name",
                "Unknown"
            ),
            "R2": float(
                info.get("R2", np.nan)
            ),
            "MAE": float(
                info.get("MAE", np.nan)
            ),
            "RMSE": float(
                info.get("RMSE", np.nan)
            )
        }

    else:

        model_metadata[target] = {
            "model_name": "Unknown"
        }


joblib.dump(
    model_metadata,
    f"{artifact_dir}/model1_metadata.joblib"
)

print("✅ Model metadata saved")


# ============================================================
# 5. SAVE FEATURE SCHEMA
# ============================================================

feature_schema = {

    "features":
        X_train.columns.tolist(),

    "targets":
        [
            "VCD_million_cells_mL",
            "growth_rate_per_h",
            "lactate_g_L",
            "osmolality_mOsm_kg"
        ],

    "categorical_features":
        [
            "cell_line",
            "immobilization",
            "impeller_type"
        ]

}


joblib.dump(
    feature_schema,
    f"{artifact_dir}/feature_schema.joblib"
)

print("✅ Feature schema saved")


# ============================================================
# 6. COPY REFERENCE DATA
# ============================================================

reference_files = {

    "physics_engine.csv":
        "/content/scalewise_physics_engine.csv",

    "scale_physics_summary.csv":
        "/content/scalewise_scale_physics_summary.csv",

    "model1_clean.csv":
        "/content/scalewise_model1_clean.csv",

    "parameter_range_check.csv":
        "/content/scalewise_parameter_range_check.csv",

    "sanity_summary.csv":
        "/content/scalewise_sanity_summary.csv"

}


for output_name, source_path in reference_files.items():

    if os.path.exists(source_path):

        data = pd.read_csv(
            source_path
        )

        data.to_csv(
            f"{artifact_dir}/{output_name}",
            index=False
        )

        print(
            f"✅ {output_name}"
        )

    else:

        print(
            f"⚠️ Missing: {source_path}"
        )


# ============================================================
# 7. CREATE REQUIREMENTS FILE
# ============================================================

requirements = """streamlit
pandas
numpy
scikit-learn
joblib
matplotlib
"""

with open(
    "/content/scalewise_artifacts/requirements.txt",
    "w"
) as f:

    f.write(requirements)


print("\n✅ requirements.txt created")


# ============================================================
# 8. LIST PACKAGE
# ============================================================

print("\n" + "=" * 80)
print("DEPLOYMENT PACKAGE CONTENTS")
print("=" * 80)

for filename in sorted(
    os.listdir(artifact_dir)
):

    filepath = os.path.join(
        artifact_dir,
        filename
    )

    size_kb = (
        os.path.getsize(filepath)
        / 1024
    )

    print(
        f"{filename:40s} "
        f"{size_kb:.1f} KB"
    )


print("\n" + "=" * 80)
print("✅ SCALEWISE DEPLOYMENT PACKAGE READY")
print("=" * 80)
