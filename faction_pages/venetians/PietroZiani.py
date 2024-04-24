import streamlit as st


def app():
    st.image("images/pietro.jpg")

    st.divider()
    bg, pwr = st.columns(2)
    with bg:
        st.markdown(
            """ 
            <h1 style='text-align: center;'>Pietro Ziani</h1>
            <p style='text-align: center'>
            Pietro Ziani, the 42nd Doge of Venice, ruled following the esteemed leadership
            of Enrico Dandolo. Hailing from the Ziani family, he was no stranger to
            the maritime world, having begun his career as a sailor and participating
            in the Fourth Crusade and consequential sacking of Constantinople. Upon his
            ascension to Doge, Ziani contemplated relocating Venice's capital to
            Constantinople, but it was vetoed by thee council. Instead, he focused on
            consolidating Venetian assets within the Latin Empire. Ziani also fostered
            commericial relations with post-Byzantine states and sought to maintain
            peace allowing Venice to concentrate on its expanding Greek territories.
            </p>
            """, unsafe_allow_html=True
        )
    with pwr:
        st.markdown(
            """
            <h1 style='text-align: center;'>Powers</h1>

            During the Fourth Crusade, aside from his expertise in sailing and his
            familial influence, Pietro Ziani lacked considerable influence, however,
            through these experiences, his family connections, and his interest in
            increasing Venetian influence in Constantinople, Ziani became the 42nd
            Doge following Dandolo and gained the powers mentioned that Enrico Dandolo
            had, that being militaristic, financial, judicial, and religious authority
            over Venice and its territories.
            """, unsafe_allow_html=True
        )

    st.divider()

    with st.expander("**Opinions on Attacking Constantinople**"):
        st.markdown(
            """
            Pietro Ziani's stance on attacking Constantinople was supportive,
            considering his active participation the the campaign and the
            subsequent events that unfolded. Ziani was deeply involved in the
            decision-making process leading up to the assault on Constantinople and
            his role as a sailor during the Crusade highlight Ziani's familiarity
            with military operations and strategic planning, showing that he
            understood the benefits of capturing the city.
            """
        )

    with st.expander("**Opinions on Governing Constantinople**"):
        st.markdown(
            """
            Pietro Ziani's views on the governance of Constantinople revolved around
            establishing Venetian influence and securing favorable arrangements
            for Venice within the newly acquired territories. Ziani favored a
            system of governance in Constantinople that allowed Venice to
            maintain significant control over trade routes, commercial activities, and
            key strategic assets in the region. Given Venice's republic tradition and
            decentralized nature of government, Ziani favored a form of government in
            Constantinople that mirrored Venice's own political structure to some
            extent. In fact, as seen by Ziani's interest in moving the capital of
            Venice to Constantinople, Ziani preferred Doge Dandolo as emperor of the
            Latin Empire leading to Ziani himself later becoming emperor.
            """)

    with st.expander("**Opinions on Religion in Constantinople**"):
        st.markdown(
            """
            As a leader of a predominantly Catholic city-state, Ziani would have
            likely sought to promote the interests of the Catholic Church in
            Constantinople and therefore prefer a signular Latin Patriarch. 
            That being said, given the diverse religious landscape
            of Constantinople, Ziani also tolerated the idea of a dual Patriarchy
            where Latin and Greek Christians worked together to find a compromise
            providing solidarity for the future of Constantinople.
            """
        )





