import streamlit as st


def app():
    st.image("images/louis.jpg")

    st.divider()
    bg, pwr = st.columns(2)
    with bg:
        st.markdown(
            """ 
            <h1 style='text-align: center;'>Louis I of Blois</h1>
            <p style='text-align: center'>
            Louis I of Blois, born in 1172 and ruling as Count of Blois from 1191
            to 1205, emerged as a significant figure in both European politics and
            the Crusades. Descended from a distinguished lineage, being the son of
            Theobald V and Alix of France, he inherited a legacy intertwined with
            the royal families of France and England. Louis displayed early martial
            prowess by joining his father on the Third Crusade during his teen
            years. Louis's pivotal role in history unfolded with his participation
            in the Fourth Crusade. He and his cousin Theobald III of Champagne were
            among the first to commit to the crusade. Departing France in 1202 with
            support from his uncle King John of England, Louis played a pivotal
            role in the siege of Constantinople in July 1203 While Louis was unable 
            to participate in the capture of Constantinople in 1204 due to a fever, 
            he maintained is dedication to the cause. </p>
            """, unsafe_allow_html=True
        )
    with pwr:
        st.markdown(
            """
            <h1 style='text-align: center;'>Powers</h1>
    
            1. **Command of Armies**: As the count, Louis held authority over the
            military forces within his realm. This allowed him to assemble armies,
            orchestrate military expeditions, and summon his vassals and knights to
            render military assistance during times of strife.
            2. **Judicial Supremacy**: Functioning as the highest judicial figure in
            his territories, the count exercised paramount authority over legal matters.
            He chaired courts, settled disputes, and served justice to uphold law and order.
            3. **Economic Oversight**: Louis held control over the economic assets of Blois.
            This encompassed the regulation of trade, imposition of taxes, and supervision of
            urban markets to ensure economic prosperity.
            4. **Diplomatic Endeavors**: Engaging in diplomatic affairs with neighboring lords,
            monarchs, and external nobles was a crucial aspect of the count's responsibilities.
            Louis navigated negotiations, brokered treaties, and forged alliances to safeguard the
            welfare of his people.
            """, unsafe_allow_html=True
        )

    st.divider()

    with st.expander("**Opinions on Attacking Constantinople**"):
        st.markdown(
            """
            While Louis understood the necessity of capturing Constantinople due to
            the Crusader's debt to the Venetians as well as the strategic benefits of
            doing so. He was cautious about the strength of the city's defenses and
            the readiness of the Crusader forces. Additionally, he was concerned about
            the moral implications of launching an attack on fellow Christians and the
            impact it may have on the reputation among other Christian powers. While 
            uncertain, Louis went with his fellow Frenchmen, including Baldwin, and
            deemed it necessary to invade Constantinople.
            """
        )

    with st.expander("**Opinions on Governing Constantinople**"):
        st.markdown(
            """
            Louis of Blois advocates for a pragmatic approach to governing 
            Constantinople, emphasizing the importance of selecting a capable 
            emperor to ensure stability. He proposes a government structure 
             combines feudalism, representative councils, and bureaucratic
              administration for inclusive decision-making. Louis highlights the 
              need to revitalize trade, promote commerce, and invest in 
              infrastructure for economic growth. Diplomatic relations with 
              neighboring powers are crucial, requiring negotiation of treaties 
              while respecting sovereignty. Louis also emphasizes inclusive 
              policies to recognize the city's multicultural nature, promoting 
              religious freedoms and social cohesion.
            """
        )

    with st.expander("**Opinions on Religion in Constantinople**"):
        st.markdown(
            """
            Louis of Blois advocates for a policy of religious tolerance in 
            Constantinople, recognizing the city's diverse population and cultural 
            heritage. He proposes a dual patriarchy system, allowing both Latin and 
            Greek patriarchies to coexist and serve their respective communities. 
            This approach aims to foster unity and cooperation among the city's 
            religious groups, promoting harmony and mutual respect.
            """
        )







