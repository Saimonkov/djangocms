from django.shortcuts import render

from charge.grub import about_three


def test(request):
    per = about_three()
    context={
        'per':per
    }
    return render(request, 'base.html',context)