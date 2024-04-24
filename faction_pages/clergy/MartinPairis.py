import streamlit as st


def app():
    st.image("images/martin.jpg", width=400)

    st.divider()
    bg, pwr = st.columns(2)
    with bg:
        st.markdown(
            """ 
            <h1 style='text-align: center;'>Martin of Pairis</h1>
            <p style='text-align: center'>
            Martin, the abbout of the Cistercian monastery of Pairis, played
            a significant role in the Fourth Crusade. Urged by Pope Innocent III,
            Martin led the Upper Rhenish contingent, preaching the crusade along
            the Upper Right and assembling an army of 1,200 men from the region.
            Respine being unarmed, he led the army on its journey to Venice, arriving
            in 1202. During the siege of Zara, Martin sought absolution from his vows
            to participate in the crusade, fearing the shedding of Christian blood.
            This was refused by the papal legate, however. He played a crucial role in
            the spiritual direction of the German contingent and later joined a
            delegation sent to seek papal forgiveness for the excommunication incurred
            during the siege. After the diversion of the crusade to Constantinople, Martin
            sailed to the Holy Land, ministering to the sick before journeying to
            Constantinople. There, he seized relics for his monastery.
            </p>
            """, unsafe_allow_html=True
        )
    with pwr:
        st.markdown(
            """
            <h1 style='text-align: center;'>Powers</h1>

            1. **Spritual Leadership**: As a religious leader Martin was allowed to
            preach the crusade along the Upper Rhenish and led his followers in
            fulfilling their vows.
            1. **Delegated Authority**: Martin was entrusted with leading the German
            contingent of the crusade, particulalry in matters concerining spiritual
            welfare. While no military command was given, he held influence over the
            soldiers under his care.
            1. **Diplomatic Representation**: Martin served as part of a delegation
            sent by the leaders of the crusade to seek papal forgiveness and the lifting
            of the excommunication incurred during the siege of Zara.
            """, unsafe_allow_html=True
        )

    st.divider()

    with st.expander("**Opinions on Attacking Constantinople**"):
        st.markdown(
            """
            While Martin was initially reluctant, as evident by his request to
            be absolved of his vow to participate in the siege of Zara, Martin
            ultimately participated in the crusaders' military actions. Therefore
            he did not oppose the assault on the city. Martin also took advantage
            of the chaos during the sack of Constantinople to seize relics for
            his monastery, indicating a fervor towards the sack as opposed to 
            moral objection.
            """
        )

    with st.expander("**Opinions on Governing Constantinople**"):
        st.markdown(
            """
            As a Cistercian monk and prelate, Martin's primary concerns were primarily
            religious rather than political. Therefore, his preferences would have
            likely gone to the majority, that being a feudal system with a Crusader
            emperor.
            """)

    with st.expander("**Opinions on Religion in Constantinople**"):
        st.markdown(
            """
            Being a member of the Latin church, Martin's primary concern was to
            promote and preserve Catholicism in the new Latin Empire, therefore he
            would have likely advocated for a Latin Patriarch. Martin's personal
            goals of acquiring relics to enhance the spiritual prestige of his own
            religious institution highlights his ambition towards securing the 
            Catholic faith.
            """
        )





