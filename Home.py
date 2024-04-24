import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon=None,
    initial_sidebar_state="expanded",
    layout="wide"
)

st.markdown(  # Sets width of sidebar
            f"""
            <style>
                section[data-testid="stSidebar"] {{
                    width: 201px !important;
                }}
            </style>
            """,
            unsafe_allow_html=True
        )

st.markdown("<h1 style='text-align: center;'>The Leaders of the Fourth Crusade</h1>", unsafe_allow_html=True)
st.markdown("""<p style = 'text-align: center;'>
The Fourth Crusade, called by Pope Innocent III, 
aimed to recapture the city of 
Jerusalem from Muslim control. To get there, the Crusaders requested from the 
Venetians, a dedicated fleet to transport the invasion force. Due to an
overestimation of their army's size, the Crusaders were unable to compensate the
Venetians adequately, so Doge, Enrico Dandolo, agrees to postpone payment as 
long as they back him in his attack on Zara, a city backed by Catholic Crusaders. 
With no other option, they agree. Zara is then brought under Venetian control and 
the Crusaders are temporarily excommunicated by the Pope. Despite this, the 
Crusaders continued to Jerusalem. On the way, the Crusaders came to an agreement 
with the Byzantine prince, Alexios IV Angelos, to help him restore his deposed 
father, Isaac II Angelos, as emperor after he was overthrowing by his own brother, 
Alexios III Angelos. The Crusaders agree to Alexios IV's proposal in exchange for 
monetary funding and additional manpower to support the Crusade. Leading to the siege 
of Constantinople in 1203 resulting in the fall of Alexios V and Alexios IV being crowned 
co-emperor alongside Isaac II. Despite the Crusaders fulfilling their end of the 
deal, Alexios IV refused to provide a majority of the agreed-upon support. This 
continued until he was deposed by an uprising led by Alexios V Doukas who was openly 
anti-crusader; depriving the Crusaders of any chance they had of getting the 
remaining bounty they were owed. At this point, the Crusaders held a council to 
decide whether they should invade Constantinople, overthrowing Alexios V, and if 
so, how they should handle various political affairs in the city such as who to 
crown as Emperor and what system of government the city should follow. As you will 
see through the accounts of various leaders of the Fourth Crusade, many members of 
the council were conflicted about whether to attack Constantinople in the first place and 
even further divided on the political aspects of their new Latin Empire.
</p>
""", unsafe_allow_html=True)
st.divider()


def page_btn(label: str, page: str):
    if st.button(label=label, use_container_width=True):
        st.switch_page(page)


st.markdown("<h1 style='text-align: center; margin-bottom: 0.30em'>Affiliations</h1>", unsafe_allow_html=True)
nfr, imp, ven, cle, ind = st.columns(5)
nfr_btn, imp_btn, ven_btn, cle_btn, ind_btn = st.columns(5)

with nfr:
    st.image("images/north_french.svg")
with nfr_btn:
    page_btn("**The Northern French**", "pages/1_The_Northern_French.py")

with ven:
    st.image("images/venetian.svg")
with ven_btn:
    page_btn("**The Venetians**", "pages/3_The_Venetians.py")

with imp:
    st.image("images/imperial.svg")
with imp_btn:
    page_btn("**The Imperials**", "pages/2_The_Imperials.py")

with cle:
    st.image("images/clergy.svg")
with cle_btn:
    page_btn("**The Clergy**", "pages/4_The_Clergy.py")

with ind:
    st.image("images/indeterminate.svg")
with ind_btn:
    page_btn("**The Indeterminates**", "pages/5_The_Indeterminates.py")

st.divider()

left, right = st.columns(2)
with left:
    st.markdown("<p style='text-align: left;'><i>HTS 3030</i></p>", unsafe_allow_html=True)
with right:
    st.markdown("<p style='text-align: right;'><i>Kyle Sanquist</i></p>", unsafe_allow_html=True)



