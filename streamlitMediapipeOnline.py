import gc  # garbage collection

import streamlit as st
import streamlit.report_thread as ReportThread
from streamlit.server.server import Server
from streamlit import caching

from functions import *
from appSessionState import getSessionState


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-[end]
# [start] [persistent states]__________________________________________
gc.enable()  # garbage collection

webapp = getSessionState(
    idx_current_page=1,
    current_page="About Web App",
    page_selector_key=0,
    idx_current_module=2,
    current_module="Face Detection",
    module_selector_key=0,
    idx_data_source=1,
    data_source="Random Image",
    source_selector_key=0,
    #
    current_image_path="",
    current_image_url="",
    idx_url_image=0,
    current_video_path="",
    current_video_url="",
    idx_url_video=0,
    sol_confidence=0.65,
    num_hands=2,
    smooth_lms=1,
    face_model=0,
    num_faces=2,
    current_image_upload="",
    current_video_upload="",
    uploader_key=0,
    webcam_device_id=0,
)


def reload():
    caching.clear_cache()
    gc.collect()  # garbage collection
    #
    webapp.idx_current_page = 1
    webapp.current_page = "About Web App"
    webapp.page_selector_key = 0
    webapp.idx_current_module = 2
    webapp.current_module = "Face Detection"
    webapp.module_selector_key = 0
    webapp.idx_data_source = 1
    webapp.data_source = "Random Image"
    webapp.source_selector_key = 0
    #
    webapp.current_image_path = ""
    webapp.current_image_url = ""
    webapp.idx_url_image = 0
    webapp.current_video_path = ""
    webapp.current_video_url = ""
    webapp.idx_url_video = 0
    webapp.sol_confidence = 0.65
    webapp.num_hands = 2
    webapp.smooth_lms = 1
    webapp.face_model = 0
    webapp.num_faces = 2
    webapp.current_image_upload = ""
    webapp.current_video_upload = ""
    webapp.uploader_key += 1
    webapp.webcam_device_id = 0
    #
    st.experimental_rerun()


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-[end]


# [start] [setup main page and side bar] ____________________________
st.set_page_config(page_title="Streamlit Mediapipe WebApp", layout="wide")

st.markdown(
    f"""
    {pageConfig}
    <div style="text-align:center; margin-top:-75px; ">
    <h1 style="font-variant: small-caps; font-size: xx-large; margin-bottom:-45px;" >
    <font color=#ea0525>w e b {nbsp*2} a p p</font>
    </h1>
    <h1> STREAMLIT MEDIAPIPE WEBAPP </h1>
    <hr>
    </div>
    """,
    unsafe_allow_html=True,
)

st.sidebar.markdown(
    f"""
    <div style="text-align:center; margin-top:-75px; margin-bottom:20px; ">
    <h3 style="font-variant: small-caps; font-size: xx-large; ">
    <font color=#ea0525>s i d e {nbsp} b a r</font>
    </h3>
    <code>Session ID: {ReportThread.get_report_ctx().session_id}</code>
    </div>
    """,
    unsafe_allow_html=True,
)
# <code>garbage history count: {gc.get_count()}</code>

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-[end]


# [start] [setup app pages, modules & data sources]__________________
pages_reload = st.sidebar.columns([9, 4])
st.sidebar.markdown("")
pages_reload[1].markdown("<br>", unsafe_allow_html=True)

reload_redirect = pages_reload[1].empty()
if reload_redirect.button("Refresh App 🔃", help="Click to clear cache and reload app."):
    reload()


appPages = ["Mediapipe Modules", "About Web App", "About Me"]
page_selection = pages_reload[0].selectbox(
    "Page Selection:",
    appPages,
    index=webapp.idx_current_page,
)
if webapp.current_page != page_selection:
    webapp.idx_current_page = appPages.index(page_selection)
    webapp.current_page = page_selection
    st.experimental_rerun()

if webapp.current_page == "About Me":
    st.markdown(aboutMe(), unsafe_allow_html=True)
    st.sidebar.markdown("---")
    st.sidebar.image(open_img_path_url("highlord.jpg", "path"), use_column_width="auto")
    st.sidebar.markdown("---")


elif webapp.current_page == "About Web App":
    if reload_redirect.button(f"➕Explore➕ ➖ App ➖ "):
        webapp.idx_current_page = 0
        webapp.current_page = "Mediapipe Modules"
        st.experimental_rerun()

    st.markdown(aboutWebApp()[0], unsafe_allow_html=True)

    st.sidebar.image(open_img_path_url("mediapipe.jpg", "path"), use_column_width="auto")
    st.sidebar.markdown(
        """
        - <a href="https://google.github.io/mediapipe/#ml-solutions-in-mediapipe" style="text-decoration:none;">ML solutions in MediaPipe</a>
        """,
        unsafe_allow_html=True,
    )
    st.sidebar.image(
        open_img_path_url("mediapipe_solutions.jpg", "path"), use_column_width="auto"
    )

    vid1, vid2 = st.columns([1, 1])
    vid1.video("https://www.youtube.com/watch?v=01sAkU_NvOY")
    vid1.caption("Advanced Computer Vision with Python - Full Course")
    vid2.video("https://www.youtube.com/watch?v=wyWmWaXapmI")
    vid2.caption(
        "StreamLit Computer Vision User Interface Course | MediaPipe OpenCV Python (2021)"
    )

    st.markdown(aboutWebApp()[1], unsafe_allow_html=True)


elif webapp.current_page == "Mediapipe Modules":
    st.set_option("deprecation.showfileUploaderEncoding", False)

    mp_selectors = st.sidebar.columns([1, 1])

    appModules = ["Hand Tracking", "Pose Estimation", "Face Detection", "Face Mesh"]
    module_selection = mp_selectors[0].selectbox(
        "Choose The Mediapipe Solution:",
        appModules,
        index=webapp.idx_current_module,
    )
    if webapp.current_module != module_selection:
        webapp.idx_current_module = appModules.index(module_selection)
        webapp.current_module = module_selection
        st.experimental_rerun()

    appDataSources = [
        "User Image",
        "Random Local Image",
        "Random Online Image",
        # "User Video",
        # "Random Local Video",
        # "Random Online Video",
        # "WebCam",
        "Video Sources",
    ]
    data_source_selection = mp_selectors[1].selectbox(
        "Select Media Source:",
        appDataSources,
        index=webapp.idx_data_source,
    )
    if webapp.data_source != data_source_selection:
        webapp.idx_data_source = appDataSources.index(data_source_selection)
        webapp.data_source = data_source_selection
        st.experimental_rerun()

    st.sidebar.markdown("")
    ph_variables = st.sidebar.columns([1, 1])
    st.sidebar.markdown("")

    read_source_media(webapp, ph_variables)


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-[end]
