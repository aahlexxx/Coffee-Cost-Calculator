import streamlit as st

st.title("Coffee Production Cost Calculator")
st.write("---")

#initialize values
amount_gcb = 0
amount_fc = 0
hauling = 0
floating = 0
depulping = 0
drying = 0
dehulling = 0
sorting = 0
storage = 0
pruning = 0
fertilizing = 0
spraying = 0
harvesting = 0
rejuvenation = 0
weeding = 0

coffee_trees = st.number_input(label="How many coffee trees are there in your farm?", min_value=1, step=1)
coffee_variety = st.radio("Select the variety of your Coffee:",
                          ("Robusta", "Arabica", "Excelsa"))
coffee_type = st.radio("Select the type of Coffee you will sell:",
                       ("Fresh", "Green Coffee Beans", "Both"))
amount_fc = st.number_input(label="Enter the total amount of fresh coffee cherries you have harvested (in kilos)", min_value=0.00, step=0.05)
if coffee_type == "Green Coffee Beans" or coffee_type == "Both":
    amount_gcb = st.number_input(label="Enter the amount of coffee cherries you have successfully converted to Green Coffee Beans (in kilos)", min_value=0.00, step=0.05)

if coffee_variety == "Robusta":
    lb_hauling = 1
    lb_floating = 0.4167
    lb_depulping = 2
    lb_drying = 0.8685
    lb_dehulling = 2
    lb_sorting = 0.9925
    lb_storage = 0

    lb_pruning = 0.5
    lb_fertilizing = 0.3125
    lb_spraying = 0.3875
    lb_weeding = 1
    lb_harvesting = 0.8
    lb_rejuvenation = 0.075

    lb_transport = 0.4688

    m_hauling = 2.5
    m_floating = 0.4167
    m_depulping = 4.8
    m_drying = 3.125
    m_dehulling = 2.7
    m_sorting = 2
    m_storage = 0

    m_pruning = 1.25
    m_fertilizing = 0.75
    m_spraying = 0.6
    m_weeding = 2
    m_harvesting = 2
    m_rejuvenation = 0.225

    m_transport = 1

    ub_hauling = 5
    ub_floating = 0.4167
    ub_depulping = 10.9881
    ub_drying = 7.7778
    ub_dehulling = 5.2721
    ub_sorting = 4.2273
    ub_storage = 0

    ub_pruning = 3
    ub_fertilizing = 2.25
    ub_spraying = 2
    ub_weeding = 3.3333
    ub_harvesting = 5
    ub_rejuvenation = 1.1294

    ub_transport = 2.1212 

elif coffee_variety == "Arabica":
    lb_hauling = 0.625
    lb_floating = 0
    lb_depulping = 1.3636
    lb_drying = 2.5133
    lb_dehulling = 2
    lb_sorting = 1.9329
    lb_storage = 0

    lb_pruning = 0.5
    lb_fertilizing = 0.3125
    lb_spraying = 0.3875
    lb_weeding = 1
    lb_harvesting = 0.8
    lb_rejuvenation = 0.075

    lb_transport = 1

    m_hauling = 1.5
    m_floating = 0
    m_depulping = 2.1667
    m_drying = 4.3016
    m_dehulling = 2.5
    m_sorting = 2.7083
    m_storage = 0

    m_pruning = 1.5
    m_fertilizing = 0.7143
    m_spraying = 0.8356
    m_weeding = 1.6667
    m_harvesting = 3.4857
    m_rejuvenation = 0.55

    m_transport = 1.5

    ub_hauling = 1.7787
    ub_floating = 0
    ub_depulping = 7.5
    ub_drying = 7.7597
    ub_dehulling = 4.7839
    ub_sorting = 7.25
    ub_storage = 0

    ub_pruning = 3
    ub_fertilizing = 1.4318
    ub_spraying = 1.3125
    ub_weeding = 3.3333
    ub_harvesting = 6.8025
    ub_rejuvenation = 1.5

    ub_transport = 2.8833

elif coffee_variety == "Excelsa":
    lb_hauling = 1.1667
    lb_floating = 0
    lb_depulping = 2.1429
    lb_drying = 2.5149
    lb_dehulling = 2.475
    lb_sorting = 2.1429
    lb_storage = 0

    lb_pruning = 0.75
    lb_fertilizing = 0.9
    lb_spraying = 0.6711
    lb_weeding = 1.44
    lb_harvesting = 2.6846
    lb_rejuvenation = 0.45833

    lb_transport = 1.1765

    m_hauling = 1.6
    m_floating = 0
    m_depulping = 3.2078
    m_drying = 4.1833
    m_dehulling = 4
    m_sorting = 3.3333
    m_storage = 0

    m_pruning = 1.3423
    m_fertilizing = 2.52
    m_spraying = 1.5
    m_weeding = 3
    m_harvesting = 7.05
    m_rejuvenation = 0.75

    m_transport = 1.8182

    ub_hauling = 2.2222
    ub_floating = 0
    ub_depulping = 17.8014
    ub_drying = 8.1433
    ub_dehulling = 6.0909
    ub_sorting = 19
    ub_storage = 0

    ub_pruning = 2.9
    ub_fertilizing = 8
    ub_spraying = 3
    ub_weeding = 9.5313
    ub_harvesting = 12
    ub_rejuvenation = 1.5

    ub_transport = 3 

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
pruning = 1 if pruning == "Yes" else 0
fertilizing = st.radio("Did you incur any labor costs for Fertilizing?:", ("Yes", "No"))
fertilizing = 1 if fertilizing == "Yes" else 0
spraying = st.radio("Did you incur any labor costs for Spraying?:", ("Yes", "No"))
if spraying == "Yes":
    spraying = 1
