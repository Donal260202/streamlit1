import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="PMFBY ANALYSIS",layout="wide")
df=pd.read_excel("C:\\Users\\dell\\Desktop\\PMFBY.xlsx")

def header_page():
    st.markdown("<h1 style='text-align: center; color: black;'>Analysis of PMFBY Data 2018-2023</h1>", unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center; color: grey;'>By: Ashwin Chaudhari</h2>", unsafe_allow_html=True)
    
    st.markdown("<h3 style='text-align: center; color: grey;'>Data Science Intern</h3>", unsafe_allow_html=True)



def Year_Wise_Analysis():
    st.title("Year Wise Analysis of PMFBY Data 2018-2023")
    
    
    st.sidebar.header("Please Select the District:")
    district=st.sidebar.multiselect("Select the district:",options=df["District Name"].unique(),default=df["District Name"].unique())
    
    
    df_selection=df[(df["District Name"].isin(district))]
    
    
    
    xyz=df_selection[["Year","Total Applications"]]
    fig1=px.bar(xyz,x="Year",y="Total Applications",title="<b>Total Application per Year<b>",text_auto=True)
    fig1.update_traces(marker_color='green')
    fig1.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="lightsteelblue",paper_bgcolor="lightsteelblue")
    st.plotly_chart(fig1)
    xyz.reset_index(drop=True,inplace=True)
    st.dataframe(xyz)

    x_farmers=df_selection[["Year","Farmers"]]
    fig2=px.bar(x_farmers,x="Year",y="Farmers",title="<b>Total Farmers per Year<b>",text_auto=True)
    fig2.update_traces(marker_color='purple')
    fig2.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="lightsalmon",paper_bgcolor="lightsalmon")

    st.plotly_chart(fig2)
    x_farmers.reset_index(drop=True,inplace=True)
    st.dataframe(x_farmers)



    x_fa=df_selection[["Year","Farmers","Total Applications"]]
    x_fa_melted=x_fa.melt(id_vars=["Year"],value_vars=["Farmers","Total Applications"],var_name='Category',value_name="Farmers and Applications")
    fig3=px.bar(x_fa_melted,x="Year",y="Farmers and Applications",color='Category',title="<b>Total Farmers And Applications per Year<b>",barmode='group',text_auto=True,color_discrete_map={"Farmers":"#ec7c34","Total Applications":"darkslateblue"})
    fig3.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="lightskyblue",paper_bgcolor="lightskyblue")
    st.plotly_chart(fig3)
    x_fa.reset_index(drop=True,inplace=True)
    st.dataframe(x_fa)


    x_pr=df_selection[["Year","GP/Sum Insured"]]
    x_pr["GP/Sum Insured"]=(x_pr["GP/Sum Insured"].round(2))*100
    fig4 = px.line(x_pr, x="Year", y="GP/Sum Insured",title="<b>Average Premium rate per Year<b>", text="GP/Sum Insured")
    fig4.update_traces(textposition="bottom center")
    fig4.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="lightyellow",paper_bgcolor="lightyellow")
    st.plotly_chart(fig4)
    x_pr.reset_index(drop=True,inplace=True)
    st.dataframe(x_pr)

    x_cap=df_selection[["Year","Claim Against Premium"]]
    x_cap["Claim Against Premium"]=(x_cap["Claim Against Premium"].round(2))*100
    fig5 = px.line(x_cap, x="Year", y="Claim Against Premium",title="<b>Claim Against Premium per Year<b>", text="Claim Against Premium")
    fig5.update_traces(textposition="top center")
    fig5.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="lightyellow",paper_bgcolor="lightyellow")
    st.plotly_chart(fig5)
    x_cap.reset_index(drop=True,inplace=True)
    st.dataframe(x_cap)

    x_area=df_selection[["Year","Area Insured"]]
    fig6=px.bar(x_area,x="Year",y="Area Insured",title="<b>Area Insured per Year<b>",text_auto=True)
    fig6.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="whitesmoke",paper_bgcolor="whitesmoke")
    st.plotly_chart(fig6)
    x_area.reset_index(drop=True,inplace=True)
    st.dataframe(x_area)

    x_sum=df_selection[["Year","Sum Insured (In Lac.)"]]
    fig7=px.bar(x_sum,x="Year",y="Sum Insured (In Lac.)",title="<b>Sum Insured (In Lac.) per Year<b>",text_auto=True)
    fig7.update_traces(marker_color='red')
    fig7.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="lightgoldenrodyellow",paper_bgcolor="lightgoldenrodyellow")
    st.plotly_chart(fig7)
    x_sum.reset_index(drop=True,inplace=True)
    st.dataframe(x_sum)

    x_gross=df_selection[["Year","Gross Premium"]]
    fig8=px.bar(x_gross,x="Year",y="Gross Premium",title="<b>Gross Premium per Year<b>",text_auto=True)
    fig8.update_traces(marker_color='brown')
    fig8.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="lightsteelblue",paper_bgcolor="lightsteelblue")
    st.plotly_chart(fig8)
    x_gross.reset_index(drop=True,inplace=True)
    st.dataframe(x_gross)


    x_gs=df_selection[["Year","Gross Premium","Sum Insured (In Lac.)"]]
    x_gs_melted=x_gs.melt(id_vars=["Year"],value_vars=["Gross Premium","Sum Insured (In Lac.)"],var_name='Category',value_name="Gross Premium and Sum Insured (In Lac.)")
    fig9=px.bar(x_gs_melted,x="Year",y="Gross Premium and Sum Insured (In Lac.)",color='Category',title="<b>Gross Premium And Sum Insured (In Lac.) per Year<b>",barmode='group',text_auto=True,color_discrete_map={"Gross Premium":"blue","Sum Insured (In Lac.)":"red"})
    fig9.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="lightgreen",paper_bgcolor="lightgreen")
    st.plotly_chart(fig9)
    x_gs.reset_index(drop=True,inplace=True)
    st.dataframe(x_gs)


    x_gt=df_selection[["Year","Gross Premium","Total Claim Paid"]]
    x_gt_melted=x_gt.melt(id_vars=["Year"],value_vars=["Gross Premium","Total Claim Paid"],var_name='Category',value_name="Gross Premium and Total Claim Paid")
    fig10=px.bar(x_gt_melted,x="Year",y="Gross Premium and Total Claim Paid",color='Category',title="<b>Gross Premium And Total Claim Paid (In Lac.) per Year<b>",barmode='group',text_auto=True,color_discrete_map={"Gross Premium":"green","Total Claim Paid":"yellow"})
    fig10.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="lightpink",paper_bgcolor="lightpink")
    st.plotly_chart(fig10)
    x_gt.reset_index(drop=True,inplace=True)
    st.dataframe(x_gt)

    x_ts=df_selection[["Year","Total Claim Paid","MT+L+PH"]]
    x_ts_melted=x_ts.melt(id_vars=["Year"],value_vars=["MT+L+PH","Total Claim Paid"],var_name='Category',value_name="Summation of Midterm,Localized,Post Harvest and Total Claim")
    fig11=px.bar(x_ts_melted,x="Year",y="Summation of Midterm,Localized,Post Harvest and Total Claim",color='Category',title="<b>Summation of Midterm,Localized,Post Harvest and Total Claim Paid (In Lac.) per Year<b>",barmode='group',text_auto=True,color_discrete_map={"Total Claim Paid":"olive","MT+L+PH":"purple"})
    fig11.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="aliceblue",paper_bgcolor="aliceblue")
    st.plotly_chart(fig11)
    x_ts.reset_index(drop=True,inplace=True)
    st.dataframe(x_ts)


    x_ty=df_selection[["Year","Total Claim Paid","Yield Based"]]
    x_ty_melted=x_ty.melt(id_vars=["Year"],value_vars=["Yield Based","Total Claim Paid"],var_name='Category',value_name="Yield Based and Total Claim Paid")
    fig12=px.bar(x_ty_melted,x="Year",y="Yield Based and Total Claim Paid",color='Category',title="<b>Yield Based and Total Claim Paid (In Lac.) per Year<b>",barmode='group',text_auto=True,color_discrete_map={"Total Claim Paid":"red","Yield Based":"yellow"})
    fig12.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="aqua",paper_bgcolor="aqua")
    st.plotly_chart(fig12)
    x_ty.reset_index(drop=True,inplace=True)
    st.dataframe(x_ty)


    x_ff=df_selection[["Year","Farmers","Total Farmer Benefit(Actual)"]]
    x_ff_melted=x_ff.melt(id_vars=["Year"],value_vars=["Total Farmer Benefit(Actual)","Farmers"],var_name='Category',value_name="Total Farmer Benefit and Farmers")
    fig13=px.bar(x_ff_melted,x="Year",y="Total Farmer Benefit and Farmers",color='Category',title="<b>Total Farmer Benefit and Farmers per Year<b>",barmode='group',text_auto=True,color_discrete_map={"Total Farmer Benefit(Actual)":"yellow","Farmers":"blue"})
    fig13.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="aquamarine",paper_bgcolor="aquamarine")
    st.plotly_chart(fig13)
    x_ff.reset_index(drop=True,inplace=True)
    st.dataframe(x_ff)

    xrevenue=df_selection[["Year","Revenue"]]
    fig14=px.bar(xrevenue,x="Year",y="Revenue",title="<b>Total Revenue per Year<b>",text_auto=True)
    fig14.update_traces(marker_color='green')
    fig14.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="blanchedalmond",paper_bgcolor="blanchedalmond")
    st.plotly_chart(fig14)
    xrevenue.reset_index(drop=True,inplace=True)
    st.dataframe(xrevenue)

    xprevented=df_selection[["Year","Prevented Sowing"]]
    fig15=px.bar(xprevented,x="Year",y="Prevented Sowing",title="<b>Total Prevented Sowing per Year<b>",text_auto=True)
    fig15.update_traces(marker_color='green')
    fig15.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="lightsteelblue",paper_bgcolor="lightsteelblue")
    st.plotly_chart(fig15)
    xprevented.reset_index(drop=True,inplace=True)
    st.dataframe(xprevented)

