from django.shortcuts import render
from django.db.models import Q

# Create your views here.
from app.models import *
def empdeptdata(request):
    LEDO=Emp.objects.select_related('DEPTNO').all()
    LEDO=Emp.objects.select_related('DEPTNO').filter(SAL__gt=5000)
    LEDO=Emp.objects.select_related('DEPTNO').filter(DEPTNO__DNAME='clerk')
    d={'LEDO':LEDO}
    return render(request,'empdeptdata.html',d)
def empmgr(request):
    LEMO=Emp.objects.select_related('MGR').all()
    LEMO=Emp.objects.select_related('MGR').filter(MGR__SAL__gt=100000)
    LEMO=Emp.objects.select_related('MGR').filter(COMM__isnull=False)
    LEMO=Emp.objects.select_related('MGR').filter(COMM__isnull=True)
    LEMO=Emp.objects.select_related('MGR').filter(MGR__COMM__isnull=False)
    LEMO=Emp.objects.select_related('MGR').filter(MGR__COMM__isnull=True)
    LEMO=Emp.objects.select_related('MGR').filter(MGR__ENAME='swathi')
    
    d={'LEMO':LEMO}
    return render(request,'empmgr.html',d)
def empmgrdept(request):
    LEMDO=Emp.objects.select_related('DEPTNO','MGR').all()
    LEMDO=Emp.objects.select_related('DEPTNO','MGR').filter(SAL__gte=100000)
    LEMDO=Emp.objects.select_related('DEPTNO','MGR').filter( Q(DEPTNO=20),Q(JOB='analyst'))
    LEMDO=Emp.objects.select_related('DEPTNO','MGR').filter(Q(ENAME='satish')| Q(EMPNO=2))
    LEMDO=Emp.objects.select_related('MGR','DEPTNO').filter(COMM__isnull=True,ENAME='navya')
    LEMDO=Emp.objects.select_related('MGR','DEPTNO').filter(MGR__COMM__isnull=True,COMM=50.00)
    LEMDO=Emp.objects.select_related('MGR','DEPTNO').filter(MGR__ENAME='swathi',ENAME='satish')
    d={'LEMDO':LEMDO}
    return render(request,'empmgrdept.html',d)


def empdeptpr(request):
    LDEO=Dept.objects.prefetch_related ('emp_set').all()
    print(LDEO)

    d={'LDEO':LDEO}
    return render(request,'empdeptpr.html',d)