harvesting = st.radio("Did you incur any labor costs for Harvesting?:", ("Yes", "No"))
if harvesting == "Yes":
    harvesting = 1
rejuvenation = st.radio("Did you incur any labor costs for Rejuvenation?:", ("Yes", "No"))
if rejuvenation == "Yes":
    rejuvenation = 1
weeding = st.radio("Did you incur any labor costs for Weeding?:", ("Yes", "No"))
if weeding == "Yes":
    weeding = 1

if coffee_type == "Green Coffee Beans" or coffee_type == "Both":
    st.header("Post Production Cost:")
    hauling = st.radio("Did you incur any labor costs for Hauling?:", ("Yes", "No"))
    if hauling == "Yes":
        hauling = 1
    floating = st.radio("Did you incur any labor costs for Floating?:", ("Yes", "No"))
    if floating == "Yes":
        floating = 1
    depulping = st.radio("Did you incur any labor costs for Deulping?:", ("Yes", "No"))
    if depulping == "Yes":
        depulping = 1
    drying = st.radio("Did you incur any labor costs for Drying?:", ("Yes", "No"))
    if drying == "Yes":
        drying = 1
    dehulling = st.radio("Did you incur any labor costs for Dehulling?:", ("Yes", "No"))
    if dehulling == "Yes":
        dehulling = 1
    sorting = st.radio("Did you incur any labor costs for Sorting?:", ("Yes", "No"))
    if sorting == "Yes":
        sorting = 1
    storage = st.radio("Did you incur any labor costs for Storage?:", ("Yes", "No"))
    if storage == "Yes":
        storage = 1

st.header("Other Costs:")
transport = st.radio("Did you incur any labor costs for Transportation?:", ("Yes", "No"))
if transport == "Yes":
    transport = 1
other_cost = st.number_input(label="Enter the amount you spent for other costs: ", min_value=0.00, step=0.05)


def calculate():
    input_cost = (
        fertilizer1 * fertilizer1qty +
        fertilizer2 * fertilizer2qty +
        organic_fertilizer * organic_fertilizer_qty +
        herbicide * herbicide_qty +
        pesticide * pesticide_qty
    )
    lb_labor_cost = (
        (lb_pruning * pruning + lb_fertilizing * fertilizing +
        lb_spraying * spraying + lb_weeding * weeding +
        lb_harvesting * harvesting + lb_rejuvenation * rejuvenation) * coffee_trees
        )
    m_labor_cost = (
        (m_pruning * pruning + m_fertilizing * fertilizing +
        m_spraying * spraying + m_weeding * weeding +
        m_harvesting * harvesting + m_rejuvenation * rejuvenation) * coffee_trees
        )
    ub_labor_cost = (
        (ub_pruning * pruning + ub_fertilizing * fertilizing +
        ub_spraying * spraying + ub_weeding * weeding +
        ub_harvesting * harvesting + ub_rejuvenation * rejuvenation) * coffee_trees
        )
    lb_postproduction_cost = (
        (lb_hauling * hauling + lb_floating * floating +
        lb_depulping * depulping + lb_drying * drying +
        lb_dehulling * dehulling + lb_sorting * sorting +
        lb_storage * storage) * amount_gcb
        )
    m_postproduction_cost = (
        (m_hauling * hauling + m_floating * floating +
        m_depulping * depulping + m_drying * drying +
        m_dehulling * dehulling + m_sorting * sorting +
        m_storage * storage ) * amount_gcb
        )
    ub_postproduction_cost = (
        (ub_hauling * hauling + ub_floating * floating +
        ub_depulping * depulping + ub_drying * drying +
        ub_dehulling * dehulling + ub_sorting * sorting +
        ub_storage * storage ) * amount_gcb
        )
    
    total_lb_bound_cost = (
        input_cost + lb_labor_cost + lb_postproduction_cost + other_cost + (lb_transport * transport * amount_fc)
        )   
    total_m_bound_cost = (
        input_cost + m_labor_cost + m_labor_cost + other_cost + (m_transport * transport * amount_fc)
        )
    total_ub_bound_cost = (
        input_cost + ub_labor_cost + ub_labor_cost + other_cost + (ub_transport * transport * amount_fc)
        )
    

    return input_cost, lb_labor_cost, m_labor_cost, ub_labor_cost, lb_postproduction_cost , m_postproduction_cost, ub_postproduction_cost, total_lb_bound_cost, total_m_bound_cost, total_ub_bound_cost


if st.button("Calculate"):
    input_cost, lb_labor_cost, m_labor_cost, ub_labor_cost, lb_postproduction_cost , m_postproduction_cost, ub_postproduction_cost, total_lb_bound_cost, total_m_bound_cost, total_ub_bound_cost = calculate()
    st.write("Input Cost: ", input_cost)
    st.write("Lower Bound Labor Cost: ", lb_labor_cost)
    st.write("Median Labor Cost:", m_labor_cost)
    st.write("Upper Bound Labor Cost:", ub_labor_cost)

    if coffee_type == "Green Coffee Beans" or coffee_type == "Both":
        st.write("Lower Bound Post Production Cost:", lb_postproduction_cost)
        st.write("Median Post Production Cost:", m_postproduction_cost)
        st.write("Upper Bound Post Production Cost:", ub_postproduction_cost)

    st.write("Other Costs: ", other_cost)
    st.write("Total Lower Bound Cost: ", total_lb_bound_cost)
    st.write("Median Total Cost: ", total_m_bound_cost)
    st.write("Upper Bound Total Cost: ", total_ub_bound_cost)
