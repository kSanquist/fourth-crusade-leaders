import streamlit as st


def app():
    c1, c2, c3, c4, c5, c6, c7 = st.columns(7)
    with c1: st.image("images/indeterminate.svg")
    with c2: st.image("images/indeterminate.svg")
    with c3: st.image("images/indeterminate.svg")
    with c4: st.image("images/indeterminate.svg")
    with c5: st.image("images/indeterminate.svg")
    with c6: st.image("images/indeterminate.svg")
    with c7: st.image("images/indeterminate.svg")

    st.markdown("<h1 style='text-align: center;'>The Indeterminates</h1>", unsafe_allow_html=True)
    st.markdown("""<p style='text-align: center;'>
        The indeterminates in the Fourth Crusade consisted of individuals who did no belong to any
        specific affiliation or established group like the Northern French, Clergy, Venetians, or Imperials.
        These figures represented a diverse array of regions, social classes, and experiences that
        are not encapsulated by the primary previously mentioned affiliations. As free agents,
        indeterminates held the unique position of being able to support the goals of any
        affiliation that aligned with their personal interests and those they believed would
        best serve the overarching goals of the Crusade. This flexibility allowed them to shift
        allegiances or offer support where it might be more strategically or morally advantageous,
        reflecting a more fluid and dynamic role within the council of crusaders.
        </p>
        """, unsafe_allow_html=True)
    st.divider()

    st.markdown("<h1 style='text-align: center; margin-bottom: 0.30em;'>Historical Figures</h1>", unsafe_allow_html=True)
    rc, tb, ol = st.columns(3)

    with rc:
        with st.expander("**Robert de Clari**"):
            st.markdown("Noble knight and chronicler!")
            st.markdown("Go to his page to learn more!")
    with tb:
        with st.expander("**Theodore Branas**"):
            st.markdown("Byzantine general turned Latin!")
            st.markdown("Go to his page to learn more!")
    with ol:
        with st.expander("**Othon de la Roche**"):
            st.markdown("First Frankish Lord of Athens!")
            st.markdown("Go to his page to learn more!")

    st.markdown("")
    st.divider()
    c1, c2, c3, c4, c5, c6, c7 = st.columns(7)
    with c1: st.image("images/indeterminate.svg")
    with c2: st.image("images/indeterminate.svg")
    with c3: st.image("images/indeterminate.svg")
    with c4: st.image("images/indeterminate.svg")
    with c5: st.image("images/indeterminate.svg")
    with c6: st.image("images/indeterminate.svg")
    with c7: st.image("images/indeterminate.svg")