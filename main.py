import base64
import streamlit as st

st.set_page_config(page_title="VCLab Coffee Production Cost Calculator", layout='wide')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#@st.experimental_memo
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("coffee4.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img}");
    background-size: cover; /* This will cover the entire container without stretching */
    background-position: center center; /* Center the image horizontally and vertically */
    background-repeat: no-repeat; /* Prevent image from repeating */
    height: 100vh; /* Set the height to 100% of the viewport height (full height) */
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)


#st.subheader("Coffee Production Cost Calculator v8")
st.markdown("<h2 style='text-align: center'>Coffee Production Cost Calculator</h2>", unsafe_allow_html=True)
st.write("---")

transpo_postprod_yesno = 0
drying_postprod_yesno = 0
drying_postprod_yesno = 0
dehulling_postprod_yesno = 0
sorting_postprod_yesno = 0
depulping_postprod_yesno = 0


with st.expander("Coffee Farm General Information"):
	col1, col2, col3 = st.columns(3)
	with col1:
		hectares = st.number_input("Number of hectares:", min_value=0.00, step=1.0)
		bearing = st.number_input("Number of bearing trees:", min_value=0.00, step=10.00)
		non_bearing = st.number_input("Number of non-bearing:", min_value=0.00, step=10.00)
	
	trees = bearing + non_bearing
	tree_perhectare = trees/hectares if hectares > 0 else 0

	with col2:
		st.write("Select the type of Coffee you will sell:")
		cb1 = st.checkbox("Fresh Cherries")
		cb2 = st.checkbox("Dried Coffee Beans")
		cb3 = st.checkbox("Green Coffee Beans")
		coffee_types = []
		if cb1: coffee_types.append("Fresh Cherries")
		if cb2: coffee_types.append("Dried Coffee Beans")
		if cb3: coffee_types.append("Green Coffee Beans")

	with col3:
		dataset = st.radio("Please select the dataset to use for the computation:", ("General - Robusta", "General - Arabica", "General - Excelsa", "Mahintana - Robusta", "Tagbina - Robusta"))

if dataset == "General - Robusta":
    lb_transport = 0.5
    lb_drying = 0.33
    lb_dehulling = 0.67
    lb_sorting = 0.24
    lb_depulping = 0.9

    lb_hauling = 0.27
    lb_pruning = 0.9
    lb_fertilizing = 0.75
    lb_weeding = 1.2
    lb_spraying = 0.39
    lb_rejuvenation = 0.08
    lb_harvesting = 1.5

    m_transport = 1.00
    m_drying = 0.69
    m_dehulling = 1.29
    m_sorting = 0.65
    m_depulping = 1.68

    m_hauling = 0.60
    m_pruning = 1.60
    m_fertilizing = 1.95
    m_weeding = 2.14
    m_spraying = 0.60
    m_rejuvenation = 0.23
    m_harvesting = 3.20

    ub_transport = 2.0
    ub_drying = 1.4
    ub_dehulling = 1.75
    ub_sorting = 1.3
    ub_depulping = 4.5

    ub_hauling = 1.0
    ub_pruning = 3.0
    ub_fertilizing = 5.33
    ub_weeding = 4.29
    ub_spraying = 2.0
    ub_rejuvenation = 1.13
    ub_harvesting = 6.0

elif dataset == "General - Arabica":
    lb_transport = 0.27
    lb_drying = 0.73
    lb_dehulling = 0.48
    lb_sorting = 0.20
    lb_depulping = 0.19

    lb_hauling = 0.47
    lb_pruning = 0.67
    lb_fertilizing = 0.5
    lb_weeding = 0.66
    lb_spraying = 0.36
    lb_rejuvenation = 0.14
    lb_harvesting = 1.67

    m_transport = 0.50
    m_drying = 1.43
    m_dehulling = 0.78
    m_sorting = 2.24
    m_depulping = 0.38

    m_hauling = 1.25
    m_pruning = 1.50
    m_fertilizing = 0.71
    m_weeding = 1.67
    m_spraying = 0.84
    m_rejuvenation = 0.55
    m_harvesting = 3.49

    ub_transport = 0.97
    ub_drying = 2.41
    ub_dehulling = 1.29
    ub_sorting = 4.34
    ub_depulping = 2.14

    ub_hauling = 2.10
    ub_pruning = 3.0
    ub_fertilizing = 1.43
    ub_weeding = 3.33
    ub_spraying = 1.31
    ub_rejuvenation = 1.5
    ub_harvesting = 6.80

