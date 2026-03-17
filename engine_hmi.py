import streamlit as st
from data_stream import generate_data
from ai_model import detect_leak
import time

st.set_page_config(layout="wide")

st.title("Diesel Engine Leak Detection HMI")

# Generate data
data = generate_data()

# Detect leak
leak, location, confidence = detect_leak(data)

# Color logic
pipe_color = "red" if leak else "green"

# ---------------- SENSOR PANEL ---------------- #

col1, col2, col3 = st.columns(3)

col1.metric("MAF", round(data["MAF"],2))
col1.metric("MAP", round(data["MAP"],2))

col2.metric("Boost", round(data["Boost"],2))
col2.metric("Turbo Speed", round(data["TurboSpeed"],0))

col3.metric("Exhaust Pressure", round(data["ExhaustPressure"],2))
col3.metric("RPM", round(data["RPM"],0))

# ---------------- STATUS ---------------- #

if leak:
    st.error(f"⚠ Leak Detected : {location}")
else:
    st.success("System Normal")

st.write("Confidence:",confidence,"%")

# ---------------- ANIMATED AIRFLOW ---------------- #

airflow_html = f"""
<style>

.arrow {{
  width:60px;
  height:10px;
  background:{pipe_color};
  position:relative;
  animation:flow 1s infinite linear;
}}

@keyframes flow {{
  from {{left:0px;}}
  to {{left:40px;}}
}}

.pipe {{
  height:12px;
  width:120px;
  background:{pipe_color};
}}

.turbo {{
  border:3px solid blue;
  padding:20px;
  border-radius:50%;
  animation:spin 2s linear infinite;
}}

@keyframes spin {{
  from {{transform:rotate(0deg);}}
  to {{transform:rotate(360deg);}}
}}

</style>

<div style="display:flex;align-items:center">

<div class="pipe"></div>
<div class="arrow"></div>

<div class="turbo">Turbo</div>

<div class="arrow"></div>
<div class="pipe"></div>

<div>Intercooler</div>

</div>
"""

st.markdown(airflow_html, unsafe_allow_html=True)

# ---------------- 3D MODEL ---------------- #

engine_3d = """
<iframe src="https://threejs.org/examples/#webgl_loader_gltf"
width="800"
height="500">
</iframe>
"""

st.markdown(engine_3d, unsafe_allow_html=True)

# ---------------- AUTO REFRESH ---------------- #

time.sleep(2)
st.rerun()
