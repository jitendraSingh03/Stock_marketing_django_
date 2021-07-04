from django.shortcuts import render
from .models import Country
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.fundamentaldata import FundamentalData
import requests
# 6KAD6UXEKNQF4QNR
# UYDC0513TXJRNHIJ
API_KEY='UYDC0513TXJRNHIJ'
fd=FundamentalData(key=API_KEY,output_format='pandas')
ts=TimeSeries(key=API_KEY,output_format='pandas')
    
# Create your views here.
def home(request):
    return render(request,'fullsite/newIndex.html')

def customSearch(request):
    companyOverview=fd.get_company_overview(request.GET['tiker'])
    tiker=ts.get_daily(request.GET['tiker']) # ye comment krunga
    
    annualIncome=fd.get_income_statement_annual(request.GET['tiker'])

    balanceSheet=fd.get_balance_sheet_annual(request.GET['tiker'])
    annualIncome=fd.get_income_statement_annual(request.GET['tiker'])
    # cashFlow=fd.get_cash_flow_annual(request.GET['tiker'])

    companyData=tiker[0].head(15).to_numpy()
    dataOfDate=tiker[0].head(15).index.copy()
    print(companyData)

    
   
    open =[]
    close=[]
    for i in companyData:
        open.append(i[int(request.GET['status'])])
        # close.append(i[int()])
    context ={ 
        'companyName':companyOverview[0].Name[0],
        'Currency':companyOverview[0].Currency[0],
        'Country':companyOverview[0].Country[0],
        'Sector':companyOverview[0].Sector[0],
        "year":balanceSheet[0].fiscalDateEnding.to_numpy()[0],
        "totalAssets":balanceSheet[0].totalAssets.to_numpy()[0],
        "inventory":balanceSheet[0].inventory.to_numpy()[0],
        "totalShareholderEquity":balanceSheet[0].totalShareholderEquity.to_numpy()[0],
        "fiscalDateEnding":annualIncome[0].fiscalDateEnding.to_numpy()[0],
        "totalRevenue":annualIncome[0].totalRevenue.to_numpy()[0],
        "grossProfit":annualIncome[0].grossProfit.to_numpy()[0],
        "netIncome":annualIncome[0].netIncome.to_numpy()[0],
        # "cashFlow":cashFlow[0].operatingCashflow.to_numpy()[0],
        'Symbol':tiker[1].get('2. Symbol'),
        'information':tiker[1].get('1. Information').split()[0],
        'lastRefreshed':tiker[1].get('3. Last Refreshed'),
        'open':open,
        'status':request.GET['status'],
        'open':open,
        'Date':dataOfDate,
        'close':close,
        'graph':request.GET['graph']
    }
    return render(request,'fullsite/newIndex.html' ,context)


def intraday(request):
    companyOverview=fd.get_company_overview(request.GET['tiker'])
    tiker=ts.get_intraday(request.GET['tiker']) # ye comment krunga
    
    annualIncome=fd.get_income_statement_annual(request.GET['tiker'])

    balanceSheet=fd.get_balance_sheet_annual(request.GET['tiker'])
    annualIncome=fd.get_income_statement_annual(request.GET['tiker'])
    # cashFlow=fd.get_cash_flow_annual(request.GET['tiker'])

    companyData=tiker[0].head(20).to_numpy()
    dataOfDate=tiker[0].head(20).index.copy()
    print(companyData)   
    open =[]
    # close=[]
    for i in companyData:
        open.append(i[int(request.GET['status'])])
        # close.append(i[int()])
    context ={ 
        'companyName':companyOverview[0].Name[0],
        'Currency':companyOverview[0].Currency[0],
        'Country':companyOverview[0].Country[0],
        'Sector':companyOverview[0].Sector[0],
        "year":balanceSheet[0].fiscalDateEnding.to_numpy()[0],
        "totalAssets":balanceSheet[0].totalAssets.to_numpy()[0],
        "inventory":balanceSheet[0].inventory.to_numpy()[0],
        "totalShareholderEquity":balanceSheet[0].totalShareholderEquity.to_numpy()[0],
        "fiscalDateEnding":annualIncome[0].fiscalDateEnding.to_numpy()[0],
        "totalRevenue":annualIncome[0].totalRevenue.to_numpy()[0],
        "grossProfit":annualIncome[0].grossProfit.to_numpy()[0],
        "netIncome":annualIncome[0].netIncome.to_numpy()[0],
        # "cashFlow":cashFlow[0].operatingCashflow.to_numpy()[0],
        'Symbol':tiker[1].get('2. Symbol'),
        'information':tiker[1].get('1. Information').split()[0],
        'lastRefreshed':tiker[1].get('3. Last Refreshed'),
        'open':open,
        'status':request.GET['status'],
        'open':open,
        'Date':dataOfDate,
        'graph':request.GET['graph']
    }
    return render(request,'fullsite/newIndex.html' ,context)

