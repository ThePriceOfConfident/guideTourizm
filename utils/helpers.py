from tourizmConfig.models import CompanyInfo



def getCompanyInfo():
    return  CompanyInfo.objects.first()