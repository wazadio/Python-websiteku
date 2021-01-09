from django.shortcuts import render
from tugas.forms import FormTugas
from tugas.models import Tugas
from time import strftime
from datetime import datetime

# Create your views here.
def tugas(request):
	data = Tugas.objects.all()
	mepet = []
	daftar = []
	for i in data:
		if i.deadline.month == datetime.now().month:
			if i.deadline.day == datetime.now().day:
				i.deadline = i.deadline.strftime('%d %B %Y')
				mepet.append(i)
			elif datetime.now().day == (i.deadline.day - 1):
				i.deadline = i.deadline.strftime('%d %B %Y')
				mepet.append(i)
			elif datetime.now().day == (i.deadline.day - 2):
				i.deadline = i.deadline.strftime('%d %B %Y')
				mepet.append(i)
			else:
				i.deadline = i.deadline.strftime('%d %B %Y')
				daftar.append(i)
		else:
				i.deadline = i.deadline.strftime('%d %B %Y')
				daftar.append(i)

	print(datetime.now())
	print(mepet)
	print(daftar)
	context = {
			'mepet': mepet,
			'daftar': daftar,
		}

	#print(data[0].deadline.strftime('%d %B %Y'))
	return render(request, 'tugas.html', context)

def tambah(request):
	form = FormTugas()

	if request.method == 'POST':
		Deadline = request.POST['deadline_year'] + "-" + request.POST['deadline_month'] + "-" + request.POST['deadline_day']
		Tugas.objects.create(
				matakuliah = request.POST['matakuliah'],
				deskripsi = request.POST['deskripsi'],
				deadline = Deadline,
				jam = request.POST['jam'],
			)


	context = {
		'form': form
	}
	return render(request, 'tambah.html', context)