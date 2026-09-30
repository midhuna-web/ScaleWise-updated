@@ -1,247 +1,678 @@
# ============================================================
# STEP 6B — CREATE SCALEWISE DEPLOYMENT PACKAGE
# SCALEWISE — AI COPILOT FOR SCALABLE CELL-CULTURE BIOPROCESS
# STEP 6A — STREAMLIT APP SKELETON
# ============================================================

import os
import joblib
import streamlit as st
import pandas as pd
import numpy as np

print("=" * 80)
print("SCALEWISE DEPLOYMENT PACKAGE")
print("=" * 80)

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="ScaleWise AI Copilot",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# 1. CREATE FOLDER
# CUSTOM CSS
# ============================================================

artifact_dir = "/content/scalewise_artifacts"
st.markdown("""
<style>

os.makedirs(
    artifact_dir,
    exist_ok=True
)
.main {
    background-color: #f7f9fc;
}

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

.scale-title {
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 0px;
}

.scale-subtitle {
    font-size: 18px;
    color: #667085;
    margin-top: 0px;
}

.section-title {
    font-size: 25px;
    font-weight: 700;
    margin-top: 20px;
    margin-bottom: 10px;
}

.metric-card {
    background: white;
    padding: 20px;
    border-radius: 14px;
    border: 1px solid #e4e7ec;
    text-align: center;
    min-height: 120px;
}

.metric-value {
    font-size: 30px;
    font-weight: 800;
}

.metric-label {
    font-size: 14px;
    color: #667085;
}

.risk-card {
    background: white;
    padding: 22px;
    border-radius: 14px;
    border: 1px solid #e4e7ec;
    margin-bottom: 15px;
}

.copilot-card {
    background: white;
    padding: 25px;
    border-radius: 16px;
    border: 1px solid #d0d5dd;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# 2. SAVE PREPROCESSOR
# HEADER
# ============================================================

joblib.dump(
    preprocessor,
    f"{artifact_dir}/preprocessor.joblib"
st.markdown(
    '<div class="scale-title">🧬 ScaleWise</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="scale-subtitle">'
    'AI Copilot for Scalable Cell-Culture Bioprocess Design'
    '</div>',
    unsafe_allow_html=True
)

print("✅ Preprocessor saved")
st.markdown("---")


# ============================================================
# 3. SAVE FINAL MODELS
# SIDEBAR — USER INPUTS
# ============================================================

# Extract actual estimators from best_models
st.sidebar.header("⚙️ Scale-Up Configuration")

final_models = {}
st.sidebar.markdown(
    "Enter the current process conditions and select the target scale."
)

for target, info in best_models.items():

    if isinstance(info, dict):
# ------------------------------------------------------------
# TARGET SCALE
# ------------------------------------------------------------

        if "model" in info:
            final_models[target] = info["model"]
target_scale = st.sidebar.selectbox(
    "Target Scale (L)",
    [2, 5, 10, 20, 50, 100],
    index=4
)

        elif "estimator" in info:
            final_models[target] = info["estimator"]

    else:
# ------------------------------------------------------------
# BIOLOGICAL PARAMETERS
# ------------------------------------------------------------

        final_models[target] = info
st.sidebar.subheader("🧫 Biological Parameters")

cell_line = st.sidebar.selectbox(
    "Cell Line",
    [
        "Chicken fibroblast"
    ]
)

joblib.dump(
    final_models,
    f"{artifact_dir}/model1_final_models.joblib"
immobilization = st.sidebar.selectbox(
    "Immobilization",
    [
        "None"
    ]
)

print("✅ Model 1 models saved")
initial_VCD = st.sidebar.number_input(
    "Initial VCD (million cells/mL)",
    min_value=0.0,
    value=0.5,
    step=0.1
)

working_time = st.sidebar.number_input(
    "Working Time (h)",
    min_value=0.0,
    value=24.0,
    step=1.0
)


# ------------------------------------------------------------
# PROCESS PARAMETERS
# ------------------------------------------------------------

st.sidebar.subheader("⚙️ Process Parameters")

rpm = st.sidebar.number_input(
    "Agitation (RPM)",
    min_value=0.0,
    value=220.0,
    step=5.0
)

aeration = st.sidebar.number_input(
    "Aeration (VVM)",
    min_value=0.0,
    value=0.06,
    step=0.01
)

temperature = st.sidebar.number_input(
    "Temperature (°C)",
    value=37.0,
    step=0.1
)

pH = st.sidebar.number_input(
    "pH",
    value=7.0,
    step=0.1
)

DO = st.sidebar.number_input(
    "Dissolved Oxygen (%)",
    min_value=0.0,
    max_value=100.0,
    value=40.0,
    step=1.0
)

feed_rate = st.sidebar.number_input(
    "Feed Rate (mL/h)",
    min_value=0.0,
    value=0.5,
    step=0.1
)


# ============================================================
# 4. SAVE MODEL METADATA
# RUN BUTTON
# ============================================================

model_metadata = {}
run_analysis = st.sidebar.button(
    "🚀 RUN SCALEWISE ANALYSIS",
    use_container_width=True
)

for target, info in best_models.items():

    if isinstance(info, dict):
# ============================================================
# SESSION STATE
# ============================================================

if "analysis_run" not in st.session_state:
    st.session_state.analysis_run = False

if run_analysis:
    st.session_state.analysis_run = True


# ============================================================
# MAIN NAVIGATION
# ============================================================

tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Process Risk Scorecard",
    "🚨 Scale-Up Risk Guardian",
    "🔥 Heatmap Explorer",
    "🤖 AI Copilot"
])

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

# ============================================================
# TAB 1 — PROCESS RISK SCORECARD
# ============================================================

with tab1:

    st.markdown(
        '<div class="section-title">'
        '📊 Process Risk Scorecard'
        '</div>',
        unsafe_allow_html=True
    )

    st.caption(
        "Overall process readiness based on biological, "
        "oxygen-transfer, hydrodynamic and model-coverage indicators."
    )

    if not st.session_state.analysis_run:

        st.info(
            "👈 Configure the target-scale process in the sidebar "
            "and click **RUN SCALEWISE ANALYSIS**."
        )

    else:

        model_metadata[target] = {
            "model_name": "Unknown"
        }
        # ----------------------------------------------------
        # TEMPORARY PLACEHOLDER VALUES
        # These will be replaced by Model 2 in Step 6C.
        # ----------------------------------------------------

        overall_score = 82

joblib.dump(
    model_metadata,
    f"{artifact_dir}/model1_metadata.joblib"
)
        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "Overall Readiness",
                f"{overall_score}%"
            )

        with col2:

print("✅ Model metadata saved")
            st.metric(
                "Target Scale",
                f"{target_scale} L"
            )

        with col3:

            st.metric(
                "Process Status",
                "CONDITIONAL GO"
            )

        with col4:

            st.metric(
                "Model Coverage",
                "Prototype"
            )


        st.markdown("### Parameter Categories")

        c1, c2, c3, c4, c5 = st.columns(5)

        with c1:
            st.metric(
                "Biological",
                "88%"
            )

        with c2:
            st.metric(
                "Oxygen Transfer",
                "91%"
            )

        with c3:
            st.metric(
                "Hydrodynamics",
                "74%"
            )

        with c4:
            st.metric(
                "Process Control",
                "86%"
            )

        with c5:
            st.metric(
                "Model Reliability",
                "69%"
            )


        st.markdown("---")

        st.subheader("🔍 Current Process Conditions")

        input_summary = pd.DataFrame({

            "Parameter": [
                "Target Scale",
                "Cell Line",
                "Initial VCD",
                "Working Time",
                "RPM",
                "Aeration",
                "Temperature",
                "pH",
                "DO",
                "Feed Rate"
            ],

            "Value": [
                f"{target_scale} L",
                cell_line,
                f"{initial_VCD:.2f} million cells/mL",
                f"{working_time:.1f} h",
                f"{rpm:.0f} RPM",
                f"{aeration:.2f} VVM",
                f"{temperature:.1f} °C",
                f"{pH:.2f}",
                f"{DO:.1f}%",
                f"{feed_rate:.2f} mL/h"
            ]
        })

        st.dataframe(
            input_summary,
            use_container_width=True,
            hide_index=True
        )


# ============================================================
# 5. SAVE FEATURE SCHEMA
# TAB 2 — SCALE-UP RISK GUARDIAN
# ============================================================

feature_schema = {
with tab2:

    "features":
        X_train.columns.tolist(),
    st.markdown(
        '<div class="section-title">'
        '🚨 Scale-Up Risk Guardian'
        '</div>',
        unsafe_allow_html=True
    )

    "targets":
        [
            "VCD_million_cells_mL",
            "growth_rate_per_h",
            "lactate_g_L",
            "osmolality_mOsm_kg"
        ],
    st.caption(
        "Continuous assessment of potential scale-up failure modes."
    )

    "categorical_features":
        [
            "cell_line",
            "immobilization",
            "impeller_type"
        ]
    if not st.session_state.analysis_run:

}
        st.info(
            "Run the ScaleWise analysis from the sidebar."
        )

    else:

joblib.dump(
    feature_schema,
    f"{artifact_dir}/feature_schema.joblib"
)
        # ----------------------------------------------------
        # TEMPORARY DEMO RISK
        # Will be replaced by Model 3 logic.
        # ----------------------------------------------------

        st.warning(
            "⚠️ WARNING — Target-scale process requires validation"
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Risk Level",
                "Moderate"
            )

        with col2:

            st.metric(
                "Confidence",
                "87%"
            )

        with col3:

            st.metric(
                "Target Scale",
                f"{target_scale} L"
            )


        st.markdown("### 🔎 Risk Assessment")

        st.markdown(
            """
            <div class="risk-card">

            <h4>⚠️ Warning</h4>

            The selected target-scale operating point requires
            confirmation against the learned operating region.

            <br><br>

print("✅ Feature schema saved")
            <b>Risk:</b><br>
            Potential oxygen-transfer / hydrodynamic deviation.

            <br><br>

            <b>Confidence:</b><br>
            87%

            <br><br>

            <b>Suggested Action:</b><br>
            Review agitation and aeration operating window.

            <br><br>

            <b>Recommended Validation:</b><br>
            Conduct a target-scale confirmation experiment before
            production implementation.

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# 6. COPY REFERENCE DATA
# TAB 3 — HEATMAP EXPLORER
# ============================================================

reference_files = {
with tab3:

    "physics_engine.csv":
        "/content/scalewise_physics_engine.csv",
    st.markdown(
        '<div class="section-title">'
        '🔥 Interactive Heatmap Explorer'
        '</div>',
        unsafe_allow_html=True
    )

    "scale_physics_summary.csv":
        "/content/scalewise_scale_physics_summary.csv",
    st.caption(
        "Explore how process parameters influence predicted "
        "target-scale biological performance."
    )

    "model1_clean.csv":
        "/content/scalewise_model1_clean.csv",

    "parameter_range_check.csv":
        "/content/scalewise_parameter_range_check.csv",
    col1, col2, col3 = st.columns(3)

    "sanity_summary.csv":
        "/content/scalewise_sanity_summary.csv"

}
    with col1:

        heatmap_target = st.selectbox(
            "Prediction Target",
            [
                "VCD",
                "Growth Rate",
                "Lactate",
                "Osmolality"
            ]
        )


    with col2:

        heatmap_x = st.selectbox(
            "X-axis Parameter",
            [
                "RPM",
                "Aeration",
                "DO",
                "Temperature",
                "pH",
                "P/V",
                "kLa",
                "Mixing Time"
            ]
        )


for output_name, source_path in reference_files.items():
    with col3:

        heatmap_y = st.selectbox(
            "Y-axis Parameter",
            [
                "Aeration",
                "RPM",
                "DO",
                "Temperature",
                "pH",
                "P/V",
                "kLa",
                "Mixing Time"
            ]
        )


    if st.session_state.analysis_run:

        st.markdown(
            f"### {heatmap_target} response — {target_scale} L"
        )

    if os.path.exists(source_path):
        # Temporary heatmap placeholder.
        # Real model-generated heatmap comes in Step 6E.

        data = pd.read_csv(
            source_path
        heatmap_data = pd.DataFrame(
            np.random.uniform(
                0,
                1,
                (8, 8)
            ),
            index=np.arange(8),
            columns=np.arange(8)
        )

        data.to_csv(
            f"{artifact_dir}/{output_name}",
            index=False
        st.dataframe(
            heatmap_data.style.background_gradient(),
            use_container_width=True
        )

        print(
            f"✅ {output_name}"
        st.caption(
            "Prototype visualization — model-generated "
            "response surface will replace this in Step 6E."
        )

    else:

        print(
            f"⚠️ Missing: {source_path}"
        st.info(
            "Run ScaleWise analysis to activate the Heatmap Explorer."
        )


# ============================================================
# 7. CREATE REQUIREMENTS FILE
# TAB 4 — AI COPILOT
# ============================================================

requirements = """streamlit
pandas
numpy
scikit-learn
joblib
matplotlib
"""
with tab4:

with open(
    "/content/scalewise_artifacts/requirements.txt",
    "w"
) as f:
    st.markdown(
        '<div class="section-title">'
        '🤖 ScaleWise AI Copilot'
        '</div>',
        unsafe_allow_html=True
    )

    f.write(requirements)
    st.caption(
        "Interactive process interpretation and scale-up guidance."
    )


print("\n✅ requirements.txt created")
    if not st.session_state.analysis_run:

        st.info(
            "Run the ScaleWise analysis first."
        )

# ============================================================
# 8. LIST PACKAGE
# ============================================================
    else:

print("\n" + "=" * 80)
print("DEPLOYMENT PACKAGE CONTENTS")
print("=" * 80)
        st.markdown(
            """
            <div class="copilot-card">

            <h3>🧠 ScaleWise Copilot</h3>

            <p>
            <b>Current assessment:</b>
            The selected target-scale operating point has been
            evaluated against the available process and physics
            information.
            </p>

            <p>
            <b>Primary consideration:</b>
            Confirm oxygen-transfer and hydrodynamic behaviour
            before production-scale implementation.
            </p>

            <p>
            <b>Recommended next step:</b>
            Review the risk assessment and operating-window
            heatmap, then perform a target-scale validation trial.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

for filename in sorted(
    os.listdir(artifact_dir)
):

    filepath = os.path.join(
        artifact_dir,
        filename
    )
        st.markdown("### 💬 Ask ScaleWise")

    size_kb = (
        os.path.getsize(filepath)
        / 1024
    )
        user_question = st.text_input(
            "Ask about the current process",
            placeholder=(
                "Example: Why is this target scale risky?"
            )
        )

    print(
        f"{filename:40s} "
        f"{size_kb:.1f} KB"
    )

        if user_question:

            st.info(
                "🤖 Copilot response engine will be connected "
                "to the ScaleWise model outputs in Step 6F."
            )


print("\n" + "=" * 80)
print("✅ SCALEWISE DEPLOYMENT PACKAGE READY")
print("=" * 80)
# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "ScaleWise — AI Copilot for Scalable Cell-Culture Bioprocess Design | "
    "Hackathon Prototype"
)
