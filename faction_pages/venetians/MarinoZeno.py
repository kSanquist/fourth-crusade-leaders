import streamlit as st


def app():
    st.image("images/marino.png", width=600)

    st.divider()
    bg, pwr = st.columns(2)
    with bg:
        st.markdown(
            """ 
            <h1 style='text-align: center;'>Marino Zeno</h1>
            <p style='text-align: center'>
            Marino Zeno, a figure from the medieval Venetian nobility, played
            significant roles in both administrative and diplomatic capacities
            during Venetian and Byzantine history. While little is known about his
            early life, Zeno assumed the position of Venetian Podesta of Constantinople in May 1205, facing the
            challenging aftermath of the Fourth Crusade's capture of Constantinople
            in 1204. With the death of Doge Dandolo in the city, Zeno stepped into
            a crucial role overseeing Venetian interests in the newly conquered
            territory. Zeno's position within the Venetian government and his
            involvement in diplomatic affairs shows he was a central figure in
            Venetian efforts to navigate the challenges and opportunities presented
            by this transformative period.
            </p>
            """, unsafe_allow_html=True
        )
    with pwr:
        st.markdown(
            """
            <h1 style='text-align: center;'>Powers</h1>
    
            1. **Administrative Authority**: As Podesta of Constantinople,
            Zeno wielded significant administrative authority, overseeing
            Venetian governance and ensuring the implementation of Venetian laws
            and policies in the new Latin Empire.
            1. **Diplomatic Representation**: Zeno served as a diplomatic
            representative of Venice in Constantinople, engaging in negotiations
            with local authorities, other Crusader factions, and external powers
            to advance Venetian interests and maintain stability in the region.
            1. **Financial Oversight**: Zeno had responsibility for financial
            matters, including the management of Venetian assets, taxation, and
            trade regulations in Constantinople. Ensuring the economic viability
            of Venetian interests in the region.
            1. **Civic Governance**: Zeno played a role in civic governance,
            overseeing the administration of public services, infrastructure
            maintenance, and urban planning efforts in Constantinople.
            """, unsafe_allow_html=True
        )

    st.divider()

    with st.expander("**Opinions on Attacking Constantinople**"):
        st.markdown(
            """
            As a Venetian nobleman and administratior, Zeno's action were influence 
            by the broated policial objectives of the Venetian Republic. He supported 
            the objectives of the Fourth Crusade,including the capturing of 
            Constantinople to secure Venetian commercial interests in the Eastern 
            Mediterranean. Zeno prioritized strategic considerations aimed at 
            enhancing Venetian influence and control in Constantinople guided by the 
            goals of Venetian expansion and trade dominance.
            """
        )

    with st.expander("**Opinions on Governing Constantinople**"):
        st.markdown(
            """
            Zeno's opinions on governing Constantinople were aligned and were guided
            by the interest of more porminent Venetians such as Doge Enrico Dandolo.
            These interests being focused on securing commercial dominance for the
            Venetians in the new Latin empire and expanding Venetian influence. Therefore,
            similar to Doge Dondolo, he advocated for a Republic and overwhelming trade
            authority for Venetians.
            """)

    with st.expander("**Opinions on Religion in Constantinople**"):
        st.markdown(
            """
            Zeno navigated religion in Constantinople with a focus on maintaining
            stability and accommodating various religious communities. While Zeno
            went for a dual Patriarchy, if it were up to him, given that Venice itself
            was a diverse city with a mix of many religious communities, he might have
            played with the idea of religious freedom in Constantinople. That being
            said, this idea would have gotten him in trouble with the Crusaders.
            Therefore, he advocated for the most appropriate option.
            """
        )





