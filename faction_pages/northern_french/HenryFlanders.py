import streamlit as st


def app():
    st.image("images/henry.jpg")

    st.divider()
    bg, pwr = st.columns(2)
    with bg:
        st.markdown(
            """ 
            <h1 style='text-align: center;'>Henry I of Flanders</h1>
            <p style='text-align: center'>
            Henry of Flanders' actions and alliances during the Fourth Crusade
            propelled him to prominence among the crusader ranks. Born into noble
            lineage as the son of Count Baldwin V of Hainaut and Countess Margaret I
            of Flanders, Henry demonstrated military prowess and leadership qualities
            from an early age. His participation in the siege of Constantinople in 1203
            showcased his strategic intelligence and valor on the battlefield. As one of
            the division generals alongside renowned leaders of the fourth crusade, Henry
            played a crucial role in the campaign's success. His daring expedition to
            secure supplies and raid enemy territory demonstrated his resourcefulness and
            determination. Despite facing ambushes and formidable adversaries, Henry
            emerged victorious, capturing relic and bolstering the morale of his fellow
            crusaders.
            </p>
            """, unsafe_allow_html=True
        )
    with pwr:
        st.markdown(
            """
            <h1 style='text-align: center;'>Powers</h1>
    
            1. **Military Leadership**: Henry wielded authority as a distinguished military leader,
            commanding troops and strategizing military campaigns during his participation in
            the Fourth Crusade. His role as a division general and his successful armed raid into
            Constantinople exemplified his military prowess and strategic astuteness.
            1. **Political Influence**: Born into noble lineage, Henry possessed inherent political
            influence within the crusader ranks. His familial connections and military achievements
            elevated his status.
            1. **Territorial Control**: Through his military exploits and political influence,
            Henry exerted control over territories and strategic locations within the crusader states.
            His actions during the siege of Constantinople and subsequent expeditions contributed
            to the expansion and consolidation of Latin rule in the region, securing valuable
            resources and territories for the new empire. 
            """, unsafe_allow_html=True
        )

    st.divider()

    with st.expander("**Opinions on Attacking Constantinople**"):
        st.markdown(
            """
            Henry's role as a division general during the siege of Constantinople
            in 1203 and 1204 shows that he supported the campaign to capture thje city.
            As a prominent leader within the crusader ranks, Henry aligned with the
            broader objectives of the expedition, which aimed to establish Latin rule
            in the Byzantine capital and secure resources for the Crusaders. His
            involvement in military engagement and strategic maneuvers during the 
            siege show his commitment to the campaign's success.
            """
        )

    with st.expander("**Opinions on Governing Constantinople**"):
        st.markdown(
            """
            Henry advocated for a strong centralized governance structure to
            maintain control over the conquered city and surrounding regions.
            Additionally, his active involvement in the political and military affairs
            of the Latin Empire show commitment to establishing and maintaining
            effective governance in Constantinple and its territories.
            """)

    with st.expander("**Opinions on Religion in Constantinople**"):
        st.markdown(
            """
            Similar to a majority of the cursaders, Henry adhered to the prevailing
            religious attitudes of the time. Henry suggested the promotion of Latin
            Christianity and the establishment of Catholic Institutions in Constantinople
            following its conquest.
            """
        )





