import streamlit as st


def app():
    c1, c2, c3, c4, c5, c6, c7 = st.columns(7)
    with c1: st.image("images/north_french.svg")
    with c2: st.image("images/north_french.svg")
    with c3: st.image("images/north_french.svg")
    with c4: st.image("images/north_french.svg")
    with c5: st.image("images/north_french.svg")
    with c6: st.image("images/north_french.svg")
    with c7: st.image("images/north_french.svg")

    st.markdown("<h1 style='text-align: center;'>The Northern French</h1>", unsafe_allow_html=True)
    st.markdown("""<p style='text-align: center;'>
        The Northern French nobility was made up of primarily crusading lords from Northwest
        France, unified by a common language and cultural background. The considerable
        influence and predominance of the Northern French during the Fourth Crusade came
        primarily from their sheer number of participants they contributed to the cause.
        This faction is characterized by familial and feudal connections, giving rise to
        both alliances and conflicts within the group. The relationships between the
        French nobles were crucial as they navigated the various challenges they faced
        during the crusade, not only through military endeavors but also through
        decisions they had to make in regards to the political landscape of the
        territories they engaged with. </p>
        """, unsafe_allow_html=True)
    st.divider()

    st.markdown("<h1 style='text-align: center; margin-bottom: 0.30em;'>Historical Figures</h1>", unsafe_allow_html=True)
    bf, lb, hs = st.columns(3)
    _, gv, hf, _ = st.columns([1,2,2,1])

    with bf:
        with st.expander("**Baldwin IX of Flanders**"):
            st.markdown("One of the most powerful lords in France!")
            st.markdown("Go to his page to learn more!")
    with lb:
        with st.expander("**Louis of Blois**"):
            st.markdown("A young, powerful, and ambitious count!")
            st.markdown("Go to his page to learn more!")
    with hs:
        with st.expander("**Hugh of Saint-Pol**"):
            st.markdown("Wisest of the Northern French Lords!")
            st.markdown("Go to his page to learn more!")
    with gv:
        with st.expander("**Geoffrey of Vollehardouin**"):
            st.markdown("Deep connection with Thibaut, great at negotiations!")
            st.markdown("Go to his page to learn more!")
    with hf:
        with st.expander("**Henry of Flanders**"):
            st.markdown("young brother and close confidant of Baldwin!")
            st.markdown("Go to his page to learn more!")

    st.markdown("")
    st.divider()
    c1, c2, c3, c4, c5, c6, c7 = st.columns(7)
    with c1: st.image("images/north_french.svg")
    with c2: st.image("images/north_french.svg")
    with c3: st.image("images/north_french.svg")
    with c4: st.image("images/north_french.svg")
    with c5: st.image("images/north_french.svg")
    with c6: st.image("images/north_french.svg")
    with c7: st.image("images/north_french.svg")