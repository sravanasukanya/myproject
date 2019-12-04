from django.urls import path
from .views import ProductsMaster, ProductRisk, AgentCommision, createAgent, VehicleMasterView, \
    VehicleDepriciationMasterView, XxgenNcbMasterView, ClaimStatusMasterView, ClaimsSurveyorMasterView, \
    ClaimStatusListView

app_name = 'Masters'

urlpatterns = [
     path('ProductsMaster/', ProductsMaster, name='ProductsMaster'),
     path('ProductRisk/', ProductRisk, name='ProductRisk'),
     path('createAgent/', createAgent, name='createAgent'),
     path('AgentCommission/', AgentCommision, name='AgentCommission'),
     path('VehicleMaster/', VehicleMasterView, name='VehicleMaster'),
     path('VehicleDepreciation/', VehicleDepriciationMasterView, name='VehicleDepreciation'),
     path('NCBMaster/', XxgenNcbMasterView, name="NCBMaster"),
     path('Claimstatus/', ClaimStatusMasterView, name="Claimstatus"),
     path('Surveyormaster/', ClaimsSurveyorMasterView, name="Surveyormaster"),
     path('Claimslist/', ClaimStatusListView, name="ClaimStatusListView"),
    ]