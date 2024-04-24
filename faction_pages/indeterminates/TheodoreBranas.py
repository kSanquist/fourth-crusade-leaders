import streamlit as st


def app():
    st.image("images/theodore.png", width=300)

    st.divider()
    bg, pwr = st.columns(2)
    with bg:
        st.markdown(
            """ 
            <h1 style='text-align: center;'>Theodore Branas</h1>
            <p style='text-align: center'>
            Theodore Branas was a Byzantine general and later served under the Latin
            Empire of Constantinople. He held the title of Caesar and became the
            governor and lord of Adrianople in 1206. Branas was a descendant of the
            imperial Komnenoi dynasty and played a prominent role in both Byzantine
            and Latin regimes. After the fall of Constantinople in 1204, he quickly
            allied with the new Latin regime, marrying Anna, and received the title
            of Caesar in return. Branas was involved in barious military and
            diplomatic endeavors, including leading Greek troops against the
            Bulgarians and mediating between Henry of Flanders and Greek cities
            threatened by Bulgarian attacks. He governed Adrianople,
            Didymoteichon, and Apros, with his lordship recognized by Venetian
            authorities, Branas' legacy includes his descendants' integration into
            Byzantine society and his granddaughter's marriage into the imperoal
            family of the Palaiologoi, indicating the enduring influence of his
            family in the Byzantine Empire.
            </p>
            """, unsafe_allow_html=True
        )
    with pwr:
        st.markdown(
            """
            <h1 style='text-align: center;'>Powers</h1>
    
            1. **Military Commander**: Branas commanded the garrison of Adrianople
            and led Greek troops in various military engagements, including defending
            against Bulgarian attacks and participating in raids against enemy
            territories.
            1. **Administrative Authority**: As the ruler of of many territories, Branas had
            administrative powers, including the administration of justice, collection
            of taxes, and maintenance of order within his domains.
            1. **Title of Caesar**: Branas was granted the title of Caesar, further
            enhancing his prestige and authority, especially among the Byzantine and
            Latin nobility.
            1. **Recognition of Venetian Authorities**: Branas received recognition
            from Venetian authorities, as evidenced by the Pactum Adrianopolitanum, which
            aknowledged his right to govern Adrianople and its territories according to
            Greek customs.
            """, unsafe_allow_html=True
        )

    st.divider()

    with st.expander("**Opinions on Attacking Constantinople**"):
        st.markdown(
            """
            Theodore Branas supported the new Latin regime that emerged during the
            fall of Constantinople in 1204, aligning himself with the Latin
            Empire. As such, he viewed the attack on Constantinople favorably,
            considering it a necessary action to establish Latin control over
            the city and the Byzantine Empire. Not to mention, being that he
            fought with Isaac II he probably saw the dethroning of Alexios V even
            more favorable.
            """
        )

    with st.expander("**Opinions on Governing Constantinople**"):
        st.markdown(
            """
            Given Theodore Branas' position and actions, he preferred a form of
            government that granted him significant autonomy and authority, allowing
            him to effectively govern his own territories while still being
            integrated int othe broader political structure of the new Latin Empire.
            This suggests that he may have favored a feudal system where he held substantial
            power over his domain. However, as a descendant of the imperial dynasty of the
            Komnenoi, he also harbored ambitions of possible restoration of Byzantine rule.
            """)

    with st.expander("**Opinions on Religion in Constantinople**"):
        st.markdown(
            """
            Theodore Branas navigated the complex religious landscape of his
            time pragmatically, aiming to maintain stability within his territories.
            As a Greek nobleman, he recognized the importance of both Latin and
            Greek religious institutions for maintaining social cohesion and
            legitimacy among his subjects. Given his cooperation with the Latin
            regime, he was inclined to support the Latin patriarch in Constantinople,
            especially if it offered him political advantages.
            """
        )





