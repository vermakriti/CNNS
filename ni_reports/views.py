from django.http import response
from django.shortcuts import render,redirect
from ni_reports.models import AreaEn
from django.utils.datastructures import MultiValueDictKeyError
from django.db.models import Q

def factsheets(request):
    india=AreaEn.objects.values('area_id','area_name').filter(area_parent_id=-1)
    states=AreaEn.objects.values('area_id','area_name').filter(area_parent_id=1).filter(~Q(area_name="Andaman & Nicobar Islands")).filter(~Q(area_name="Chandigarh")).filter(~Q(area_name="Dadra and Nagar Haveli")).filter(~Q(area_name="Daman and Diu")).filter(~Q(area_name="Lakshadweep")).filter(~Q(area_name="Puducherry")).order_by('area_name')
    for i in range(len(states)):
        individual_name=states[i]['area_name'].split()
        str=''
        flag=True
        if len(individual_name)>1:
            for s in individual_name:
                if flag:
                    str+=s +'-'
                    flag=False
                else:
                    str+=s
                    flag=True
        else :
            str=individual_name[0]
        states[i]['area_id'] = '/static_files/factsheets/CNNS-v6-factsheet-' + str + '.pdf'
    for i in range(len(india)):
        india[i]['area_id']=  '/static_files/factsheets/CNNS-v6-factsheet-' + india[i]['area_name'] + '.pdf'
    return render(request,'factsheets.html',{'states':states,'india':india})


def nfhsfactsheets(request):
    states = {"AP" : "Andhra Pradesh","AR" : "Arunachal Pradesh", "AS" : "Assam","BR" : "Bihar","CT" : "Chhattisgarh","GA" : "Goa","GJ" : "Gujarat","HR" : "Haryana","HP" : "Himachal Pradesh","JH" : "Jharkhand", "KA" : "Karnataka","KL" : "Kerala", "MP" : "Madhya Pradesh","MH" : "Maharashtra","MN" : "Manipur", "ML" : "Meghalaya","MZ" : "Mizoram", "NL" : "Nagaland","OR" : "Odisha", "PB" : "Punjab", "RJ" : "Rajasthan","SK" : "Sikkim","TN" : "Tamil Nadu", "TL" : "Telangana","TR" : "Tripura","UP" : "Uttar Pradesh", "UT" : "Uttarakhand", "WB" : "West Bengal","AN" : "Andaman Nicobar Islands","DD" : "Dadra Nagar Haveli Daman Diu","DL" : "NCT Delhi","JK" : "Jammu Kashmir", "LH" : "Ladakh", "PY" : "Puducherry"}
    context = {'states': states}
    return render(request,'nfhsfactsheets.html',context)


def presentations(request):
    states=AreaEn.objects.values('area_id','area_name').filter(area_parent_id=1).filter(~Q(area_name="Andaman & Nicobar Islands")).filter(~Q(area_name="Chandigarh")).filter(~Q(area_name="Dadra and Nagar Haveli")).filter(~Q(area_name="Daman and Diu")).filter(~Q(area_name="Lakshadweep")).filter(~Q(area_name="Puducherry")).order_by('area_name')

    for i in range(len(states)):
        individual_name=states[i]['area_name'].split()
        str=''
        flag=True
        if len(individual_name)==2:
            for s in individual_name:
                if flag:
                    str+=s +'_'
                    flag=False
                else:
                    str+=s
        elif len(individual_name)==3:
            temp=2
            for s in individual_name:
                if temp:
                    str+=s +'_'
                    temp-=1
                    continue
                else:
                    str+=s
        else :
            str=individual_name[0]
        states[i]['area_id'] = '/static_files/presentations/CNNS_Presentations_' + str + '.pdf'
    return render(request,'presentations.html',{'states':states})    



def stateAndDistrict (request):

    selected_state_value='India'
    india=AreaEn.objects.values('area_id','area_name').filter(area_parent_id=-1)
    states=AreaEn.objects.values('area_id','area_name','area_id').filter(area_parent_id=1).order_by('area_name')

    for i in range(len(states)):
        states[i]['area_id'] = '/static_files/stateAndDistrict/NutritionInfo_' + str(states[i]['area_id'])+ '_' + states[i]['area_name'] + '.pdf'
    for i in range(len(india)):
        india[i]['area_id']= '/static_files/stateAndDistrict/NutritionInfo_' + str(india[i]['area_id'])+ '_' + india[i]['area_name'] + '.pdf'

    if request.method == 'POST':

        try:
            selected_state_value=request.POST['selected_state']
        except MultiValueDictKeyError:
           selected_state_value = ''

        if selected_state_value!='India':
            areaId=AreaEn.objects.values('area_id').filter(area_name=selected_state_value).first()
            id=areaId['area_id']
            district=AreaEn.objects.values('area_id','area_name').filter(area_parent_id=id).order_by('area_name')
            for i in range(len(district)):
                district[i]['area_id']= '/static_files/stateAndDistrict/NutritionInfo_' + str(district[i]['area_id'])+ '_' + district[i]['area_name'] + '.pdf'
            return render(request,'stateAndDistrict.html',{'states':states,'india':india,'district':district,'selected_state_value':selected_state_value})
        else :
            return render(request,'stateAndDistrict.html',{'states':states,'india':india,'selected_state_value':selected_state_value})
    else :
        return render(request,'stateAndDistrict.html',{'states':states,'india':india,'selected_state_value':selected_state_value})