elif dataset == "General - Excelsa":
    lb_transport = 0.67
    lb_drying = 1.2
    lb_dehulling = 0.98
    lb_sorting = 4.28
    lb_depulping = 0.33

    lb_hauling = 0.83
    lb_pruning = 0.75
    lb_fertilizing = 0.9
    lb_weeding = 1.44
    lb_spraying = 0.67
    lb_rejuvenation = 0.46
    lb_harvesting = 2.68

    m_transport = 1.25
    m_drying = 2.50
    m_dehulling = 1.94
    m_sorting = 4.28
    m_depulping = 2.08

    m_hauling = 1.33
    m_pruning = 1.34
    m_fertilizing = 2.52
    m_weeding = 3.00
    m_spraying = 1.50
    m_rejuvenation = 0.75
    m_harvesting = 7.05

    ub_transport = 2.12
    ub_drying = 5.09
    ub_dehulling = 4.0
    ub_sorting = 4.53
    ub_depulping = 4.23

    ub_hauling = 3.75
    ub_pruning = 2.9
    ub_fertilizing = 8
    ub_weeding = 9.53
    ub_spraying = 3
    ub_rejuvenation = 1.5
    ub_harvesting = 12

elif dataset == "Mahintana - Robusta":
    lb_transport = 0.56
    lb_drying = 0.375
    lb_dehulling = 0.8
    lb_sorting = 0.00
    lb_depulping = 0.00

    lb_hauling = 0.00
    lb_pruning = 1.00
    lb_fertilizing = 1.00
    lb_weeding = 1.23
    lb_spraying = 0.00
    lb_rejuvenation = 0.00
    lb_harvesting = 1.78

    m_transport = 1.11
    m_drying = 0.67
    m_dehulling = 1.34
    m_sorting = 0.00
    m_depulping = 0.00

    m_hauling = 0.00
    m_pruning = 1.67
    m_fertilizing = 2.4
    m_weeding = 2.27
    m_spraying = 0.00
    m_rejuvenation = 0.00
    m_harvesting = 3.5

    ub_transport = 2.00
    ub_drying = 1.25
    ub_dehulling = 1.71
    ub_sorting = 0.00
    ub_depulping = 0.00

    ub_hauling = 0.00
    ub_pruning = 3.00
    ub_fertilizing = 6.23
    ub_weeding = 4.52
    ub_spraying = 0.00
    ub_rejuvenation = 0.00
    ub_harvesting =6.00
	
elif dataset == "Tagbina - Robusta":
    lb_transport = 0.05
    lb_drying = 0.06
    lb_dehulling = 0.16
    lb_sorting = 0.14
    lb_depulping = 0.00

    lb_hauling = 0.00
    lb_pruning = 0.8
    lb_fertilizing = 0.19
    lb_weeding = 1.00
    lb_spraying = 0.34
    lb_rejuvenation = 0.00
    lb_harvesting = 1.00

    m_transport = 0.10
    m_drying = 1.00
    m_dehulling = 0.32
    m_sorting = 0.34
    m_depulping = 0.00

    m_hauling = 0.00
    m_pruning = 1.25
    m_fertilizing = 0.25
    m_weeding = 1.60
    m_spraying = 0.60
    m_rejuvenation = 0.00
    m_harvesting = 1.60

    ub_transport = 0.10
    ub_drying = 1.00
    ub_dehulling = 0.32
    ub_sorting = 0.34
    ub_depulping = 0.00

    ub_hauling = 0.00
    ub_pruning = 1.25
    ub_fertilizing = 0.25
    ub_weeding = 1.60
    ub_spraying = 0.60
    ub_rejuvenation = 0.00
    ub_harvesting = 1.60


