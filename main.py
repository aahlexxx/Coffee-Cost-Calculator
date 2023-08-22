import streamlit as st

st.title("Coffee Production Calculator")
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

st.header("Production Costs:")
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

st.header("Post Production Costs:")

def calculate():
    productioncost = (
        fertilizer1 * fertilizer1qty +
        fertilizer2 * fertilizer2qty +
        organicfertilizer * organicfertilizerqty +
        herbicide * herbicideqty +
        pesticide * pesticideqty
    )
    return productioncost

if st.button("Calculate"):
    productioncost = calculate()
    st.write("Production Cost: ", productioncost)
    st.write("Post Production Cost: ", productioncost)
