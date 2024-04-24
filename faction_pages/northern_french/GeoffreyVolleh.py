import streamlit as st


def app():
    st.image("images/geoffrey.jpg", width=250)

    st.divider()
    bg, pwr = st.columns(2)
    with bg:
        st.markdown(
            """ 
            <h1 style='text-align: center;'>Geoffrey of Vollehardouin</h1>
            <p style='text-align: center'>
            Geoffrey of Villehardouin, renowned as both a French knight and
            historian, left a mark on history through his pivotal role in
            chronicling the events of the Fourth Crusade. Serving as Marshal of
            Champagne from 1185, he embarked on the Crusade in 1199 following an
            invitation from Count Thibaud III of Champagne. Appointed as one of the
            ambassadors to Venice to secure ships for the journey, he played a key
            role in electing Boniface of MontFerrat as the the Crusade's new leader
            upon the death of Thibaud. He also served as an ambassador to Isaac II
            Angelus and participated in the embassy that demanded the appointment
            of Alexis IV as co-emperor. </p>
            """, unsafe_allow_html=True
        )
    with pwr:
        st.markdown(
            """
            <h1 style='text-align: center;'>Powers</h1>

            1. **Military Leadership**: Serving as Marshal of Champagne, Geoffrey of
            Villehardouin held significant authority over military matters within
            his domain. This encompassed organizing and commanding armed forces,
            strategizing military campaigns, and rallying knights and vassals to
            participate in military endeavors.
            1. **Diplomatic Representation**: Villegardouin played a crucial role in
            diplomatic affairs, acting as ambassador for Count Thibaud and later
            participating in diplomatic missions during the Fourth Cursade. These
            engagements included negotiations with Venice to procure ships and
            discussions with Emperor Isaac II Angelus of regarding the appointment 
            of co-emperors
            1. **Historiographical Legacy**: Villeghardouin's most enduring power lay
            in his role as a chronicler and historian. His chronicle, "On the
            Conquest of Constantinople," stands as a seminal work of medieval
            history, providing invaluable insights into the events of the Fourth
            Crusade and shaping historical narratives.
            """, unsafe_allow_html=True
        )

    st.divider()

    with st.expander("**Opinions on Attacking Constantinople**"):
        st.markdown(
            """
            Geoffrey of Villehardouin supported the decision to divert the Fourth
            Crusade towards Constantinople. His participation in diplomatic missions
            to secure Venetian ships and discussions with Byzantine Emperor Isaac II
            show a pragmatic approach to the campaign's objectives.
            """
        )

    with st.expander("**Opinions on Governing Constantinople**"):
        st.markdown(
            """
            Villegadouin prioritized stability and order in the newly conquered city.
            He urged focus on commitment to maintaining military control and
            defending against potential threats. He also understood the importance
            of political negotiations and alliances in governing a diverse and 
            potentially hostile population.
            """)

    with st.expander("**Opinions on Religion in Constantinople**"):
        st.markdown(
            """
            Villehardouin adhered to the prevailing Christian beliefs of his time.
            Therefore he was in support of the establishment of Latin Christianity
            in Constantinople. He advocated for a Latin Patriarch in oversee religious
            affairs and promote the spread of Catholicism among the local population.
            """
        )