maincol1, maincol2 = st.columns(2)
with maincol1:
	st.subheader("Farm Production Costs")
	tab1, tab2, tab3, tab4 = st.tabs(["Supply Costs", "Labor Costs", "Post Production Costs", "Other Cost"])
	
	with tab1:
		#st.subheader("FERTILIZERS")
		fert_cost = 0
		fert_apply = st.radio("Will you apply fertilizers?", ("Yes", "No"))
		if fert_apply == "Yes":
			fert_application = st.radio("To which coffee trees will you apply fertilizers?", ("Bearing", "Non-bearing", "Both"))
			if fert_application == "Bearing":
				fert_percent = st.number_input("Percent of bearing trees to be applied with fertilizers?", min_value=0.00, max_value = 100.00, step=10.00)
				fert_kg = st.number_input("How many kilograms of fertilizers will be used for the bearing trees?", min_value=0.00, step=10.00)
				fert_costperkg = st.number_input("Cost per kilogram of fertilizers?", min_value=0.00, step=10.00)
				fert_cost = (fert_kg * fert_costperkg) / ((fert_percent/100) * (bearing/hectares)) if bearing and hectares and fert_percent > 0 else 0
			elif fert_application == "Non-bearing":
				fert_percent = st.number_input("Percent of non bearing trees to be applied with fertilizers?", min_value=0.00, max_value = 100.00, step=10.00)
				fert_kg = st.number_input("How many kilograms of fertilizers will be used for the non bearing trees?", min_value=0.00, step=10.00)
				fert_costperkg = st.number_input("Cost per kilogram of fertilizers?", min_value=0.00, step=10.00)
				fert_cost = (fert_kg * fert_costperkg) / ((fert_percent/100) * (non_bearing/hectares)) if non_bearing and hectares and fert_percent > 0 else 0
			elif fert_application == "Both":
				fert_percent = st.number_input("Percent of total trees to be applied with fertilizers?", min_value=0.00, max_value = 100.00, step=10.00) 
				fert_kg = st.number_input("How many kilograms of fertilizers will be used?", min_value=0.00, step=10.00)
				fert_costperkg = st.number_input("Cost per kilogram of fertilizers?", min_value=0.00, step=10.00)
				fert_cost = (fert_kg * fert_costperkg) / ((fert_percent/100)* tree_perhectare) if tree_perhectare and fert_percent > 0 else 0
		
		st.write("---")
		#st.subheader("HERBICIDES")
		herb_cost = 0
		herb_apply = st.radio("Will you apply herbicides?", ("Yes", "No"))
		if herb_apply == "Yes":
			herb_application = st.radio("To which coffee trees will you apply herbicides?", ("Bearing", "Non-bearing", "Both"))
			if herb_application == "Bearing":
				herb_percent = st.number_input("Percent of bearing trees to be applied with herbicides?", min_value=0.00, max_value = 100.00, step=10.00)
				herb_kg = st.number_input("How many kilograms of herbicides will be used for the bearing trees?", min_value=0.00, step=10.00)
				herb_costperkg = st.number_input("Cost per kilogram of herbicides?", min_value=0.00, step=10.00)
				herb_cost = (herb_kg * herb_costperkg) / ((herb_percent/100) * (bearing/hectares)) if bearing and hectares and herb_percent > 0 else 0
			elif herb_application == "Non-bearing":
				herb_percent = st.number_input("Percent of non bearing trees to be applied with herbicides?", min_value=0.00, max_value = 100.00, step=10.00)
				herb_kg = st.number_input("How many kilograms of herbicides will be used for the non bearing trees?", min_value=0.00, step=10.00)
				herb_costperkg = st.number_input("Cost per kilogram of herbicides?", min_value=0.00, step=10.00)
				herb_cost = (herb_kg * herb_costperkg) / ((herb_percent/100) * (non_bearing/hectares)) if non_bearing and hectares and herb_percent > 0 else 0
			elif herb_application == "Both":
				herb_percent = st.number_input("Percent of total trees to be applied with herbicides?", min_value=0.00, max_value = 100.00, step=10.00)
				herb_kg = st.number_input("How many kilograms of herbicides will be used?", min_value=0.00, step=10.00)
				herb_costperkg = st.number_input("Cost per kilogram of herbicides?", min_value=0.00, step=10.00)
				herb_cost = (herb_kg * herb_costperkg) / ((herb_percent/100) * tree_perhectare) if tree_perhectare and herb_percent > 0 else 0

		st.write("---")
		#st.subheader("PESTICIDES")
		pest_code = 0
		pest_apply = st.radio("Will you apply pesticides?", ("Yes", "No"))
		if pest_apply == "Yes":
			pest_application = st.radio("To which coffee trees will you apply pesticides?", ("Bearing", "Non-bearing", "Both"))
			if pest_application == "Bearing":
				pest_percent = st.number_input("Percent of bearing trees to be applied with pesticides?", min_value=0.00, max_value = 100.00, step=10.00)
				pest_kg = st.number_input("How many kilograms of pesticides will be used for the bearing trees?", min_value=0.00, step=10.00)
				pest_costperkg = st.number_input("Cost per kilogram of pesticides?", min_value=0.00, step=10.00)
				pest_cost = (pest_kg * pest_costperkg) / ((pest_percent/100) * (bearing/hectares)) if bearing and hectares and pest_percent > 0 else 0
			elif pest_application == "Non-bearing":
				pest_percent = st.number_input("Percent of non bearing trees to be applied with pesticides?", min_value=0.00, max_value = 100.00, step=10.00)
				pest_kg = st.number_input("How many kilograms of pesticides will be used for the non bearing trees?", min_value=0.00, step=10.00)
				pest_costperkg = st.number_input("Cost per kilogram of pesticides?", min_value=0.00, step=10.00)
				pest_cost = (pest_kg * pest_costperkg) / ((pest_percent/100) * (non_bearing/hectares)) if non_bearing and hectares and pest_percent > 0 else 0
			elif pest_application == "Both":
				pest_percent = st.number_input("Percent of total trees to be applied with pesticides?", min_value=0.00, max_value = 100.00, step=10.00)
				pest_kg = st.number_input("How many kilograms of pesticides will be used?", min_value=0.00, step=10.00)
				pest_costperkg = st.number_input("Cost per kilogram of pesticides?", min_value=0.00, step=10.00)
				pest_cost = (pest_kg * pest_costperkg) / ((pest_percent/100) * tree_perhectare) if tree_perhectare and pest_percent > 0 else 0
	
	with tab2:
		#st.subheader("Labor Cost - Harvesting")
		harvesting_labor_percent = 0
		hauling_labor_percent = 0
		pruning_labor_percent_bearing = 0
		pruning_labor_percent_nonbearing = 0
		fertilizer_labor_percent_bearing = 0
		fertilizer_labor_percent_nonbearing = 0
		weeding_labor_percent_bearing = 0
		weeding_labor_percent_nonbearing = 0
		spraying_labor_percent_bearing = 0
		spraying_labor_percent_nonbearing = 0
		rejuvenation_labor_percent_bearing = 0
		rejuvenation_labor_percent_nonbearing = 0

		harvesting_labor_yesno = st.radio("Did you incur any labor costs for Harvesting?:", ("Yes", "No"))
		if harvesting_labor_yesno == "Yes":
			harvesting_labor_yesno = 1
			harvesting_labor_percent = st.number_input("Percent of bearing trees that you will be harvesting?", min_value=0.00, max_value = 100.00, step=10.00)
		elif harvesting_labor_yesno == "No":
			harvesting_labor_yesno = 0
		
		st.write("---")
		#st.subheader("Labor Cost - Hauling")
		hauling_labor_yesno = st.radio("Did you incur any labor costs for Hauling?:", ("Yes", "No"))
		if hauling_labor_yesno == "Yes":
			hauling_labor_yesno = 1
			hauling_labor_percent = st.number_input("Percent of bearing trees that you will be Hauling?", min_value=0.00, max_value = 100.00, step=10.00)
		elif hauling_labor_yesno == "No":
			hauling_labor_yesno = 0
		
		st.write("---")
		#st.subheader("Labor Cost - Pruning")
		pruning_labor_yesno = st.radio("Did you incur any labor costs for Pruning?:", ("Yes", "No"))
		if pruning_labor_yesno == "Yes":
			pruning_labor_yesno = 1
			pruning_labor_percent_bearing = st.number_input("Percent of bearing trees to be applied with Pruning?", min_value=0.00, max_value = 100.00, step=10.00)
			pruning_labor_percent_nonbearing = st.number_input("Percent of non-bearing trees to be applied with Pruning?", min_value=0.00, max_value = 100.00, step=10.00)
		elif pruning_labor_yesno == "No":
			pruning_labor_yesno = 0

		st.write("---")
		#st.subheader("Labor Cost - Fertilizing")
		fertilizer_labor_yesno = st.radio("Did you incur any labor costs for Fertilizing?:", ("Yes", "No"))
		if fertilizer_labor_yesno == "Yes":
			fertilizer_labor_yesno = 1
			fertilizer_labor_percent_bearing = st.number_input("Percent of bearing trees to be applied with Fertilizing labor?", min_value=0.00, max_value = 100.00, step=10.00)
			fertilizer_labor_percent_nonbearing = st.number_input("Percent of non-bearing trees to be applied with Fertilizing labor?", min_value=0.00, max_value = 100.00, step=10.00)
		elif fertilizer_labor_yesno == "No":
			fertilizer_labor_yesno = 0

		st.write("---")
		#st.subheader("Labor Cost - Weeding")
		weeding_labor_yesno = st.radio("Did you incur any labor costs for Weeding?:", ("Yes", "No"))
		if weeding_labor_yesno == "Yes":
			weeding_labor_yesno = 1
			weeding_labor_percent_bearing = st.number_input("Percent of bearing trees to be applied with weeding?", min_value=0.00, max_value = 100.00, step=10.00)
			weeding_labor_percent_nonbearing = st.number_input("Percent of non-bearing trees to be applied with weeding?", min_value=0.00, max_value = 100.00, step=10.00)
		elif weeding_labor_yesno == "No":
			weeding_labor_yesno = 0

		st.write("---")
		#st.subheader("Labor Cost - Spraying")
		spraying_labor_yesno = st.radio("Did you incur any labor costs for Spraying?:", ("Yes", "No"))
		if spraying_labor_yesno == "Yes":
			spraying_labor_yesno = 1
			spraying_labor_percent_bearing = st.number_input("Percent of bearing trees to be applied with spraying?", min_value=0.00, max_value = 100.00, step=10.00)
			spraying_labor_percent_nonbearing = st.number_input("Percent of non bearing trees to be applied with spraying?", min_value=0.00, max_value = 100.00, step=10.00)
		elif spraying_labor_yesno == "No":
			spraying_labor_yesno = 0

		st.write("---")
		#st.subheader("Labor Cost - Rejuvenation")
		rejuvenation_labor_yesno = st.radio("Did you incur any labor costs for Rejuvenation?:", ("Yes", "No"))
		if rejuvenation_labor_yesno == "Yes":
			rejuvenation_labor_yesno = 1
			rejuvenation_labor_percent_bearing = st.number_input("Percent of bearing trees to be applied with rejuvenation?", min_value=0.00, max_value = 100.00, step=10.00)
			rejuvenation_labor_percent_nonbearing = st.number_input("Percent of non bearing trees to be applied with rejuvenation?", min_value=0.00, max_value = 100.00, step=10.00)
		elif rejuvenation_labor_yesno == "No":
			rejuvenation_labor_yesno = 0
    
	with tab3:
		transpo_postprod_yesno = st.radio("Did you incur any costs for Transportation?:", ("Yes", "No"))
		if transpo_postprod_yesno == "Yes":
			transpo_postprod_yesno = 1
		elif transpo_postprod_yesno == "No":
			transpo_postprod_yesno = 0
		
		if "Dried Coffee Beans" in coffee_types: #coffee_type == "Dried Coffee Beans" or coffee_type == "Fresh and Dried Coffee Beans":
			drying_postprod_yesno = st.radio("Did you incur any costs for Drying:", ("Yes", "No"))
			if drying_postprod_yesno == "Yes":
				drying_postprod_yesno = 1
			elif drying_postprod_yesno == "No":
				drying_postprod_yesno = 0
        
		if "Green Coffee Beans" in coffee_types: #"coffee_type == "Green Coffee Beans" or coffee_type == "Fresh and Green Coffee Beans" or coffee_type == "Dried and Green Coffee Beans" or coffee_type == "All":
			dehulling_postprod_yesno = st.radio("Did you incur any costs for Dehulling:", ("Yes", "No"))
			if dehulling_postprod_yesno == "Yes":
				dehulling_postprod_yesno = 1
			elif dehulling_postprod_yesno == "No":
				dehulling_postprod_yesno = 0
			
			sorting_postprod_yesno = st.radio("Did you incur any costs for Sorting:", ("Yes", "No"))
			if sorting_postprod_yesno == "Yes":
				sorting_postprod_yesno = 1
			elif sorting_postprod_yesno == "No":
				sorting_postprod_yesno = 0
            
			depulping_postprod_yesno = st.radio("Did you incur any costs for Depulping:", ("Yes", "No"))
			if depulping_postprod_yesno == "Yes":
				depulping_postprod_yesno = 1
			elif depulping_postprod_yesno == "No":
				depulping_postprod_yesno = 0
    
	with tab4:
		other_cost = st.number_input(label="Enter total cost for unaccounted production items: ", min_value=0.00, step=10.00)
		other_cost_perhectare = (other_cost/hectares) if hectares > 0 else 0



