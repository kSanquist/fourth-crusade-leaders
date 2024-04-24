import streamlit as st


def app():
    st.image("images/othon.jpg")

    st.divider()
    bg, pwr = st.columns(2)
    with bg:
        st.markdown(
            """ 
            <h1 style='text-align: center;'>Othon de la Roche</h1>
            <p style='text-align: center'>
            Othon de la Roche, a descendant of the De la Roche family in Burgundy,
            rose to prominence during the Fourth Crusade. Joining the expedition,
            he secured Athens, becoming its first Frankish Lord in 1204. He
            possibly acquired Thebes from Boniface of Montferrat, although it is
            still ambiguous. Assuming th title of Megaskyr, Othon fortified
            Athens' Acropolis and supported the Latin Church, despite conflicts
            with the Church over appointments and land disputes, leading to clashes
            with the papacy. Othon's involvement in the Fourth Crusade
            extended beyond his acquisition of Athens. As a key participant in the
            expedition, he played a crucial role in the distribution of
            conquered territories and the establishment of Latin rule in the 
            Byzantine Empire.
            </p>
            """, unsafe_allow_html=True
        )
    with pwr:
        st.markdown(
            """
            <h1 style='text-align: center;'>Powers</h1>
    
            1. **Military Command**: As the lord of a strategic city like Athens,
            Othon commanded military forces responsible for defending his domains
            and expanding Latin control un mainland Greece. His military ventures
            included capturing key locations like Acrocorinth, Argos, and Nauplia.
            1. **Ecclesiastical Patronage**: Othon exercised influence over the
            Church in his domains, appointing clergy and overseeing religious affairs.
            Despite conflictus with the church, he supported the development
            of the Latin Church in Athens and maintained relations with the papacy.
            1. **Diplomatic Relations**: Othon engaged in diplomacy with neighboring
            powers, navigating alliances and rivalries to safeguard his territories.
            His loyalty to rulers like King Demetrius of Thessalonica and Emperor
            Henry of Flanders underscored his diplomatic acumen.
            """, unsafe_allow_html=True
        )

    st.divider()

    with st.expander("**Opinions on Attacking Constantinople**"):
        st.markdown(
            """
            As a participant in the Crusade and a recipient of territories
            following its conquest, he took a pragmatic approach rather than
            outspoken advocacy for or against the attack. Othon's primary
            concern was securing territorial gains for himself and his followers,
            rather than engaging in broader debates about the morality
            or strategic necessity of the assault on Constantinople. As a
            member of the crusading army, he followed the directives of his
            commanders and participated in the siege and subsequent
            events based on prevailing consensus of leadership.
            """
        )

    with st.expander("**Opinions on Governing Constantinople**"):
        st.markdown(
            """
            Given that he followed suit with the consensus of leadership and had
            a background as a nobleman from Burgundy, he favored a feudal system
            of government. Othon sought to establish himself as a feudal lord,
            with authority over his vassals and subjects in his territories. Othon
            also advocated for a system of vassalage, granting land and privileges
            to loyal supporters and knights in exchange for military service
            and allegiance. 
            """)

    with st.expander("**Opinions on Religion in Constantinople**"):
        st.markdown(
            """
            As a nobleman of the Latin Church, and his support for the
            Catholic Archbishop of Athens and establishing connections with
            Cistercian monks, showed a commitment to promoting Catholicism in his
            territories. Othon's interactions with the Orthodox clergy and
            population in Athens influenced his approach to religious matters,
            leading to policies of religious tolerance.
            """
        )





