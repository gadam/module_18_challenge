# PyChain Ledger
################################################################################
# This app builds a ledger using the `blockchain` approach

# Step 1: Creates a Record Data Class
# * Creates a new data class named `Record`. This class will serve as the
# blueprint for the financial transaction records that the blocks of the ledger
# will store.

# Step 2: Adds relevant user inputs to the Streamlit Interface
# * Creates additional user input areas in the Streamlit application. These
# input areas collect the relevant information for each financial record
# that are stored in the `PyChain` ledger.

################################################################################
# Imports
import streamlit as st
import datetime as datetime
import pandas as pd
from pychain import Record, Block, PyChain
################################################################################
# Streamlit Code

# Adds the cache decorator for Streamlit

@st.cache(allow_output_mutation=True)
def setup():
    """Create the genesis block and add to the pychain"""
    print("Initializing Chain")
    return PyChain([Block("Genesis", 0)])


st.markdown("# PyChain")
st.markdown("## Store a Transaction Record in the PyChain")

pychain = setup()

################################################################################
# Step 2:
# Add Relevant User Inputs to the Streamlit Interface

# Add an input area for `sender` from the user.
sender_input = st.text_input("Sender")

# Add an input area for `receiver` from the user.
receiver_input = st.text_input("Receiver")

# Add an input area for `amount` from the user.
amount_input = st.number_input("Amount")

if st.button("Add Block"):
    prev_block = pychain.chain[-1]
    prev_block_hash = prev_block.hash_block()

    # Update `new_block` so that `Block` consists of an attribute named `record`
    # which is set equal to a `Record` that contains the `sender`, `receiver`,
    # and `amount` values
    new_block = Block(
        record = Record(
            sender = sender_input,
            receiver = receiver_input,
            amount=amount_input
        ),
        creator_id=42,
        prev_hash=prev_block_hash
    )

    pychain.add_block(new_block)
    st.balloons()

################################################################################
# Streamlit Code (continues)

st.markdown("## The PyChain Ledger")

pychain_df = pd.DataFrame(pychain.chain).astype(str)
st.write(pychain_df)

difficulty = st.sidebar.slider("Block Difficulty", 1, 5, 2)
pychain.difficulty = difficulty

st.sidebar.write("# Block Inspector")
selected_block = st.sidebar.selectbox(
    "Which block would you like to see?", pychain.chain
)

st.sidebar.write(selected_block)

if st.button("Validate Chain"):
    st.write(pychain.is_valid())


