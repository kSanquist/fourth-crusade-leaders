import streamlit as st


def app():
    st.image("images/conrad.jpg", width=600)

    st.divider()
    bg, pwr = st.columns(2)
    with bg:
        st.markdown(
            """ 
            <h1 style='text-align: center;'>Conrad of Krosigk</h1>
            <p style='text-align: center'>
            Conrad of Krosigk, a nobleman from a prestigious family, played a
            significant role in the Fouth Crusade. Rising through the ranks of
            the church due to family connections, Conrad became the Bishop of
            Halberstadt in 1202. Despite facing many challenges as Bishop, 
            including a rebellion by vassals and subsequent excommunication, 
            Conrad joined the Fourth Crusade in 1202. Although excommunicated,
            Conrad was treated as an equal among other bishops on the crusade.
            He supported the diversion of the crusade to Constantinople and
            participated in the assault on the city in 1204. Conrad was also
            involved in the election of Baldwin of Flanders as emperor.
            </p>
            """, unsafe_allow_html=True
        )
    with pwr:
        st.markdown(
            """
            <h1 style='text-align: center;'>Powers</h1>

            1. **Spiritual Authority**: As a bishop, Conrad wielded spiritual
            authority over the clergy and faithful. This included the ability
            to administer sacraments oversee religious instruction, and enforce
            church discipline.
            1. **Leadership Role**: Conrad assumed a leadership role among the
            crusaders, particularly those from his region. Despine being
            excommunicated, he was treated with respect and rgarded as an equal.
            1. **Moral Influence**: Conrad's presence on the crusade provided
            moral guidance and inspiration to fellow crusaders. His participation
            in the campaign demonstrates his commitment to the cause.
            """, unsafe_allow_html=True
        )

    st.divider()

    with st.expander("**Opinions on Attacking Constantinople**"):
        st.markdown(
            """
            Conrad of Krosigk was in favor of the diversion of the Fourth Crusade
            to Constantinople and supported the decision to attack the city. Conrad
            believed in the Crusaders' mission to secure resources from Constantinople
            for their campaign and to restore Christian rule in the region. It is
            likely that due to his excommunication before the crusade, he might have
            thought of the attack of Constantinople as an opportunity for himself, or
            at least the excommunication made it easier for him to not follow the
            Pope's wishes.
            """
        )

    with st.expander("**Opinions on Governing Constantinople**"):
        st.markdown(
            """
            Conrad's active participation in the election of Baldwin of Flanders
            as emperor and his involvement in the coronation ceremony show that he
            supported not only the establishment of a Latin Empire in Constantinople
            but a crusader emperor as well and probably a feudal system to boot. 
            As a bishop and participant in the Fourth Crusade, Conrad believed in 
            the necessity of establishing Christian rule in the captured territories
            """)

    with st.expander("**Opinions on Religion in Constantinople**"):
        st.markdown(
            """
            As a bishop and participant in the crusade, Conrad supported the Catholic
            Church's efforts to establish its authority in the city. Being that he
            was excommunicated, it is possible he saw Catholicism in Constantinople
            as an opportunity to make himself the Latin Patriarch or at least a lower
            vassal of the Patriarch.
            """
        )





