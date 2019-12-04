from django.forms import modelformset_factory
from django.shortcuts import render
from django.views.generic import ListView

from .models import XxgenProductRiskMaster, Xxgen_agent_Prod_Comm_Master, XxgenClaimStatusMaster
from .forms import ProductsMasterForm, ProductRiskForm, AgentCommisionForm, AgentCreateForm, VehicleMasterForm, \
    VehicleDepriciatinoForm, XxgenNcbMasterForm, ClaimStatusMasterForm, ClaimsSurveyorMasterForm
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/MyAdmin/clogin/')
def ProductsMaster(request):
    Pform = ProductsMasterForm(request.POST or None)
    if Pform.is_valid():
        form = Pform.save(commit=False)
        form.created_by = str(request.user)
        form.last_updated_by = str(request.user)
        form.save()
        Pform = ProductsMasterForm()
    context = {'Pform': Pform}
    return render(request, 'Masters/ProductMaster.html', context)

@login_required(login_url='/MyAdmin/clogin/')
def ProductRisk(request):
    cformset = modelformset_factory(XxgenProductRiskMaster, form=ProductRiskForm, extra=4)
    formset = cformset(request.POST or None)

    if request.method == 'GET':
        search_id = request.GET.get('Sid')
        if request.GET.get('Sid') != "None" :
            try:
                formset = cformset(request.POST or None,
                                   queryset=XxgenProductRiskMaster.objects.filter(prod_code=search_id)
                                   )
            except XxgenProductRiskMaster.DoesNotExist:
                formset = cformset(queryset=XxgenProductRiskMaster.objects.none())

    if request.method == 'POST':
        if formset.is_valid():
            for form in formset.forms:
                if form['risk_code'].value() != '':
                    for name, field in form.fields.items():
                        tmpform = form.save(commit=False)
                        setattr(tmpform, 'created_by', str(request.user))
                        setattr(tmpform, 'last_updated_by', str(request.user))
                        tmpform.save()
            formset = cformset(queryset=XxgenProductRiskMaster.objects.none())

    context = {'formset':formset}
    return render(request, 'Masters/ProdRiskDetails.html', context)

@login_required(login_url='/MyAdmin/clogin/')
def createAgent(request):
    Aform = AgentCreateForm(request.POST or None)
    if Aform.is_valid():
        form = Aform.save(commit=False)
        form.created_by = str(request.user)
        form.last_updated_by = str(request.user)
        form.save()
        Aform = AgentCreateForm()
    context = {'Aform':Aform}
    return render(request, 'Masters/AgentCreate.html', context)

@login_required(login_url='/MyAdmin/clogin/')
def AgentCommision(request):
    cformset = modelformset_factory(Xxgen_agent_Prod_Comm_Master, form=AgentCommisionForm, extra=5)
    formset = cformset(request.POST or None)
    if request.method == 'GET':
        search_id = request.GET.get('prod_code')

        print('search_id', search_id)
        if request.GET.get('prod_code') != "None":
            try:
                formset = cformset(request.POST or None,
                                   queryset=Xxgen_agent_Prod_Comm_Master.objects.filter(agen_id=request.GET.get('prod_code'))
                                   )
            except XxgenProductRiskMaster.DoesNotExist:
                formset = cformset(queryset=Xxgen_agent_Prod_Comm_Master.objects.none())

    if formset.is_valid():
        for form in formset.forms:
            if form['agen_id'].value() != '':
                for name, field in form.fields.items():
                    tmpform = form.save(commit=False)
                    setattr(tmpform, 'created_by', str(request.user))
                    setattr(tmpform, 'last_updated_by', str(request.user))
                    tmpform.save()

    context = {'formset': formset}
    return render(request, 'Masters/AgentCommission.html', context)

@login_required(login_url='/MyAdmin/clogin/')
def VehicleMasterView(request):
    vform = VehicleMasterForm(request.POST or None)
    print('vform', vform)
    if vform.is_valid():
        form = vform.save(commit=False)
        form.created_by = str(request.user)
        form.last_updated_by = str(request.user)
        form.save()
        vform = VehicleMasterForm()
    context = {'vform': vform}
    print('vform',vform)
    return render(request, 'Masters/VehicleMaster.html', context)

@login_required(login_url='/MyAdmin/clogin/')
def VehicleDepriciationMasterView(request):
    vform = VehicleDepriciatinoForm(request.POST or None)
    print('vform', vform)
    if vform.is_valid():
        form = vform.save(commit=False)
        form.created_by = str(request.user)
        form.last_updated_by = str(request.user)
        form.save()
        vform = VehicleDepriciatinoForm()
    context = {'vform': vform}
    print('vform',vform)
    return render(request, 'Masters/VehicleDepriciation.html', context)


@login_required(login_url='/MyAdmin/clogin/')
def XxgenNcbMasterView(request):
    vform = XxgenNcbMasterForm(request.POST or None)
    print('vform', vform)
    if vform.is_valid():
        form = vform.save(commit=False)
        form.created_by = str(request.user)
        form.last_updated_by = str(request.user)
        form.save()
        vform = XxgenNcbMasterForm()
    context = {'vform': vform}
    return render(request, 'Masters/NCBMaster.html', context)

@login_required(login_url='/MyAdmin/clogin/')
def ClaimStatusMasterView(request):
    vform = ClaimStatusMasterForm(request.POST or None)
    if vform.is_valid():
        form = vform.save(commit=False)
        form.created_by = str(request.user)
        form.last_updated_by = str(request.user)
        form.save()
        vform = ClaimStatusMasterForm()
    context = {'vform': vform}
    return render(request, 'Masters/ClaimStatus.html', context)

@login_required(login_url='/MyAdmin/clogin/')
def ClaimsSurveyorMasterView(request):
    vform = ClaimsSurveyorMasterForm(request.POST or None)
    if vform.is_valid():
        form = vform.save(commit=False)
        form.created_by = str(request.user)
        form.last_updated_by = str(request.user)
        form.save()
        vform = ClaimsSurveyorMasterForm()
    context = {'vform': vform}
    print('vform', vform)
    return render(request, 'Masters/SurveyorMaster.html', context)


class ClaimStatusListView(ListView):
    template_name = 'Masters/XxgenClaimStatusMaster_list.html'
    queryset = XxgenClaimStatusMaster.objects.all()
