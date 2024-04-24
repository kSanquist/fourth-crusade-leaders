import streamlit as st


def app():
    c1, c2, c3, c4, c5, c6, c7 = st.columns(7)
    with c1: st.image("images/clergy.svg")
    with c2: st.image("images/clergy.svg")
    with c3: st.image("images/clergy.svg")
    with c4: st.image("images/clergy.svg")
    with c5: st.image("images/clergy.svg")
    with c6: st.image("images/clergy.svg")
    with c7: st.image("images/clergy.svg")

    st.markdown("<h1 style='text-align: center;'>The Clergy</h1>", unsafe_allow_html=True)
    st.markdown("""<p style='text-align: center;'>
        The Clergy was united by their shared vocation and devotion to the papacy.
        Despite their vows of poverty, these clerics wielded significant power and
        resources. Among them were bishops who managed entire dioceses and worked
        in close coordination with the pope to oversee church activities regionally.
        Additionally, influential abbots from wealthy Cistercian monasteries controlled
        expanses of land comparable to those help by noble lords. During the Fourth Crusade,
        this group served as the moral and spiritual guides of the Crusader army.
        While other members of the cross focused on earthly ambitions and power dynamics,
        the those who affiliated themselves with the Clergy were tasked with the
        spiritual welfare of the crusaders, ensuring their actions aligned with their
        ultimate goal of salvation.
        </p>
        """, unsafe_allow_html=True)
    st.divider()

    st.markdown("<h1 style='text-align: center; margin-bottom: 0.30em;'>Historical Figures</h1>", unsafe_allow_html=True)
    _, ck, mp, _ = st.columns([1,2,2,1])
    _, nq, pl, _ = st.columns([1,2,2,1])

    with ck:
        with st.expander("**Conrad of Krosigk**"):
            st.markdown("The Bisjop of Halberstadt!")
            st.markdown("Go to his page to learn more!")
    with mp:
        with st.expander("**Martin of Pairis**"):
            st.markdown("Abbot of the Cistercian monastey of Pairis!")
            st.markdown("Go to his page to learn more!")
    with nq:
        with st.expander("**Nivelon de Quierzy**"):
            st.markdown("The Bishop of Soissons!")
            st.markdown("Go to his page to learn more!")
    with pl:
        with st.expander("**Peter of Lucedio**"):
            st.markdown("The Abbot of Lucedio!")
            st.markdown("Go to his page to learn more!")

    st.markdown("")
    st.divider()
    c1, c2, c3, c4, c5, c6, c7 = st.columns(7)
    with c1: st.image("images/clergy.svg")
    with c2: st.image("images/clergy.svg")
    with c3: st.image("images/clergy.svg")
    with c4: st.image("images/clergy.svg")
    with c5: st.image("images/clergy.svg")
    with c6: st.image("images/clergy.svg")
    with c7: st.image("images/clergy.svg")