import xml.dom.minidom

from django.shortcuts import render_to_response


def about_three():
    dom = xml.dom.minidom.parse("http://www.cbr.ru/scripts/XML_daily.asp")
    dom.normalize()
    node1 = dom.getElementsByTagName("Valute")[0]
    #node2 = node1.nodeName
    node2='asdf1234asdf1234asdf1234asdf1234'
    print("name=" + node1.nodeName)

    return render_to_response('base.html', {'node2': node2} )