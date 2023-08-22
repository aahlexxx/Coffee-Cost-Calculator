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

    st.header("Input Costs:")
    fertilizer1 = st.number_input(label="Enter the cost of Fertilizer 1 per kilogram: ", min_value=0.00, step=0.05)
    fertilizer1qty = st.number_input(label="Enter the number of kilos of Fertilizer 1 used: ", min_value=0.00, step=0.05)
    fertilizer2 = st.number_input(label="Enter the cost of Fertilizer 2 per kilogram: ", min_value=0.00, step=0.05)
    fertilizer2qty = st.number_input(label="Enter the number of kilos of Fertilizer 2 used: ", min_value=0.00, step=0.05)
    organic_fertilizer = st.number_input(label="Enter the cost of Organic Fertilizer per kilogram: ", min_value=0.00, step=0.05)
    organic_fertilizer_qty = st.number_input(label="Enter the number of kilos of Organic Fertilizer used: ", min_value=0.00, step=0.05)
    herbicide = st.number_input(label="Enter the cost of Herbicide per kilogram: ", min_value=0.00, step=0.05)
    herbicide_qty = st.number_input(label="Enter the number of kilos of Herbicide used: ", min_value=0.00, step=0.05)
    pesticide = st.number_input(label="Enter the cost of Pesticide per kilogram: ", min_value=0.00, step=0.05)
    pesticide_qty = st.number_input(label="Enter the number of kilos of Pesticide used: ", min_value=0.00, step=0.05)

    st.header("Labor Costs:")
    pruning = st.radio("Did you incur any labor costs for Pruning?:", ("Yes", "No"))
    if pruning == "Yes":
      pruning = 1
    fertilizing = st.radio("Did you incur any labor costs for Fertilizing?:", ("Yes", "No"))
    if fertilizing == "Yes":
      pruning = 1
    spraying = st.radio("Did you incur any labor costs for Spraying?:", ("Yes", "No"))
    harvesting = st.radio("Did you incur any labor costs for Harvesting?:", ("Yes", "No"))
    rejuvenation = st.radio("Did you incur any labor costs for Rejuvenation?:", ("Yes", "No"))
    weeding = st.radio("Did you incur any labor costs for Weeding?:", ("Yes", "No"))

    st.header("Other Costs:")
    transportation = st.radio("Did you incur any labor costs for Transportation?:", ("Yes", "No"))
    other_cost = st.number_input(label="Enter the amount you spent for other costs: ", min_value=0.00, step=0.05)

if coffee_type == "Green Coffee Beans" or "Both":
    st.header("Other Costs:")
    transportation = st.radio("Did you incur any labor costs for Transportation?:", ("Yes", "No"))
    other_cost = st.number_input(label="Enter the amount you spent for other costs: ", min_value=0.00, step=0.05)


def calculate():
    input_cost = (
        fertilizer1 * fertilizer1qty +
        fertilizer2 * fertilizer2qty +
        organic_fertilizer * organic_fertilizer_qty +
        herbicide * herbicide_qty +
        pesticide * pesticide_qty
    )
    labor_cost = (
        pruning + fertilizing + spraying + harvesting + rejuvenation + weeding
    )

    return input_cost, labor_cost


if st.button("Calculate"):
    input_cost, labor_cost = calculate()
    st.write("Input Cost: ", input_cost)
    st.write("Labor Cost: ", labor_cost)
    st.write("Other Costs: ", other_cost)
    st.write("Total Cost: ", input_cost + labor_cost + other_cost)