def District_Wise_Analysis():
    st.title(" District Wise Analysis of PMFBY Data 2018-2023")


    st.sidebar.header("Please Select the Year:")
    year=st.sidebar.multiselect("Select the Year:",options=df["Year"].unique(),default=df["Year"].unique())


    df_selection=df[(df["Year"].isin(year))]
    
    
    
    xyz=df_selection[["District Name","Total Applications"]]
    xyz.sort_values(by="Total Applications",ascending=False,inplace=True)
    fig1=px.bar(xyz,x="District Name",y="Total Applications",title="<b>Total Application per District<b>",text_auto=True)
    fig1.update_traces(marker_color='green')
    fig1.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="lightsteelblue",paper_bgcolor="lightsteelblue")
    st.plotly_chart(fig1)
    xyz.reset_index(drop=True,inplace=True)
    st.dataframe(xyz)

    x_farmers=df_selection[["District Name","Farmers"]]
    x_farmers.sort_values(by="Farmers",ascending=False,inplace=True)
    fig2=px.bar(x_farmers,x="District Name",y="Farmers",title="<b>Total Farmers per District<b>",text_auto=True)
    fig2.update_traces(marker_color='purple')
    fig2.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="lightsalmon",paper_bgcolor="lightsalmon")
    st.plotly_chart(fig2)
    x_farmers.reset_index(drop=True,inplace=True)
    st.dataframe(x_farmers)

    x_fa=df_selection[["District Name","Farmers","Total Applications"]]
    x_fa.sort_values(by="Total Applications",ascending=False,inplace=True)
    x_fa_melted=x_fa.melt(id_vars=["District Name"],value_vars=["Farmers","Total Applications"],var_name='Category',value_name="Farmers and Applications")
    fig3=px.bar(x_fa_melted,x="District Name",y="Farmers and Applications",color='Category',title="<b>Total Farmers And Applications per Year<b>",barmode='group',text_auto=True,color_discrete_map={"Farmers":"#ec7c34","Total Applications":"darkslateblue"})
    fig3.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="lightskyblue",paper_bgcolor="lightskyblue")
    st.plotly_chart(fig3)
    x_fa.reset_index(drop=True,inplace=True)
    st.dataframe(x_fa)


    x_pr=df_selection[["District Name","GP/Sum Insured"]]
    x_pr.sort_values(by="GP/Sum Insured",ascending=False,inplace=True)
    x_pr["GP/Sum Insured"]=(x_pr["GP/Sum Insured"].round(2))*100
    fig4 = px.line(x_pr, x="District Name", y="GP/Sum Insured",title="<b>Average Premium rate per District Name<b>", text="GP/Sum Insured")
    fig4.update_traces(textposition="bottom center")
    fig4.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="lightyellow",paper_bgcolor="lightyellow")
    st.plotly_chart(fig4)
    x_pr.reset_index(drop=True,inplace=True)
    st.dataframe(x_pr)

    x_cap=df_selection[["District Name","Claim Against Premium"]]
    x_cap.sort_values(by="Claim Against Premium",ascending=False,inplace=True)
    x_cap["Claim Against Premium"]=(x_cap["Claim Against Premium"].round(2))*100
    fig5 = px.line(x_cap, x="District Name", y="Claim Against Premium",title="<b>Claim Against Premium per District<b>", text="Claim Against Premium")
    fig5.update_traces(textposition="top center")
    fig5.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="lightyellow",paper_bgcolor="lightyellow")
    st.plotly_chart(fig5)
    x_cap.reset_index(drop=True,inplace=True)
    st.dataframe(x_cap)

    x_area=df_selection[["District Name","Area Insured"]]
    x_area.sort_values(by="Area Insured",ascending=False,inplace=True)
    fig6=px.bar(x_area,x="District Name",y="Area Insured",title="<b>Area Insured in Hectares per District<b>",text_auto=True)
    fig6.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="whitesmoke",paper_bgcolor="whitesmoke")
    st.plotly_chart(fig6)
    x_area.reset_index(drop=True,inplace=True)
    st.dataframe(x_area)

    x_sum=df_selection[["District Name","Sum Insured (In Lac.)"]]
    x_sum.sort_values(by="Sum Insured (In Lac.)",ascending=False,inplace=True)
    fig7=px.bar(x_sum,x="District Name",y="Sum Insured (In Lac.)",title="<b>Sum Insured (In Lac.) per District <b>",text_auto=True)
    fig7.update_traces(marker_color='red')
    fig7.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="lightgoldenrodyellow",paper_bgcolor="lightgoldenrodyellow")
    st.plotly_chart(fig7)
    x_sum.reset_index(drop=True,inplace=True)
    st.dataframe(x_sum)

    x_gross=df_selection[["District Name","Gross Premium"]]
    x_gross.sort_values(by="Gross Premium",ascending=False,inplace=True)
    fig8=px.bar(x_gross,x="District Name",y="Gross Premium",title="<b>Gross Premium (In Lac.) per District <b>",text_auto=True)
    fig8.update_traces(marker_color='brown')
    fig8.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="lightsteelblue",paper_bgcolor="lightsteelblue")
    st.plotly_chart(fig8)
    x_gross.reset_index(drop=True,inplace=True)
    st.dataframe(x_gross)

    x_gs=df_selection[["District Name","Gross Premium","Sum Insured (In Lac.)"]]
    x_gs.sort_values(by="Sum Insured (In Lac.)",ascending=False,inplace=True)
    x_gs_melted=x_gs.melt(id_vars=["District Name"],value_vars=["Gross Premium","Sum Insured (In Lac.)"],var_name='Category',value_name="Gross Premium and Sum Insured (In Lac.)")
    fig9=px.bar(x_gs_melted,x="District Name",y="Gross Premium and Sum Insured (In Lac.)",color='Category',title="<b>Gross Premium And Sum Insured (In Lac.) per District <b>",barmode='group',text_auto=True,color_discrete_map={"Gross Premium":"blue","Sum Insured (In Lac.)":"red"})
    fig9.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="lightgreen",paper_bgcolor="lightgreen")
    st.plotly_chart(fig9)
    x_gs.reset_index(drop=True,inplace=True)
    st.dataframe(x_gs)

    x_gt=df_selection[["District Name","Gross Premium","Total Claim Paid"]]
    x_gt.sort_values(by="Total Claim Paid",ascending=False,inplace=True)
    x_gt_melted=x_gt.melt(id_vars=["District Name"],value_vars=["Gross Premium","Total Claim Paid"],var_name='Category',value_name="Gross Premium and Total Claim Paid")
    fig10=px.bar(x_gt_melted,x="District Name",y="Gross Premium and Total Claim Paid",color='Category',title="<b>Gross Premium And Total Claim Paid (In Lac.) per District<b>",barmode='group',text_auto=True,color_discrete_map={"Gross Premium":"green","Total Claim Paid":"yellow"})
    fig10.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="lightpink",paper_bgcolor="lightpink")
    st.plotly_chart(fig10)
    x_gt.reset_index(drop=True,inplace=True)
    st.dataframe(x_gt)

    x_ts=df_selection[["District Name","Total Claim Paid","MT+L+PH"]]
    x_ts.sort_values(by="Total Claim Paid",ascending=False,inplace=True)
    x_ts_melted=x_ts.melt(id_vars=["District Name"],value_vars=["MT+L+PH","Total Claim Paid"],var_name='Category',value_name="Summation of Midterm,Localized,Post Harvest and Total Claim")
    fig11=px.bar(x_ts_melted,x="District Name",y="Summation of Midterm,Localized,Post Harvest and Total Claim",color='Category',title="<b>Summation of Midterm,Localized,Post Harvest and Total Claim (In Lac.) per District <b>",barmode='group',text_auto=True,color_discrete_map={"Total Claim Paid":"olive","MT+L+PH":"purple"})
    fig11.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="aliceblue",paper_bgcolor="aliceblue")
    st.plotly_chart(fig11)
    x_ts.reset_index(drop=True,inplace=True)
    st.dataframe(x_ts)


    x_ty=df_selection[["District Name","Total Claim Paid","Yield Based"]]
    x_ty.sort_values(by="Total Claim Paid",ascending=False,inplace=True)
    x_ty_melted=x_ty.melt(id_vars=["District Name"],value_vars=["Yield Based","Total Claim Paid"],var_name='Category',value_name="Yield Based and Total Claim Paid")
    fig12=px.bar(x_ty_melted,x="District Name",y="Yield Based and Total Claim Paid",color='Category',title="<b>Yield Based and Total Claim Paid (In Lac.) per District <b>",barmode='group',text_auto=True,color_discrete_map={"Total Claim Paid":"red","Yield Based":"yellow"})
    fig12.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="aqua",paper_bgcolor="aqua")
    st.plotly_chart(fig12)
    x_ty.reset_index(drop=True,inplace=True)
    st.dataframe(x_ty)


    x_ff=df_selection[["District Name","Farmers","Total Farmer Benefit(Actual)"]]
    x_ff.sort_values(by="Farmers",ascending=False,inplace=True)
    x_ff_melted=x_ff.melt(id_vars=["District Name"],value_vars=["Total Farmer Benefit(Actual)","Farmers"],var_name='Category',value_name="Total Farmer Benefit and Farmers")
    fig13=px.bar(x_ff_melted,x="District Name",y="Total Farmer Benefit and Farmers",color='Category',title="<b>Total Farmer Benefit and Farmers per District<b>",barmode='group',text_auto=True,color_discrete_map={"Total Farmer Benefit(Actual)":"yellow","Farmers":"blue"})
    fig13.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="aquamarine",paper_bgcolor="aquamarine")
    st.plotly_chart(fig13)
    x_ff.reset_index(drop=True,inplace=True)
    st.dataframe(x_ff)

    xrevenue=df_selection[["District Name","Revenue"]]
    xrevenue.sort_values(by="Revenue",ascending=False,inplace=True)
    fig14=px.bar(xrevenue,x="District Name",y="Revenue",title="<b>Total Revenue(in CR.) per District<b>",text_auto=True)
    fig14.update_traces(marker_color='green')
    fig14.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="blanchedalmond",paper_bgcolor="blanchedalmond")
    st.plotly_chart(fig14)
    xrevenue.reset_index(drop=True,inplace=True)
    st.dataframe(xrevenue)



    xprevented=df_selection[["District Name","Prevented Sowing"]]
    fig15=px.bar(xprevented,x="District Name",y="Prevented Sowing",title="<b>Total Prevented Sowing per District<b>",text_auto=True)
    fig15.update_traces(marker_color='green')
    fig15.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="lightsteelblue",paper_bgcolor="lightsteelblue")
    st.plotly_chart(fig15)
    xprevented.reset_index(drop=True,inplace=True)
    st.dataframe(xprevented)


page = st.sidebar.selectbox('Select Analysis',['header_page','Year_Wise_Analysis','District_Wise_Analysis']) 
if page == 'Year_Wise_Analysis':
    Year_Wise_Analysis()
elif page =='District_Wise_Analysis':
    District_Wise_Analysis()
else:
    header_page()
