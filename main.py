import streamlit as st

st.title("Coffee Production Cost Calculator")
st.write("---")

coffee_trees = st.number_input(label="How many coffee trees are there in your farm?", min_value=1, step=1)
coffee_variety = st.radio("Select the variety of your Coffee:",
                          ("Robusta", "Arabica", "Excelsa"))
coffee_type = st.radio("Select the type of Coffee you will sell:",
                       ("Fresh", "Green Coffee Beans", "Both"))

if coffee_variety == "Robusta":
    h = 1
elif coffee_variety == "Arabica":
    h = 2
elif coffee_variety == "Excelsa":
    h = 3

if coffee_type == "Fresh":
  st.header("Input Costs:")
  fertilizer1 = st.number_input(label="Enter the cost of Fertilizer 1 per kilogram: ", min_value=0.00, step=0.05)
  fertilizer1qty = st.number_input(label="Enter the number of kilos of Fertilizer 1 used: ", min_value=0.00, step=0.05)
  fertilizer2 = st.number_input(label="Enter the cost of Fertilizer 2 per kilogram: ", min_value=0.00, step=0.05)
  fertilizer2qty = st.number_input(label="Enter the number of kilos of Fertilizer 2 used: ", min_value=0.00, step=0.05)
  organicfertilizer = st.number_input(label="Enter the cost of Organic Fertilizer per kilogram: ", min_value=0.00, step=0.05)
  organicfertilizerqty = st.number_input(label="Enter the number of kilos of Organic Fertilizer used: ", min_value=0.00, step=0.05)
  herbicide = st.number_input(label="Enter the cost of Herbicide per kilogram: ", min_value=0.00, step=0.05)
  herbicideqty = st.number_input(label="Enter the number of kilos of Herbicide used: ", min_value=0.00, step=0.05)
  pesticide = st.number_input(label="Enter the cost of Pesticide per kilogram: ", min_value=0.00, step=0.05)
  pesticideqty = st.number_input(label="Enter the number of kilos of Pesticide used: ", min_value=0.00, step=0.05)
  
  st.header("Labor Costs:")
  pruning = st.radio("Did you incur any labor costs for Pruning?:",
                       ("Yes", "No"))
  fertilizing = st.radio("Did you incur any labor costs for Fertilizing?:",
                       ("Yes", "No"))
  spraying = st.radio("Did you incur any labor costs for Spraying?:",
                       ("Yes", "No"))
  harvesting = st.radio("Did you incur any labor costs for Harvesting?:",
                       ("Yes", "No"))
  rejuvenation = st.radio("Did you incur any labor costs for Rejuvenation?:",
                       ("Yes", "No"))
  weeding = st.radio("Did you incur any labor costs for Weeding?:",
                       ("Yes", "No"))

  st.header("Other Costs:")
  transportation = st.radio("Did you incur any labor costs for Transportation?:",
                       ("Yes", "No"))
  other = st.number_input(label="Enter the amount you spent for other costs: ", min_value=0.00, step=0.05)
  

def calculate():
    inputcost = (
        fertilizer1 * fertilizer1qty +
        fertilizer2 * fertilizer2qty +
        organicfertilizer * organicfertilizerqty +
        herbicide * herbicideqty +
        pesticide * pesticideqty
    )
    laborcost = (
        fertilizer1 * fertilizer1qty +
        fertilizer2 * fertilizer2qty +
        organicfertilizer * organicfertilizerqty +
        herbicide * herbicideqty +
        pesticide * pesticideqty
    )
    return inputcost, laborcost


if st.button("Calculate"):
    productioncost = calculate()
    st.write("Input Cost: ", inputcost)
    st.write("Labor Cost: ", laborcost)
    st.write("Other Costs: ", othercost)
    st.write("Post Production Cost: ", postproductioncost)
