import streamlit as st


def app():
    c1, c2, c3, c4, c5, c6, c7 = st.columns(7)
    with c1: st.image("images/venetian.svg")
    with c2: st.image("images/venetian.svg")
    with c3: st.image("images/venetian.svg")
    with c4: st.image("images/venetian.svg")
    with c5: st.image("images/venetian.svg")
    with c6: st.image("images/venetian.svg")
    with c7: st.image("images/venetian.svg")

    st.markdown("<h1 style='text-align: center;'>The Venetians</h1>", unsafe_allow_html=True)
    st.markdown("""<p style='text-align: center;'>
        The Venetian role in the Fourth Crusade was pivotal and uniquely driven by economic
        and strategic interests, distinguishing them from other participants primarily
        motivated by religion. Venice agreed to provide transport and naval support for the
        crusaders, but with conditions that underlined their mercantile priorities.
        Initially, the agreement called for transportation of crusaders to Jerusalem in
        exchange for payment. When the crusaders failed to meet these financial commitments,
        Dandolo renegotiated the terms, landing to the diversion of the Crusade first
        to Zara (a rival Christan city) and later to Constantinople. This shift from a
        religious mission to a series of economic maneuvers was heavily influenced by the 
        Venetians. Venice, as a maritime, republic was distinct from the feudal societies
        of most other crusader states. Its economy was based on trade and governed by a
        republic, with elected leaders as opposed to monarchies. The city's involvement in
        the Crusade was strategic, aiming to expand its trade routes and establish colonies
        and trading posts.
        </p>
        """, unsafe_allow_html=True)
    st.divider()

    st.markdown("<h1 style='text-align: center; margin-bottom: 0.30em;'>Historical Figures</h1>", unsafe_allow_html=True)
    ed, mz, pz = st.columns(3)

    with ed:
        with st.expander("**Enrico Dandolo**"):
            st.markdown("The Doge of Venice during the Fourth Crusade!")
            st.markdown("Go to his page to learn more!")
    with mz:
        with st.expander("**Marino Zeno**"):
            st.markdown("Commander of the Venetian fleet!")
            st.markdown("Go to his page to learn more!")
    with pz:
        with st.expander("**Pietro Ziani**"):
            st.markdown("A Venetian Crusader succeeding Enrico Dandolo!")
            st.markdown("Go to his page to learn more!")

    st.markdown("")
    st.divider()
    c1, c2, c3, c4, c5, c6, c7 = st.columns(7)
    with c1: st.image("images/venetian.svg")
    with c2: st.image("images/venetian.svg")
    with c3: st.image("images/venetian.svg")
    with c4: st.image("images/venetian.svg")
    with c5: st.image("images/venetian.svg")
    with c6: st.image("images/venetian.svg")
    with c7: st.image("images/venetian.svg")