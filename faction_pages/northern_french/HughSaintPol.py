import streamlit as st


def app():
    st.image("images/hugh.svg", width=250)

    st.divider()
    bg, pwr = st.columns(2)
    with bg:
        st.markdown(
            """ 
            <h1 style='text-align: center;'>Hugh IV of Saint-Pol</h1>
            <p style='text-align: center'>
            Hugh IV of Saint-Pol, a member of the House of Campdavaine, served as
            the count of Saint-Pol from 1174 until 1205. Hugh distinguished himself in
            the Third Crusade alongside Philip I, Count of Flanders, particularly during
            the siege of Acre in 1191. Recognized for his service, he was granted lands by
            Philip II of France in 1194, including Pont-Sainte-Maxence, Verneuil, and Pontpoint.
            Joining the Fourth Crusade in 1200, his prior experience and status positioned
            him as one of the leading nobles. He played a significant role in the
            conquest of Constantinople in 1204. Notably, in an effort to control the city's
            pillaging, he took action by executing one of his own knights. </p>
            """, unsafe_allow_html=True
        )
    with pwr:
        st.markdown(
            """
            <h1 style='text-align: center;'>Powers</h1>

            1. **Military Command**: As count, Hugh wielded authority over the armed
            forces within his domain. This empowered him to command troops, coordinate
            military campaigns, and mobilize his vassals and knights to provide military
            support in times of conflict.
            1. **Judicial Authority**: Serving as the ultimate judicial arbiter in his
            territories, Hugh exercised supreme jurisdiction over legal matters. He
            presided over courts of law, resolved disputes, and administered justice
            to maintain peace and order.
            1. **Economic Control**: Hugh held power over the economic resources of
            Saint-Pol. this included overseeing trade regulations, levying taxes, and
            supervising commercial activities in urban centers to stimulate economic
            growth.
            1. **Diplomatic Relations**: Engaging in diplomatic endeavors with neighboring
            rulers, monarchs, and foreign dignitaries formed a crucial aspect of Hugh's
            duties. He navigated diplomatic negotiations, facilitated treaty
            agreements, and fostered alliances to safeguard the interests of his realm.
            """, unsafe_allow_html=True
        )

    st.divider()

    with st.expander("**Opinions on Attacking Constantinople**"):
        st.markdown(
            """
            As a seasoned participant in the Third Crusade, Hugh recognized the
            strategic importance of Constantinople in the context of reclaiming
            Jerusalem. However, Hugh strictly viewed the expedition as a means to
            secure resources and support for the Crusaders' ultimate goal. He was
            also greatly concerned about dealing with those who choose to break
            their oath during the sack. 
            """
        )

    with st.expander("**Opinions on Governing Constantinople**"):
        st.markdown(
            """
            Similar to the other members of the Northern French, Hugh advocated for
            a feudal system, similar to that in Western Europe. He also advocated for
            the importance of maintaining law and order, not just for the residence
            of Constantinople but also for the Emperor as well. He believed that while
            the emperor should be stronger than any other noble in the city, he should
            still be checked and balanced in order to avoid a emperor with too much
            power.
            """
        )

    with st.expander("**Opinions on Religion in Constantinople**"):
        st.markdown(
            """
            Hugh's position, again similar to that of his other Frenchmen, believed
            that a dual patriarchy was beneficial to uniting the city of Constantinople.
            He believed that while every practitioner of Christianity should be allowed
            to practice the way they prefer, the major doctrines of the Christian religion
            should be agreed upon by both the Greeks and the Latins.
            """
        )

