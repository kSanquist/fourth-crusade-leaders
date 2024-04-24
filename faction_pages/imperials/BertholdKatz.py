import streamlit as st


def app():
    st.image("images/berthold.svg", width=300)

    st.divider()
    bg, pwr = st.columns(2)
    with bg:
        st.markdown(
            """ 
            <h1 style='text-align: center;'>Berthold II von Katzenelnbogen</h1>
            <p style='text-align: center'>
            Berthold II von Katzenelnbogen played a prominent role in the Forth
            Crusade, particularly within the German contingent led by Boniface
            of Montferrat. Arriving at the Crusaer camp after the capture of
            Zara in 1202, Berthold developed a close relationship with Boniface,
            which would prove influential in the events to come. As the Crusaders
            reached Constantinople, in 1203, Boniface aligned with Henry of Flanders
            and participated in the breach of the city's defense in 1204. Following
            the fall of Constantinople and the proclamation of Baldwin IX of
            Flanders as the new Latin Emperor, Berthold supported Boniface in his
            brief rebellion against Baldwin's rule. As a reward for his loyalty,
            Berthold was granted a lordship centered on Velestino and the title
            "Lord of Valestino". Additionally, he undertook diplomatic missions
            in behalf of Pope Innocent III, further showcasing his importance in
            the Crusade.
            </p>
            """, unsafe_allow_html=True
        )
    with pwr:
        st.markdown(
            """
            <h1 style='text-align: center;'>Powers</h1>

            1. **Leadership with German Contingent**: Berthold held a prominent
            position within the German contingent of the Fourth Crusade, which
            was under the command of Boniface
            1. **Close relations with Boniface**: Berthold's close personal
            relationship with Boniface allowed him to wield considerable influence
            in decision-making processes within the contingent
            1. **Role in Diplomatic Missions**: Berthold's involvement in diplomatic
            missions on behalf of Pope Innocent III indicates a level of authority
            entrusted to him by both Boniface and papal leadership.
            1. **Influence in Strategy and Poltical Matters**: Berthold's position
            as a trusted advisor and ally to key figures in the Crusade granted him
            influence in strategic and political matters, albeit without specific formal
            powers.
            """, unsafe_allow_html=True
        )

    st.divider()

    with st.expander("**Opinions on Attacking Constantinople**"):
        st.markdown(
            """
            Berthold actively participated in the siege and subsequent breach
            of Constantinople alongside the Crusader army. showing his
            advocacy for the attack. Also, as a prominent member of the German
            contingent under Boniface, Berthold aligned himself with the
            overall views and decisions made by the leadership of the Crusade,
            including the decision to attack Constantinople.
            """
        )

    with st.expander("**Opinions on Governing Constantinople**"):
        st.markdown(
            """
            As a supporter of Boniface of Montferrat, Berthold aligned himself
            with the political objectives of Boniface. Therefore, Berthold
            supported Boniface as emperor alongside a feudal government in
            Constantinople. This can be seen through Berthold's support for
            Boniface's brief contest for the title of Latin Emperor against
            Count Baldwin IX of Flanders.
            """)

    with st.expander("**Opinions on Religion in Constantinople**"):
        st.markdown(
            """
            Similar to Oberto II of Biandrate, being a both a Crusader and a loyal
            supporter of Boniface, Berthold likely was split between accepting his
            religion and siding with a Latin Patriarch or following under Boniface's
            opinions and going with a strictly Greek Patriarch. That being said,
            considering the overwhelming majority for at least a dual Latin and 
            Greek Patriarch, Berthold might have folded for the majority when it came
            to decision.
            """
        )





