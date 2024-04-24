import streamlit as st


def app():
    st.image("images/boniface.jpg")

    st.divider()
    bg, pwr = st.columns(2)
    with bg:
        st.markdown(
            """ 
            <h1 style='text-align: center;'>Boniface I of Montferrat</h1>
            <p style='text-align: center'>
            Boniface of Montferrat, hailing from a prestigious family with ties to
            the Kingdom of Jerusalem, emerged as a key figure in the Fourth
            Crusade. Chosen as the leader following the death of Count Theobald III
            of Champagne, Boniface's leadership was pivotal in the strategic
            decisions of the Fourth Crusade. Boniface formed an alliance with
            Alexius IV Angelos, the son of deposed Byzantine emperor Isaac II Angelos.
            This alliance aimed to restore Alexios' father's claim to the Byzantine
            throne, a plan which sought the blessing of Pope Innocent III, albeit
            with strict instructions to avoid conflict with fellow Christians. Following
            the conquest of Constantinople in 1204, Boniface was preceived as a potential
            candidate for Latin Emperor. However, the Venetians opposed this opting
            for Baldin IX of Flanders instead.
            </p>
            """, unsafe_allow_html=True
        )
    with pwr:
        st.markdown(
            """
            <h1 style='text-align: center;'>Powers</h1>

            1. **Marquisate Authority**: As Marquis of Montferrat, Boniface exercised
            authority over his domain, including the administration of justice, collection
            of taxes, and maintenance of feudal obligations.
            1. **Military Command**: Boniface of Montferat held significant authority
            as the leader of the Fourth Cursade, with the power to make strategic
            decisions regarding military operations, troop movements, and engaging
            with enemy forces.
            1. **Diplomatic Leadership**: He wielded influence in diplomatic matters,
            negotiating alliances, treaties, and agreements with other Crusader
            leaders, as well as with local rulers and powers in the regions where the
            Crusade operated.
            1. **Engagement with Papacy**: He engaged with Pope Innocent III and other
            European leaders to secure papal support for the Crusade, as well as to
            gain political and financial assistance for the expedition.
            1. **Naval Operations**: Boniface collaborated with the Venetians, who
            provided the Crusaders with naval support, overseeing the coordination of
            naval operations and ensuring effective cooperation between the Crusader
            army and the Venetian fleet.
            """, unsafe_allow_html=True
        )

    st.divider()

    with st.expander("**Opinions on Attacking Constantinople**"):
        st.markdown(
            """
            Boniface of Montferrat supported the mission to to attack Constantinople
            seeing it as the only opportunity to get the revenue the crusaders earned
            by returning Alexius IV to his thrown. The crusaders needed the money
            promised to them by Alexius IV to repay the Venetians for their support,
            however after he was usurped by the anti-crusader Alexius V, Boniface
            saw no other option but to attack Constantinople. Therefore Boniface
            advocated heavily for the attack on Constantinople.
            """
        )

    with st.expander("**Opinions on Governing Constantinople**"):
        st.markdown(
            """
            Boniface advocate for a government structure ensuring stability and
            control over the newly conquered territory. Therefore he likely
            advocated for a feudal system coupled with a strong emperor capable
            of maintaining order and asserting Latin rule in Constantinople.
            In terms of the emperor he would have liked to see on the throne, it
            is obvious that he advocated for himself as emperor. 
            """)

    with st.expander("**Opinions on Religion in Constantinople**"):
        st.markdown(
            """
            Given that the Fourth Crusade was intended to restore Christian control
            over Jerusalem, Boniface placed high importance on maintaining Christian
            religious institutions in Constantinople. Therefore it is reasonable
            to assume that Boniface would have preferred a Latin Patriarch. That
            being said, Boniface in fact advocated for a Greek Patriarch as he was 
            aware of the tension within the city walls and sought to maintain peace
            by limiting the amount of change in the Latin Empire.
            """
        )