def daily(request):
    companyOverview=fd.get_company_overview(request.GET['tiker'])
    tiker=ts.get_daily(request.GET['tiker']) # ye comment krunga
    annualIncome=fd.get_income_statement_annual(request.GET['tiker'])
    balanceSheet=fd.get_balance_sheet_annual(request.GET['tiker'])
    annualIncome=fd.get_income_statement_annual(request.GET['tiker'])
    # cashFlow=fd.get_cash_flow_annual(request.GET['tiker'])

    companyData=tiker[0].head(int(request.GET.get('size'))).to_numpy()
    dataOfDate=tiker[0].head(int(request.GET.get('size'))).index.copy()
    print(companyData)   
    open =[]
    # close=[]
    for i in companyData:
        open.append(i[int(request.GET['status'])])
        # close.append(i[int()])
    context ={ 
        'companyName':companyOverview[0].Name[0],
        'Currency':companyOverview[0].Currency[0],
        'Country':companyOverview[0].Country[0],
        'Sector':companyOverview[0].Sector[0],
        "year":balanceSheet[0].fiscalDateEnding.to_numpy()[0],
        "totalAssets":balanceSheet[0].totalAssets.to_numpy()[0],
        "inventory":balanceSheet[0].inventory.to_numpy()[0],
        "totalShareholderEquity":balanceSheet[0].totalShareholderEquity.to_numpy()[0],
        "fiscalDateEnding":annualIncome[0].fiscalDateEnding.to_numpy()[0],
        "totalRevenue":annualIncome[0].totalRevenue.to_numpy()[0],
        "grossProfit":annualIncome[0].grossProfit.to_numpy()[0],
        "netIncome":annualIncome[0].netIncome.to_numpy()[0],
        # "cashFlow":cashFlow[0].operatingCashflow.to_numpy()[0],
        'Symbol':tiker[1].get('2. Symbol'),
        'information':tiker[1].get('1. Information').split()[0],
        'lastRefreshed':tiker[1].get('3. Last Refreshed'),
        'open':open,
        'status':request.GET['status'],
        'open':open,
        'Date':dataOfDate,
        'graph':request.GET['graph']
    }
    return render(request,'fullsite/newIndex.html' ,context)

