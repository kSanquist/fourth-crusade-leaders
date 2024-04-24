import streamlit as st


def app():
    st.image("images/enrico.png", width=270)

    st.divider()
    bg, pwr = st.columns(2)
    with bg:
        st.markdown(
            """ 
            <h1 style='text-align: center;'>Enrico Dandolo</h1>
            <p style='text-align: center'>
            Enrico Dandolo became the Doge of Venice in 1192, and is known for his
            role in the Fourth Crusade, particularly the diversion to and the
            sack of Constantinople in 1204. Despite being in is 80s and blind, he
            managed to be an effective commander during the Crusade. While Dandolo
            made significant reforms in Venice, his leadership took a turn in
            1202 when he negotiated with the French envoys of the Fourth Crusade,
            leading to Venice's role in providing a fleet and supplies in exchange
            for a substantial payment and a share of the Crusader's spoils. Despite
            financial strains this placed on Venice when the Crusaders could not
            meet their financial obligations, Dandolo maneuvered to maintain the
            city's involvement by suggesting the Crusaders back him in attacking
            Zara. This decision led to the excommunication of the Venetians by Pope
            Innocent III. However, his actions in the Fourth Crusade would leave
            him known as a pious leader and skilled diplomat who significantly
            expanded Venetian power and influence.
            </p>
            """, unsafe_allow_html=True
        )
    with pwr:
        st.markdown(
            """
            <h1 style='text-align: center;'>Powers</h1>
    
            1. **Commander-in-Chief**: Dandol severed as the supreme military
            leader of Venice. He had the power to command the Venetian armed forces
            and to make strategic decisions regarding military campaigns and
            engagements
            1. **Diplomatic Authority**: Dandolo had the authority to conduct
            diplomatic relations with other states and entities. He represented
            Venice in negotiations, treaties, and alliances.
            1. **Judicial Oversight**: Although Venice had separate judicial bodies,
            the Doge played a role in the administration of justice. He could grant
            pardons, commute sentences, and intervene in legal matters when
            deemed necessary.
            1. **Financial Control**: Dandolo had authority over Venice's finances,
            including the management of state revenues, expenditures, and taxation.
            He could propose budgets, allocate funds, and oversee economic policies.
            1. **Religious Authority**: While Venice maintained separation of church
            and state, the Doge had influence over religious matters within the Republic.
            He could support or suppress religious institutions, influence the selection
            of clergy, and participate in ceremonial and religious events.
            """, unsafe_allow_html=True
        )

    st.divider()

    with st.expander("**Opinions on Attacking Constantinople**"):
        st.markdown(
            """
            As Doge of Venice, Dandolo recognized the strategic significance
            of Constantinople as a gateway to both Europe and Asia, viewing its
            conquest as not only a means to get the reimbursement owed by the 
            Crusaders, but also as an opportunity to expand Venetian power and secure
            lucrative trade routes. He also understood the vulnerabilities of the
            Byzantine Empire and believed that capturing Constantinople would serve
            Venetian interests while weakening potential rivals in the region. Thus,
            Dandolo's would have advocated strongly for the attack on Constantinople.
            """
        )

    with st.expander("**Opinions on Governing Constantinople**"):
        st.markdown(
            """
            Given Dandolo's role in orchestrating the Fourth Crusade's conquest of
            Constantinople, Dandolo favored a governance structure that would ensure
            Venetian dominance and economic prosperity in the region. He advocated
            for a system that allowed Venetian merchants to maintain their
            commercial privileges and exploit the resources of the Byzantine Empire
            while also preserving stability and order to facilitate trade.
            """)

    with st.expander("**Opinions on Religion in Constantinople**"):
        st.markdown(
            """
            While Dandolo's primary objective was to facilitate trade in the new
            Latin Empire, he probably saw that in order to maintain these lucrative
            trade routes for the Venetian people in the empire, there would need to be
            cooperation between the two major forms of Christian religion in the 
            empire: the Greek Orthodox and Latin Catholics. Therefore, Dandolo
            advocated for a dual patriarchy allowing the least amount of oppression and
            religious tension in order to keep the empire, and subsequently the Venetian's
            trade routes, secure.
            """
        )





