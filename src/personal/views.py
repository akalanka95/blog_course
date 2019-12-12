from django.shortcuts import render

# Create your views here.
def home_screen_view(request):

    context = {}
    context['some_string'] = "this is some string that I passed"

    # context = {
    #     'some_string2': 'thisddhsidsdsdsdssd',
    #     'some_number': 125142512,
    # }

    list_of_values = []
    list_of_values.append("first entry")
    list_of_values.append("second entry")

    context['list_of_values'] = list_of_values

    return render(request , 'personal/home.html',context)