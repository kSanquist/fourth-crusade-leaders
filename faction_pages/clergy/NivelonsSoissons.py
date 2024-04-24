import streamlit as st


def app():
    st.image("images/nivelon.png")

    st.divider()
    bg, pwr = st.columns(2)
    with bg:
        st.markdown(
            """ 
            <h1 style='text-align: center;'>Nivelon de Quierzy</h1>
            <p style='text-align: center'>
            As the bishop of Soissons, Nivelon de Quierzy organized assemblies
            to discuss the crusade's objectives and strategy. Despite being
            tasked by Pope Innocent III to dissuade the crusaders from attacking
            Constantinople, Nivelon not only failed to convey the message but also
            actively preached in favor of the invasion, portraying the Greeks as
            "schismatic and traitorous" Nivelon's direct involvement in the naval
            attack against Constantinople, commanding the Paradise ship, further
            highlights his active participation in the campaign. Nivelon was also
            one of twelve electors who installed Baldwin IX of Flanders as emperor
            of Constantinople. After the capture of Constantinople, Nivelon
            acquired and redistributed relics, demonstrating his commitment to
            both spiritual and material aspects of the crusade's objectives.
            </p>
            """, unsafe_allow_html=True
        )
    with pwr:
        st.markdown(
            """
            <h1 style='text-align: center;'>Powers</h1>

            1.**Ecclesiastical Authority**: As bishop of Soissons, Nivelon held
            significant ecclesiastical power over the clergy. This authority
            allowed him to organize and mobilize support for the crusade within
            his jurisdiction.
            1. **Preaching Authority**: Nivelon's position as a bishop granted him
            the authority to preach and spread religious teachings. Despite being
            tasked by Pope Innocent III to discourage attacking Constantinople,
            Nivelon preached in favor of the invasion.
            1. **Political Influence**: Nivelon's involvement in the election of 
            Baldwin as emperor of Constantinople highlights his political influence
            within crusader leadership.
            1. **Relic Acquisition and Redistribution**: Nivelon was acquired numerous
            relics from the city of Constantinople and was given authority to
            redistribute them to various churches, including his own cathedral in
            Soissons.
            """, unsafe_allow_html=True
        )

    st.divider()

    with st.expander("**Opinions on Attacking Constantinople**"):
        st.markdown(
            """
            Nivelon's stance on attacking Constantinople could not have been more
            supportive, reflecting a blend of religious fervor and strategic alignment
            with the goals of the Fourth Crusade. Nivelon preached in favor of attacking
            Constantinople framing the Greeks as traitorous heathens, going against
            the Pope's own wishes. Nivelon also actively participate in the military
            campagin, commanding a ship that played a crucial role in the naval
            assault showing how truly supportive he was for taking Constantinople.
            """
        )

    with st.expander("**Opinions on Governing Constantinople**"):
        st.markdown(
            """
            Nivelon's active involvement in the crusade's planning shows he
            supported a system of government that aligned with the interest of the
            crusaders and their allies. This stance his close association with
            Boniface. That being a feudal system with a crusader emperor on the
            throne of the new Latin Empire.
            """)

    with st.expander("**Opinions on Religion in Constantinople**"):
        st.markdown(
            """
            Nivelon preached that an invasion of Constantinople was justifiable
            calling the Orthodox Greeks heathens, therefore, it can be justified
            that Nivelon prefered a strictly Latin Patriarch and would be
            adamantly driven to convert all of those who did not worship
            Catholicism in the walls of Constantinople.
            """
        )





