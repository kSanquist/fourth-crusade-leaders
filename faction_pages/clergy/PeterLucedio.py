import streamlit as st


def app():
    st.image("images/peter.svg", width=300)

    st.divider()
    bg, pwr = st.columns(2)
    with bg:
        st.markdown(
            """ 
            <h1 style='text-align: center;'>Peter of Lucedio</h1>
            <p style='text-align: center'>
            Peter's experience as an administrator and mediator coupled with is
            deep connections with both the secular and ecclesiastical realms,
            positioned him to play a significant role in the Fourth Crusade. His
            involvement began in 1201 when he joined Boniface of Montferrat,
            in the initial preparations. His journey alongside Boniface and his
            participation in the gathering of Crusaders in Venice, highlights the
            trust placed in him by both ecclesiastical and secular leaders. During
            the crusade, Peter's role extended beyond participation. He was
            entrusted with a letter from Pope Innocent III directed to the crusading
            army, instructing them against attacking the Christian city of Zara.
            While the letter was not effective in warding off the attack from the
            Crusaders on Zara, Peter's involvement showcases his responsibility in
            aligning crusader's actions with that of the papacy. Peter was also
            involved in key negotiations such as persuading Emperor Alexius IV's
            widow to convert to Catholic faith, and selecting a new emperor
            after the sack of Constantinople.
            </p>
            """, unsafe_allow_html=True
        )
    with pwr:
        st.markdown(
            """
            <h1 style='text-align: center;'>Powers</h1>
    
            1. **Abbot of Lucedio**: As the abbot, Peter had full administrative authority
            over the abbey, including its financial and land assets, and he had significant
            influencei in religious and local political matters within the region.
            1. **Papal Judge-Delegate**: This role gave him the authority to handle disputes
            on behalf of the Pope. It involved resolving conflicts between various
            ecclesiastical and secular figures.
            1. **Advisor and Mediator**: Peter's close relationship with Pope Innocent III and
            various European nobility, including Boniface of Montferrat, positioned him as a
            key advisor and mediator. This role was particularly crucial during negotiations
            and decision-making processes throughout the crusade.
            1. **Elector of New Emperor**: Peter was one of twelve electors chosen to select
            a new emperor for the Latin Empire. This role granted him significant political
            influence over future leadership.
            1. **Diplomatic Envoy**: As a diplomatic envoy, Peter carried important papal
            letters and participated in negotiating ecclesiastical reunification efforts,
            such as converting key figures to the Catholic faith and persuading them
            to restore communion between the Eastern Orthodox and Roman Catholic Churches.
            """, unsafe_allow_html=True
        )

    st.divider()

    with st.expander("**Opinions on Attacking Constantinople**"):
        st.markdown(
            """
            As a papal envoy and representative of Pope Innocent III, who had openly
            criticised the diversion of the Crusade toward attacking the Christian
            city of Zara, Peter harbored similar reservations about the siege of
            Constantinople. He preferred to avoid conflicts with fellow Christians and
            preferred the Crusaders focus on the original goal of the Crusade aimed
            at reclaiming the Holy Land.
            """
        )

    with st.expander("**Opinions on Governing Constantinople**"):
        st.markdown(
            """
            As a Cistercian monk and prelate, his primary concerns revolved around
            spiritual matters as opposed to secular governance. Therefore, instead
            of reasoning for a specific form of government, Peter supported a
            government that would uphold Christian principles and promote stability and 
            peace within the city. And as a representative of the Church, he advocated
            for a form of government that respected Latin, religious institutions and
            provided for the spiritual needs of the population.
            """)

    with st.expander("**Opinions on Religion in Constantinople**"):
        st.markdown(
            """
            As a high-ranking ecclesiastic figure and representative of the Latin
            Church, Peter supported the establishment of a strictly Latin Patriarch in
            Constantinople. The Latin Patriarch would represent the interests of the
            Catholic Church in the city and facilitate the integration of Constantinople
            into the broader Latin Christan world. A full Latin Patriarchy in Constantinople
            would also facilitate toward the conversion of Greek Orthodox members to Latin
            Catholicism in Constantinople.
            """
        )





