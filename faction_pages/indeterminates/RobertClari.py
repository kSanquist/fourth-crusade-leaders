import streamlit as st


def app():
    st.image("images/robert.jpg")

    st.divider()
    bg, pwr = st.columns(2)
    with bg:
        st.markdown(
            """ 
            <h1 style='text-align: center;'>Robert de Clari</h1>
            <p style='text-align: center'>
            Robert de Clari, a knight from Picardy, accompanied Count Peter of Amiens
            and his brother Aleaumes de Clari on the Fourth Crusade, chronicling
            the events in Old French. His account offers a unique perspective as a
            lower vassal, shedding light on lesser-known aspects of crusader
            activities. Aleaumes, his brother, distinguished himself during the final
            siege of Constantinople, earning recognition from Count Hugh of Saint-Pol.
            Robert's mention of the Shroud of Turn in Constantinople, though likely a 
            confusion with the sudarium of Saint Veronica, remains notable. His
            narrative, although lacking in the discussions of leadership, provides
            insights into camp rumors and the reality of combat, portraying the
            Byzantines as treacherous and favoring the Venetians.
            </p>
            """, unsafe_allow_html=True
        )
    with pwr:
        st.markdown(
            """
            <h1 style='text-align: center;'>Powers</h1>
            
            As a knight and chronicler, Robert de Clari held no formal powers in
            the traditional sense. His authority lay in his role as a participant
            of the Fourth Crusade and as a chronicler who documented the events
            of the crusade. While he lacked political or military authority, his
            account provided valuable insight into the experiences of lower-ranking
            crusaders and shed light on aspects of the crusade often overlooked
            by higher-ranking sources.
            """, unsafe_allow_html=True
        )

    st.divider()

    with st.expander("**Opinions on Attacking Constantinople**"):
        st.markdown(
            """
            Robert de Clari supported the attack on Constantinople. He describes
            events leading up to the siege and subsequent conquests of the city,
            providing details of the crusaders' actions and motivations. He
            also portrays the Byzantines as treacherous, indicating a belief in
            the legitimacy of the crusaders' actions against Constantinople.
            """
        )

    with st.expander("**Opinions on Governing Constantinople**"):
        st.markdown(
            """
            He viewed establishment of Latin rule in Constantinople favorably,
            he portrayed the conquest of the city as a significant achievement
            of the crusaders. His support for the crusade and subsequent Latin
            administration in Constantinople showed approval for new order
            established in the city.
            """)

    with st.expander("**Opinions on Religion in Constantinople**"):
        st.markdown(
            """
            Little is known about Robert de Clari's opinions on religion in
            Constantinople as his accounts of the Fourth Crusade focus
            primarily on the military events and logistical challenges faced by
            the crusaders rather than religious matters. That being said, his
            enlisting as a knight of the fourth crusade and his positive accounts
            of the militaristic events of the attack of Constantinople suggest
            that he was in favor of Latin influence in religious matters inside
            Constantinople.
            """
        )





