import streamlit as st


def app():
    c1, c2, c3, c4, c5, c6, c7 = st.columns(7)
    with c1: st.image("images/imperial.svg")
    with c2: st.image("images/imperial.svg")
    with c3: st.image("images/imperial.svg")
    with c4: st.image("images/imperial.svg")
    with c5: st.image("images/imperial.svg")
    with c6: st.image("images/imperial.svg")
    with c7: st.image("images/imperial.svg")

    st.markdown("<h1 style='text-align: center;'>The Imperials</h1>", unsafe_allow_html=True)
    st.markdown("""<p style='text-align: center;'>
        The Imperials played a significant and influential role despite being a
        minority in terms of numbers. This group was diverse, comprising of mainly
        Germans and some northern Italian. Although outnumbered by the Northern
        French and Venetians, the imperial faction's strategic leadership was pivotal.
        Their role became especially crucial during key decisions and battles, as they
        navigated political and military obstacles faced during the crusade. Their
        leadership at the council and in directing the crusade's operations highlights
        the impact and influence of the imperial faction in driving the events and
        outcomes of the Fourth Crusade.
        </p>
        """, unsafe_allow_html=True)
    st.divider()

    st.markdown("<h1 style='text-align: center; margin-bottom: 0.30em;'>Historical Figures</h1>", unsafe_allow_html=True)
    bm, bk, ob = st.columns(3)

    with bm:
        with st.expander("**Boniface I of Montferrat**"):
            st.markdown("The valiant leader of the Fourth Crusade!")
            st.markdown("Go to his page to learn more!")
    with bk:
        with st.expander("**Berthold II von Katzenelnbogen**"):
            st.markdown("German nobleman and close friend of Boniface!")
            st.markdown("Go to his page to learn more!")
    with ob:
        with st.expander("**Oberto II of Biandrate**"):
            st.markdown("The Count of Biandrate!")
            st.markdown("Go to his page to learn more!")

    st.markdown("")
    st.divider()
    c1, c2, c3, c4, c5, c6, c7 = st.columns(7)
    with c1: st.image("images/imperial.svg")
    with c2: st.image("images/imperial.svg")
    with c3: st.image("images/imperial.svg")
    with c4: st.image("images/imperial.svg")
    with c5: st.image("images/imperial.svg")
    with c6: st.image("images/imperial.svg")
    with c7: st.image("images/imperial.svg")