def calculate():
    input_cost_perhectare = (fert_cost + herb_cost + pest_cost)
    lb_labor_cost = 0
    m_labor_cost = 0
    ub_labor_cost = 0
    lb_postproduction_cost = 0
    m_postproduction_cost = 0
    ub_postproduction_cost = 0
    total_lb_bound_cost = 0
    total_m_bound_cost = 0
    total_ub_bound_cost = 0
	
    lb_labor_cost = (
		lb_harvesting * harvesting_labor_yesno * ((harvesting_labor_percent/100) * (bearing/hectares)) +
		lb_hauling * hauling_labor_yesno * ((hauling_labor_percent/100) * (bearing/hectares)) +
		lb_pruning * pruning_labor_yesno * (((pruning_labor_percent_bearing/100) + (pruning_labor_percent_nonbearing/100)) * tree_perhectare) +
		lb_fertilizing * fertilizer_labor_yesno * (((fertilizer_labor_percent_bearing/100) + (fertilizer_labor_percent_nonbearing/100)) * tree_perhectare) +
		lb_weeding * weeding_labor_yesno * (((weeding_labor_percent_bearing/100) + (weeding_labor_percent_nonbearing/100)) * tree_perhectare) +
		lb_spraying * spraying_labor_yesno * (((spraying_labor_percent_bearing/100) + (spraying_labor_percent_nonbearing/100)) * tree_perhectare) +
		lb_rejuvenation * rejuvenation_labor_yesno * (((rejuvenation_labor_percent_bearing/100) + (rejuvenation_labor_percent_nonbearing/100)) * tree_perhectare)
    )if bearing and hectares > 0 else 0
	
    m_labor_cost = (
		m_harvesting * harvesting_labor_yesno * ((harvesting_labor_percent/100) * (bearing/hectares)) +
		m_hauling * hauling_labor_yesno * ((hauling_labor_percent/100) * (bearing/hectares)) +
		m_pruning * pruning_labor_yesno * (((pruning_labor_percent_bearing/100) + (pruning_labor_percent_nonbearing/100)) * tree_perhectare) +
		m_fertilizing * fertilizer_labor_yesno * (((fertilizer_labor_percent_bearing/100) + (fertilizer_labor_percent_nonbearing/100)) * tree_perhectare) +
		m_weeding * weeding_labor_yesno * (((weeding_labor_percent_bearing/100) + (weeding_labor_percent_nonbearing/100)) * tree_perhectare) +
		m_spraying * spraying_labor_yesno * (((spraying_labor_percent_bearing/100) + (spraying_labor_percent_nonbearing/100)) * tree_perhectare) +
		m_rejuvenation * rejuvenation_labor_yesno * (((rejuvenation_labor_percent_bearing/100) + (rejuvenation_labor_percent_nonbearing/100)) * tree_perhectare)
    )if bearing and hectares > 0 else 0
	
    ub_labor_cost = (
		ub_harvesting * harvesting_labor_yesno * ((harvesting_labor_percent/100) * (bearing/hectares)) +
		ub_hauling * hauling_labor_yesno * ((hauling_labor_percent/100) * (bearing/hectares)) +
		ub_pruning * pruning_labor_yesno * (((pruning_labor_percent_bearing/100) + (pruning_labor_percent_nonbearing/100)) * tree_perhectare) +
		ub_fertilizing * fertilizer_labor_yesno * (((fertilizer_labor_percent_bearing/100) + (fertilizer_labor_percent_nonbearing/100)) * tree_perhectare) +
		ub_weeding * weeding_labor_yesno * (((weeding_labor_percent_bearing/100) + (weeding_labor_percent_nonbearing/100)) * tree_perhectare) +
		ub_spraying * spraying_labor_yesno * (((spraying_labor_percent_bearing/100) + (spraying_labor_percent_nonbearing/100)) * tree_perhectare) +
		ub_rejuvenation * rejuvenation_labor_yesno * (((rejuvenation_labor_percent_bearing/100) + (rejuvenation_labor_percent_nonbearing/100)) * tree_perhectare)
    )if bearing and hectares > 0 else 0
	
    if "Fresh Cherries" in coffee_types and len(coffee_types) == 1: #coffee_type == "Fresh Cherries":
        lb_postproduction_cost = (
			lb_transport * tree_perhectare * transpo_postprod_yesno
        )
        m_postproduction_cost = (
			m_transport * tree_perhectare * transpo_postprod_yesno
        )
        ub_postproduction_cost = (
			ub_transport * tree_perhectare * transpo_postprod_yesno
        )
		
    elif "Dried Coffee Beans" in coffee_types and len(coffee_types) == 1 or "Dried Coffee Beans" in coffee_types and "Fresh Cherries" in coffee_types and len(coffee_types) == 2: #coffee_type == "Dried Coffee Beans" or "Fresh and Dried Coffee Beans":
        lb_postproduction_cost = (
			lb_transport * tree_perhectare * transpo_postprod_yesno +
			lb_drying * (bearing/hectares) * drying_postprod_yesno
        )if bearing and hectares > 0 else 0
		
        m_postproduction_cost = (
			m_transport * tree_perhectare * transpo_postprod_yesno +
			m_drying * (bearing/hectares) * drying_postprod_yesno
        )if bearing and hectares > 0 else 0
		
        ub_postproduction_cost = (
			ub_transport * tree_perhectare * transpo_postprod_yesno +
			ub_drying * (bearing/hectares) * drying_postprod_yesno
        )if bearing and hectares > 0 else 0
		
    elif "Green Coffee Beans" in coffee_types: #coffee_type == "Green Coffee Beans" or "Freshh and Green Coffee Beans" or "Dried and Green Coffee Beans" or "All":
        lb_postproduction_cost = (
			lb_transport * tree_perhectare * transpo_postprod_yesno +
			lb_drying * (bearing/hectares) * drying_postprod_yesno +
			lb_dehulling * (bearing/hectares) * dehulling_postprod_yesno +
			lb_sorting * (bearing/hectares) * sorting_postprod_yesno +
			lb_depulping * (bearing/hectares) * depulping_postprod_yesno
        )if bearing and hectares > 0 else 0
		
        m_postproduction_cost = (
			m_transport * tree_perhectare * transpo_postprod_yesno +
			m_drying * (bearing/hectares) * drying_postprod_yesno +
			m_dehulling * (bearing/hectares) * dehulling_postprod_yesno +
			m_sorting * (bearing/hectares) * sorting_postprod_yesno +
			m_depulping * (bearing/hectares) * depulping_postprod_yesno
        )if bearing and hectares > 0 else 0
		
        ub_postproduction_cost = (
			ub_transport * tree_perhectare * transpo_postprod_yesno +
			ub_drying * (bearing/hectares) * drying_postprod_yesno +
			ub_dehulling * (bearing/hectares) * dehulling_postprod_yesno +
			ub_sorting * (bearing/hectares) * sorting_postprod_yesno +
			ub_depulping * (bearing/hectares) * depulping_postprod_yesno
        )if bearing and hectares > 0 else 0
	
    total_lb_bound_cost = (
		input_cost_perhectare + lb_postproduction_cost + lb_labor_cost + other_cost_perhectare
    )
	
    total_m_bound_cost = (
		input_cost_perhectare + m_postproduction_cost + m_labor_cost + other_cost_perhectare
    )
	
    total_ub_bound_cost = (
		input_cost_perhectare + ub_postproduction_cost + ub_labor_cost + other_cost_perhectare
    )
	
    return input_cost_perhectare, lb_labor_cost, m_labor_cost, ub_labor_cost, lb_postproduction_cost, m_postproduction_cost, ub_postproduction_cost, total_lb_bound_cost, total_m_bound_cost, total_ub_bound_cost



