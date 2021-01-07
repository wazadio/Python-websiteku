from django.shortcuts import render
from tugas.forms import FormTugas
from tugas.models import Tugas
from time import strftime

# Create your views here.
def tugas(request):
	data = Tugas.objects.all()
	for i in data:
		i.deadline = i.deadline.strftime('%d %B %Y')
	print(data[0].deadline)	
	#print(data[0].deadline.strftime('%d %B %Y'))
	return render(request, 'tugas.html', {'data': data})

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