def weekly(request):
    companyOverview=fd.get_company_overview(request.GET['tiker'])
    tiker=ts.get_weekly(request.GET['tiker']) # ye comment krunga
    annualIncome=fd.get_income_statement_annual(request.GET['tiker'])
    balanceSheet=fd.get_balance_sheet_annual(request.GET['tiker'])
    annualIncome=fd.get_income_statement_annual(request.GET['tiker'])
    # cashFlow=fd.get_cash_flow_annual(request.GET['tiker'])

    companyData=tiker[0].head(int(request.GET.get('size'))).to_numpy()
    dataOfDate=tiker[0].head(int(request.GET.get('size'))).index.copy()
    print(companyData)   
    open =[]
    # close=[]
    for i in companyData:
        open.append(i[int(request.GET['status'])])
        # close.append(i[int()])
    context ={ 
        'companyName':companyOverview[0].Name[0],
        'Currency':companyOverview[0].Currency[0],
        'Country':companyOverview[0].Country[0],
        'Sector':companyOverview[0].Sector[0],
        "year":balanceSheet[0].fiscalDateEnding.to_numpy()[0],
        "totalAssets":balanceSheet[0].totalAssets.to_numpy()[0],
        "inventory":balanceSheet[0].inventory.to_numpy()[0],
        "totalShareholderEquity":balanceSheet[0].totalShareholderEquity.to_numpy()[0],
        "fiscalDateEnding":annualIncome[0].fiscalDateEnding.to_numpy()[0],
        "totalRevenue":annualIncome[0].totalRevenue.to_numpy()[0],
        "grossProfit":annualIncome[0].grossProfit.to_numpy()[0],
        "netIncome":annualIncome[0].netIncome.to_numpy()[0],
        # "cashFlow":cashFlow[0].operatingCashflow.to_numpy()[0],
        'Symbol':tiker[1].get('2. Symbol'),
        'information':tiker[1].get('1. Information').split()[0],
        'lastRefreshed':tiker[1].get('3. Last Refreshed'),
        'open':open,
        'status':request.GET['status'],
        'open':open,
        'Date':dataOfDate,
        'graph':request.GET['graph']
    }
    return render(request,'fullsite/newIndex.html' ,context)


def monthly(request):
    companyOverview=fd.get_company_overview(request.GET['tiker'])
    tiker=ts.get_monthly(request.GET['tiker']) # ye comment krunga
    
    annualIncome=fd.get_income_statement_annual(request.GET['tiker'])

    balanceSheet=fd.get_balance_sheet_annual(request.GET['tiker'])
    annualIncome=fd.get_income_statement_annual(request.GET['tiker'])
    # cashFlow=fd.get_cash_flow_annual(request.GET['tiker'])

    companyData=tiker[0].loc[request.GET['to']:request.GET['from']].to_numpy()
    dataOfDate=tiker[0].loc[request.GET['to']:request.GET['from']].index.copy()
    print(companyData)

    open =[]
    close=[]
    print('>>',type(request.GET['from']),'>>',request.GET['to'],'>>>>',request.GET['status'])
    for i in companyData:
        open.append(i[int(request.GET['status'])])
        # close.append(i[int()])
    context ={ 
        'companyName':companyOverview[0].Name[0],
        'Currency':companyOverview[0].Currency[0],
        'Country':companyOverview[0].Country[0],
        'Sector':companyOverview[0].Sector[0],
        "year":balanceSheet[0].fiscalDateEnding.to_numpy()[0],
        "totalAssets":balanceSheet[0].totalAssets.to_numpy()[0],
        "inventory":balanceSheet[0].inventory.to_numpy()[0],
        "totalShareholderEquity":balanceSheet[0].totalShareholderEquity.to_numpy()[0],
        "fiscalDateEnding":annualIncome[0].fiscalDateEnding.to_numpy()[0],
        "totalRevenue":annualIncome[0].totalRevenue.to_numpy()[0],
        "grossProfit":annualIncome[0].grossProfit.to_numpy()[0],
        "netIncome":annualIncome[0].netIncome.to_numpy()[0],
        # "cashFlow":cashFlow[0].operatingCashflow.to_numpy()[0],
        'Symbol':tiker[1].get('2. Symbol'),
        'information':tiker[1].get('1. Information').split()[0],
        'lastRefreshed':tiker[1].get('3. Last Refreshed'),
        'open':open,
        'from':request.GET['from'],
        'status':request.GET['status'],
        'to':request.GET['to'],
        'open':open,
        'Date':dataOfDate,
        'close':close,
        'graph':request.GET['graph']
    }
    return render(request,'fullsite/newIndex.html' ,context)
