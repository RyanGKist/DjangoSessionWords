from django.shortcuts import render, HttpResponse, redirect

def index(request):
	if 'count' in request.session:
		return render(request, ('sessionWords/index.html'))
	else:
		request.session['count'] = [None]

		return render(request, ('sessionWords/index.html'))

def add_session(request):
	if request.method == 'POST':
			# request.session['word'] = request.POST['user_word']
			# request.session['color'] = request.POST['color']
			# print request.session['color']
			# request.session['fontSize'] = request.POST.get('fontSize')
			# print request.session['fontSize']
			if request.POST.get('fontSize') == 'on':
				fontStyle = 'bold'
			else:
				fontStyle = 'normal'
			temp = {
			'color' : request.POST['color'],
			'word' : request.POST['user_word'],
			'fontStyle': fontStyle
			}
		
			request.session['count'].append(dict(temp))
			print request.session['count']

			return render(request,'sessionWords/display.html')
	


# Create your views here.
