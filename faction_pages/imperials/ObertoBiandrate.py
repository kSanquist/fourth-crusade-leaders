import streamlit as st


def app():
    st.image("images/oberto.jpg", width=600)

    st.divider()
    bg, pwr = st.columns(2)
    with bg:
        st.markdown(
            """ 
            <h1 style='text-align: center;'>Oberto II of Biandrate</h1>
            <p style='text-align: center'>
            Oberto II of Biandrate, Count of Biandrate in Lombardy, played a
            significant yet tumultuous role in the Fourth Crusade and its
            aftermath. As a close ally and companion of Boniface of Montferrat,
            the crusade's leader, Oberto was deeply involved in the political and
            military affairs that took place during and after the crusade. During
            the Fourth Crusade, Oberto's support for Boniface was crucial, particularly
            after the diversion of the crusade to Constantinople. After the death
            of Boniface in 1207, Oberto took on the role of regent for Boniface's son,
            Demetrius, in the new Kingdom of Thessalonica. Alongside allies, Oberto 
            plotted to overthrow Demetrius in favor of William VI, Boniface's elder
            son. This move led to tension with the Latin Emperor Henry IX of Flanders
            who sought to secure Demetrius's position.
            </p>
            """, unsafe_allow_html=True
        )
    with pwr:
        st.markdown(
            """
            <h1 style='text-align: center;'>Powers</h1>

            1. **Feudal Authority**: as the Count of Biandrate, Oberto held feudal
            authority over his domain, giving him the power to govern the land and
            people within his jurisdiction.
            1. **Judicial Power**: Oberto had the ability to administer justice within
            his territory, which included settling disputes and enforcing laws.
            1. **Taxation Rights**: Oberto had the authority to levy taxes on his lands,
            enabling him to fund his administrative and military ventures
            1. **Military Command**: As a Count, Oberta could rally and command troops,
            a crucial ability for participating in the campaigns like the Fourth Crusade
            1. **Diplomatic Influence**: His status as a noble and companion to Boniface on
            the crusade provided him with diplomatic influence both within the crusader states
            and in negotiations with external powers.
            """, unsafe_allow_html=True
        )

    st.divider()

    with st.expander("**Opinions on Attacking Constantinople**"):
        st.markdown(
            """
            Oberto was a close companion and supporter of Boniface of
            Montferrat, the leader of the Fourth Crusade, who played a signifiant
            role in diverting the crusade towards Constantinople. Oberto's
            close alignment with Boniface shows Oberto's support for the 
            strategic decision made by the crusade leadership including the 
            attack on Constantinople as well. His active participation in the
            crusade also shows Oberto's advocacy for the attack.
            """
        )

    with st.expander("**Opinions on Governing Constantinople**"):
        st.markdown(
            """
            Oberto shared in ambitions of the crusade's leadership to establish
            Latin control over Constantinople. Oberto was also a prominent Count
            showing his advocacy for a feudal system in Constantinople and as seen
            by Oberto's advocacy for Boniface's rule over Constantinople, he
            definitely shared the many crusader's opinions of having a crusader
            Emperor. That being said, Oberto would have prefered Boniface be
            emperor as opposed to Henry IX of Flanders.
            """)

    with st.expander("**Opinions on Religion in Constantinople**"):
        st.markdown(
            """
            Oberto shared in the broader religious motivations of the crusade,
            of which being the desire to reclaim and defend Christian territories
            in the Holy Land and beyond, therefore he likely advocated for a Latin
            or at least a dual Patriarch in Constantinople. That being said,
            Boniface was known to advocate for a strictly Greek patriarch and due
            to Oberto's connection with Boniface, he might have been persuaded
            to go against the grade of the Latin Crusades and side with Boniface
            on a strictly Greek Patriarch.
            """
        )





