from django.shortcuts import render
from .forms import CalimsRaiseForm, CalimsProcessForm, CalimsSurveyorForm, CalimsDocumentForm, \
    CalimsPaymentsForm
# Create your views here.
from django.views.generic import (ListView)
from .models import XxgenClaims, XxgenClaimsProcessDtls, XxgenClaimsDocs, XxgenClaimsSurveyorDtls,\
    XxgenClaimsPayments
from django.forms import modelformset_factory


def CalimsRaiseView(request):
    context = {}

    ClaimForm = CalimsRaiseForm(request.POST or None)
    if request.method == "POST":
        if ClaimForm.is_valid():
            print(ClaimForm.cleaned_data)

            claim = ClaimForm.save(commit=False)
            print('policy no:', claim.policy_no)
            claim.created_by = str(request.user)
            claim.claim_status = 'SUBMITTED'
            claim.last_updated_by = str(request.user)
            claim.save()

            ClaimForm = CalimsRaiseForm()
    context['ClaimForm'] = ClaimForm

    return render(request, 'Claims/Claim_Raise.html', context)


