import streamlit as st


def app():
    st.image("images/baldwin.jpg")

    st.divider()
    bg, pwr = st.columns(2)
    with bg:
        st.markdown(
            """ 
            <h1 style='text-align: center;'>Baldin IX of Flanders</h1>
            <p style='text-align: center'>
            Baldwin IX of Flanders and Hainaut, born into a distinguished lineage as the 
            son of Count Baldwin V of Hainaut and Countess Margaret I of Flanders,
            emerged as a prominent figure in European politics including the Fourth
            Crusade. He was designated heir to Count Philip I of Flanders, his
            brother-in-law, who entrusted him with significant responsibilities during
            his absence on a crusade. Upon philip's return, Baldwin was appointed chief
            adviser to Philip Augustus by the King Louis VII of France. Baldwin's ties
            to the French monarchy deepened when he marries Isabelle of Hainaut, Philips'
            niece. Despite tension, Baldwin's ascent continued, marked by his marriage
            to Marie, daughter of Count Henry I of Champagne and Marie of France.
            Baldwin's commitment to the Crusades was unwavering, influenced by familial
            connectons to defend the Holy Land. His leadership during the Fourth Crusade
            was pivotal, as he rallied support from fellow crusaders and allies, including
            Richard I of England and Otto IV of Germany. </p>
            """, unsafe_allow_html=True
        )
    with pwr:
        st.markdown(
        """
        <h1 style='text-align: center;'>Powers</h1>
        
        1. **Military Command**: As count, Baldwin exercised command over the military
        forces within his domain. Allowing him to raise armies, organize military campaigns,
        and call upon his vassals and knights to provide military service in times of conflict.
        3. **Judicial Authority**: The count served as the ultimate judicial authority
        within his territories. He presided over courts of law, adjudicated disputes,
        and administered justice.
        4. **Economic Control**: Baldwin exercised control over the economic resources of
        Flanders and Hainaut. Including regulating trade, collecting tolls and tariffs, and
        overseeing the management of agricultural estates and urban centers.
        5. **Diplomatic Relations**: The count engaged in diplomatic relations with
        neighboring lords, monarchs, and foreign powers. He negotiated treaties and alliances
        to secure the interests of Flanders and Hainaut and maintain peac and stability.
        """, unsafe_allow_html=True
        )

    st.divider()

    with st.expander("**Opinions on Attacking Constantinople**"):
        st.markdown(
            """
            As a seasoned military leader, Baldwin recognized the strategic 
            significance of Constantinople, understanding its potential to secure 
            vital resources like funds for the Venetians and reinforcements for 
            the crusader army. Additionally, as a powerful French lord, he harbored 
            personal ambitions for territorial expansion. The establishment of a 
            Latin Empire provided Baldwin with an opportunity to potentially ascend 
            to the position of the first Latin emperor of Constantinople. Motivated 
            by his Christian faith and the fervent desire to reclaim Jerusalem, 
            Baldwin viewed the Byzantine Empire, especially under the rule of 
            Alexios III Angelos, as a deserving target for retribution. These 
            factors fueled his determination to participate in the Fourth Crusade 
            and take decisive action against Constantinople.
            """
        )

    with st.expander("**Opinions on Governing Constantinople**"):
        st.markdown(
            """
            First and foremost, Baldwin wanted a
            Crusader Emperor with strong military and political credentials.
            Someone like himself. He preferred that he would be the one to
            sit on the throne of Constantinople. Baldwin also advocated for a feudal system
            similar to that in Western Europe, allowing for a divinely-
            sanctioned hereditary link between the emperor and his lords and
            allow for a strong but now overpowering emperor.
            """)

    with st.expander("**Opinions on Religion in Constantinople**"):
        st.markdown(
            """
            While Baldwin preferred to leave most of the religious decisions
            up to the Clergy, he still had a say. While a Latin patriarchy was
            fine he has seen the trouble it has caused in other nations so he
            preferred a dual patriarchy. One where the important doctrines were
            compromised, but smaller practices could be practiced in either a
            Greek or Latin manner.
            """
        )