with maincol2:
	if st.button("Compute Production Costs"):
		input_cost_perhectare, lb_labor_cost, m_labor_cost, ub_labor_cost, lb_postproduction_cost, m_postproduction_cost, ub_postproduction_cost, total_lb_bound_cost, total_m_bound_cost, total_ub_bound_cost = calculate()
		
		st.write("---")
		

		st.markdown(f"<h4>INPUT COST PER HECTARE: ₱{input_cost_perhectare:.2f}</h4>", unsafe_allow_html=True)
		st.write(f"\n")
		
		st.markdown(f"<h4>LABOR COST PER HECTARE: ₱{lb_labor_cost:.2f} to ₱{ub_labor_cost:.2f}</h4>", unsafe_allow_html=True)
		st.write(f"\n")
		
		st.markdown(f"<h4>POST PRODUCTION COST PER HECTARE: ₱{lb_postproduction_cost:.2f} to ₱{ub_postproduction_cost:.2f}</h4>", unsafe_allow_html=True)
		st.write(f"\n")

		st.markdown(f"<h4>OTHER COST PER HECTARE: ₱{other_cost_perhectare:.2f}</h4>", unsafe_allow_html=True)
		st.write(f"\n")
		
		st.markdown(f"<h4>OVERALL COST PER HECTARE: ₱{total_lb_bound_cost:.2f} to ₱{total_ub_bound_cost:.2f}</h4>", unsafe_allow_html=True)
